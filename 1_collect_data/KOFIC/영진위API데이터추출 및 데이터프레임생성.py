# 영화진흥위원회 API에서 영화목록 및 상세내용 저장 후 DataFrame 생성


import urllib.request
import json
import datetime


class searchMovieList:
    def __init__(self):
        self.boxtype = 'searchMovieList'
        
    def toJson(self, result):
        with open('C:/Users/DELL/eclipse-workspace/HomeTraining/Home/2010-2019movielist/{}-{}movielist{}.json'.format(self.openStartDt,self.openEndDt,self.curPage), 'w', encoding='utf-8') as file :
            json.dump(result, file, ensure_ascii=False, indent= '\t')
            
    def getKOFIC_API_Result(self, boxtype, itemPerPage, curPage, openStartDt, openEndDt ):
        self.url='http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/'+str(self.boxtype)+'.json'
        self.boxtype=boxtype
        self.openStartDt=openStartDt
        self.openEndDt=openEndDt
        self.curPage=curPage
        self.itemPerPage=itemPerPage    
        
        key='8ccfd7e4b86fa70f21da9b3bf8cfdc8e'
        self.url+='?key=%s'%(key)
        self.url+='&curPage=%s'%(self.curPage)
        self.url+='&itemPerPage=%s'%(self.itemPerPage)
        self.url+='&openStartDt=%s'%(self.openStartDt)
        self.url+='&openEndDt=%s'%(self.openEndDt)
        
        retData = self.get_request_url(self.url)
        
        if(retData == None):
            return None
        else:
            self.toJson(json.loads(retData))
            print('{}년도부터 {}년보 _{} 영화리스트 정보가 저장되었습니다.'.format(self.openStartDt, self.openEndDt, self.curPage))
            
            
    def get_request_url(self, url):
        self.req = urllib.request.Request(self.url)
        try:
            response=urllib.request.urlopen(self.req)
            if response.getcode()==200:
                print('[%s] Url Request Success'%(datetime.datetime.now()))
                return response.read().decode('utf-8')
        except Exception as e:
            print(e)
            print('[%s] Url Request Success'%(datetime.datetime.now(),self.url))
            return None
        
class searchMovieInfo(searchMovieList):
    def __init__(self):
        self.boxtype = 'searchMovieInfo'


    def getKOFIC_API_Result(self, movieCd, idx):
        self.url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/'+str(self.boxtype)+'.json'
        self.movieCd=movieCd
        self.idx = idx
         
        key = '8ccfd7e4b86fa70f21da9b3bf8cfdc8e'
        self. url += '?key=%s'%(key)
        self.url += '&movieCd=%s'%(self.movieCd)
         
        retData = self.get_request_url(self.url)
         
        if(retData == None):
            return None 
        else:
            with open('C:/Users/DELL/eclipse-workspace/HomeTraining/Home/2010-2019movielist/2010-2019movieinfo_{}.json'.format(self.idx), 'w', encoding='utf-8') as file :
                json.dump(json.loads(retData), file, ensure_ascii=False, indent= '\t')
            print('영화리스트 정보가 저장되었습니다.')
     
    def get_request_url(self, url):
        self.req = urllib.request.Request(self.url)
        try:
            response=urllib.request.urlopen(self.req)
            if response.getcode()==200:
                print('[%s] Url Request Success'%(datetime.datetime.now()))
                return response.read().decode('utf-8')
        except Exception as e:
            print(e)
            print('[%s] Url Request Success'%(datetime.datetime.now(),self.url))
            return None    
     
        
import pandas

searchmovie = searchMovieList()
totallist = []

startmv = 0
endmv = 25

for idx in range(startmv, endmv):
    searchmovie.getKOFIC_API_Result('searchMovieList', '100', str(idx+1), '2010', '2019')
    myfile='C:/Users/DELL/eclipse-workspace/HomeTraining/Home/2010-2019movielist/2010-2019movielist{}.json'.format(str(idx+1))
    rfile=open(myfile,'rt',encoding='utf-8')
    rfile=rfile.read()
    jsonData=json.loads(rfile)
    movieListResult=jsonData['movieListResult']
    # print(movieListResult)
    movielist=movieListResult['movieList']
#     print(movielist)
    totallist.append(movielist)
# print(len(movielist))
# print(len(totallist))

searchmovieinfo = searchMovieInfo()

moviedata = []
movienm = []
movienmen = []
moviecd = []
opendt = []

directornm = []
directornmen = []
showtm = []
nations = []
watchgrade = []
company = []
genre = []
people_list = []
topeople_list = []

moviecnt = 0
for movielist in totallist:
    for onedata in movielist:
        searchmovieinfo.getKOFIC_API_Result(onedata['movieCd'], (moviecnt+1))
        
        moviecd.append(onedata['movieCd'])
        movienm.append(onedata['movieNm'].strip())
        movienmen.append(onedata['movieNmEn'].strip())
        opendt.append(onedata['openDt'])
    
        
        myfile1='C:/Users/DELL/eclipse-workspace/HomeTraining/Home/2010-2019movielist/2010-2019movieinfo_{}.json'.format((moviecnt+1))
        moviecnt += 1
