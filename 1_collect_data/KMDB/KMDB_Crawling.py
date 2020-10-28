import urllib.request
import json
import pandas as pd
from pandas import DataFrame
from json import JSONDecodeError
import re


service_key = ''


def urlRequest(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('크롤링 성공!')
            
            return response.read().decode('utf-8')
    
    except Exception as e:
        print('크롤링 실패 ㅜㅜ', e, '확인바람')
        
        return None


def movieExtractor(startdate, enddate, count):
    
    end_point = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json.jsp?'
    
    parameters = 'collection=kmdb_new'
    parameters += '&detail=Y'
    parameters += '&listCount=1'
    parameters += '&startCount=' + str(count)
    parameters += '&sort=title'
    parameters += '&releaseDts=' + str(startdate)
    parameters += '&releaseDte=' + str(enddate)
    parameters += '&ServiceKey=' + service_key
    
    url = end_point + parameters
    
    jsondata = urlRequest(url)
    
    if jsondata == None:
        
        return None
    
    else:
        try:
            return json.loads(jsondata)
        except JSONDecodeError as e:
            print(e)
            print('JSON데이터에 문제가 있습니다 직접 확인해주세요!')
            return None


def kmdbValueSearcher(year, index, *keys):
    
    end_point = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json.jsp?'
    
    parameters = 'collection=kmdb_new'
    parameters += '&detail=Y'
    parameters += '&listCount=1'
    parameters += '&startCount=' + str(index-1)
    parameters += '&sort=title'
    parameters += '&releaseDts=' + str(year) + '0101'
    parameters += '&releaseDte=' + str(year) + '1231'
    parameters += '&ServiceKey=' + service_key
    
    url = end_point + parameters
    
    data = urlRequest(url)
    
    if data == None:
        
        return None
    else:
        valuelist = list()
        for key in keys:
            
            if key in ['rating','director']:
                value = eval(re.search('(?<="%s":)\[.*?\]'%(key), data).group())
                valuelist.append(value)
            else:
                match = re.search('"%s":".*?"'%(key),data)
                value = re.search(':".*?"',match.group()).group().strip(':"')
                valuelist.append(value)
            
        return valuelist


yearlist = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
startdate = '0101'
enddate = '0609'
movielist=list()
columns = ['개봉일','영화명','영문명','감독명','키워드','수상내역','줄거리']


for year in yearlist:
    for idx in range(1000):
        power = True
        print('%s년 %d번째 영화'%(year, idx+1))
        
        if year == '2019':
            moviedata = movieExtractor(int(year+startdate), int(year+enddate), idx)
        else:
            moviedata = movieExtractor(int(year+'0101'), int(year+'1231'), idx)
        try:
            for moviedict in moviedata['Data']:
            
                if moviedict['Result']:
                    for resultdict in moviedict['Result']:
                        for ratingdata in resultdict['rating']:
                            
                            if ratingdata['ratingMain'] == 'Y':
                                rel_data = ratingdata['releaseDate']
                                break
                        
                        all_dir = ''
                        if resultdict['director']:
                            for dirdata in resultdict['director']:
                                all_dir += dirdata['directorNm'] + ','
                        
                            
                        movielist.append([rel_data, resultdict['title'], resultdict['titleEng'], all_dir, resultdict['keywords'], resultdict['Awards1']+'|'+resultdict['Awards2'], resultdict['plot']])

                else:
                    power = False
                    break
        
            if not power:
                break
        except TypeError as e:
            print(e)


errorlist = ['2015년123','2015년362','2015년741','2016년515','2017년838','2018년432','2018년653']


for error in errorlist:
    intargs = error.split('년')
    valuelist = kmdbValueSearcher(int(intargs[0]), int(intargs[1]), 'rating', 'director', 'title', 'titleEng', 'keywords', 'Awards1', 'Awards2', 'plot')
    
    for err_ratingdata in valuelist[0]:
        
        if err_ratingdata['ratingMain'] == 'Y':
            err_rel_data = err_ratingdata['releaseDate']
            break
    
    err_all_dir = ''
    if valuelist[1]:
        for err_dirdata in valuelist[1]:
            err_all_dir += err_dirdata['directorNm'] + ','
            
    movielist.append([err_rel_data, valuelist[2], valuelist[3], err_all_dir, valuelist[4], valuelist[5]+'|'+valuelist[6], valuelist[7]])


movietable = DataFrame(movielist, columns=columns)
movietable = movietable.sort_values('영화명')
movietable['영화명'] = movietable['영화명'].apply(lambda x: x.strip())
movietable['수상내역'] = movietable['수상내역'].apply(lambda x: x.strip('|'))
movietable['감독명'] = movietable['감독명'].apply(lambda x: x.strip(','))
movietable = movietable.reindex(['영화명','영문명','감독명','개봉일','키워드','줄거리','수상내역'], axis=1)
movietable['개봉일'] = pd.to_datetime(movietable['개봉일'])
movietable.info()
movietable.to_csv('KMDB.csv', index=False, encoding='utf-8')