#         print(moviecnt)
        rfile1=open(myfile1,'rt',encoding='utf-8')
        rfile1=rfile1.read()
        jsonData1=json.loads(rfile1)
#         print(jsonData1)
        if jsonData1['movieInfoResult']['movieInfo']['showTm'] != []:
            showtm.append(jsonData1['movieInfoResult']['movieInfo']['showTm'])
        else:
            showtm.append(None)
        if jsonData1['movieInfoResult']['movieInfo']['audits'] != []:
            watchgrade.append(jsonData1['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm'])
        else:
            watchgrade.append(None)
            
        if jsonData1['movieInfoResult']['movieInfo']['directors'] != []:
            directornm.append(jsonData1['movieInfoResult']['movieInfo']['directors'][0]['peopleNm'])
            directornmen.append(jsonData1['movieInfoResult']['movieInfo']['directors'][0]['peopleNmEn'])
        else:
            directornm.append(None)
            directornmen.append(None)
            
        onegenre_list = []
        if jsonData1['movieInfoResult']['movieInfo']['genres'] != []:
            for onegenre in range(len(jsonData1['movieInfoResult']['movieInfo']['genres'])):
                onegenre_list.append(jsonData1['movieInfoResult']['movieInfo']['genres'][onegenre]['genreNm'])
            genre.append(onegenre_list)
        else:
            genre.append(None)
            
        onecompany_list = []
        if jsonData1['movieInfoResult']['movieInfo']['companys'] != []:
    #             print(jsonData1['movieInfoResult']['movieInfo']['companys'])
            onecompany_list = []
            for onecompany in range(len(jsonData1['movieInfoResult']['movieInfo']['companys'])):
                if jsonData1['movieInfoResult']['movieInfo']['companys'][onecompany]['companyPartNm'] == '배급사':
                    onecompany_list.append(jsonData1['movieInfoResult']['movieInfo']['companys'][onecompany]['companyNm'])
            company.append(onecompany_list)
        else:
            company.append(None)
        
        onenation_list = []
        for onenation in range(len(jsonData1['movieInfoResult']['movieInfo']['nations'])):
            onenation_list.append(jsonData1['movieInfoResult']['movieInfo']['nations'][onenation]['nationNm'])
        nations.append(onenation_list)
        
        name_list = []
        role_list = []
        people_list = []
        
        if jsonData1['movieInfoResult']['movieInfo']['actors'] != [] or jsonData1['movieInfoResult']['movieInfo']['staffs']  != []:
            for onepeople in range(len(jsonData1['movieInfoResult']['movieInfo']['actors'])):
                name_list.append(jsonData1['movieInfoResult']['movieInfo']['actors'][onepeople]['peopleNm'])
                role_list.append(jsonData1['movieInfoResult']['movieInfo']['actors'][onepeople]['cast'])
              
            for onestaff in range(len(jsonData1['movieInfoResult']['movieInfo']['staffs'])):
                name_list.append(jsonData1['movieInfoResult']['movieInfo']['staffs'][onestaff]['peopleNm'])
                role_list.append(jsonData1['movieInfoResult']['movieInfo']['staffs'][onestaff]['staffRoleNm'])
            people_list = list(zip(name_list, role_list))
    #             print(people_list)
            
        else:
            people_list.append('notpeople')
            
        if 'notpeople' in people_list:
            topeople_list.append(None)
        else:
            topeople_list.append(people_list)


import pandas as pd

moviedf = pd.DataFrame()
moviedf = moviedf.append(
    {'movieNm':'', 'movieNmEn':'', 'openDt':'', 'showTm':'', 'watchGradeNm':'', 'genreNm':'', 'companyNm':'', 
     'nationNm':'', 'peopleNm':'', 'directorNm':'', 'directorNmEn':''}, ignore_index=True)

num = len(moviecd)
# print(num)
for i in range(0, num):
    moviedf.ix[i, 'movieNm'] = movienm[i]
    moviedf.ix[i, 'movieNmEn'] = movienmen[i]
    moviedf.ix[i, 'openDt'] = opendt[i]
    moviedf.ix[i, 'directorNm'] = directornm[i]
    moviedf.ix[i, 'directorNmEn'] = directornmen[i]
    moviedf.ix[i, 'showTm'] = showtm[i]
    moviedf.ix[i, 'watchGradeNm'] = watchgrade[i]
    moviedf.ix[i, 'genreNm'] = genre[i]
    moviedf.ix[i, 'companyNm'] = company[i]
    moviedf.ix[i, 'nationNm'] = nations[i]
    moviedf.ix[i, 'peopleNm'] = topeople_list[i]

print(moviedf)

movie_use = moviedf[ (moviedf.openDt >= '20100101') & (moviedf.openDt <= '20190609')]
print(movie_use)

filename = 'imsi01.csv'
 
movie_use.to_csv( filename, encoding = 'utf-8')
print(filename + '파일로 저장됨')
         

