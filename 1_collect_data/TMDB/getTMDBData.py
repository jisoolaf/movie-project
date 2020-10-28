import http.client
import json
import pandas as pd


payload = "{}"
TMDBData = []

# page 맥시멈 : 1000
# 개봉일자가 신뢰도가 떨어진 영화가 많아서 현재까지 한국에서 개봉한 모든 영화를 크롤링하는 코드를 작성했습니다.
# for idx in range(1000):
for idx in range(1):
# for idx in range(200):
# for idx in range(200, 425):   
    mainUrl = "/3/discover/movie?page="
    mainUrl += str(idx+1) 
    mainUrl += "&include_video=true&include_adult=true&sort_by=original_title.asc&language=ko-KR&region=KR&api_key=2b4a725a283b9fa435aca3507c61bae2"
    
    try:
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        conn.request("GET", mainUrl, payload)
        main_res = conn.getresponse()
        if main_res.getcode() == 200:
            print('[mainUrl] Connected!')
            json_main = json.loads(main_res.read().decode('utf-8'))
       
    except Exception as e:
        print('[mainUrl] Access failed.', e)
        continue

    movieList = json_main['results']
    

 
    for onemovie in movieList:
#         print(onemovie)
#         print('-'*50)
#         print(onemovie.keys())
        id = onemovie['id']
        movieNm = onemovie['title']
        openDt = onemovie['release_date']
        if openDt == None:
            openDt = ''

        detailUrl = "/3/movie/"
        detailUrl += str(id)
        detailUrl += "?language=en-US&api_key=2b4a725a283b9fa435aca3507c61bae2"
        
        try:
            conn = http.client.HTTPSConnection("api.themoviedb.org")
            conn.request("GET", detailUrl, payload)
            detail_res = conn.getresponse()
            if detail_res.getcode() == 200:
                print('[detailUrl] Connected!')
                json_detail = json.loads(detail_res.read().decode('utf-8'))
       
        except Exception as e:
            print('[detailUrl] Access failed.', e)
            continue

# #         print(json_detail)
# #         print(type(json_detail))
        movieOriNm = json_detail['title']
#         print(movieOriNm)
#         print('-'*50)
        budget = json_detail['budget']
        if budget == 0:
            budget = ''
        series_dict = json_detail['belongs_to_collection']
        if series_dict != None:
            series = 1
        else : 
            series = 0
        ori_lang_list = json_detail['spoken_languages']
#         print(ori_lang_list)
        ori_lang = []
        if ori_lang_list != []:
            for onelang in ori_lang_list :
                ori_lang.append( onelang['iso_639_1'] )
        else : 
            ori_lang = ''
        
#         print(budget) 
#         print(series)
#         print(ori_lang)

        creditUrl = "/3/movie/"
        creditUrl += str(id)
        creditUrl += "/credits?api_key=2b4a725a283b9fa435aca3507c61bae2"
        
        try:
            conn = http.client.HTTPSConnection("api.themoviedb.org")
            conn.request("GET", creditUrl, payload)
            credit_res = conn.getresponse()
            if credit_res.getcode() == 200:
                print('[creditUrl] Connected!')
                json_credit = json.loads(credit_res.read().decode('utf-8'))
       
        except Exception as e:
            print('[creditUrl] Access failed.', e)
            continue
         
#         print(json_credit)
        crew_list = json_credit['crew']
        cast_list = json_credit['cast']
#         print(crew_list)
#         print('-'*20+'crew'+'-'*20)
#         print(cast_list)
#         print('-'*20+'cast'+'-'*20)
#         print('-'*50)
    
        crewData = []
        castData = []
        movieDr = []
        
        if crew_list != []:
            for onecrew in crew_list :
                crewDict = dict()
                crewDict['name'] = onecrew['name']
                crewDict['department'] = onecrew['job']
                crewDict['gender'] = onecrew['gender']
                crewData.append(crewDict)
                if onecrew['job'] == 'Director':
                    movieDr.append(onecrew['name'])
        else : 
            crewData = ''
            movieDr = ''
        
        if cast_list != []:
            for onecast in cast_list :
                castDict = dict()
                castDict['name'] = onecast['name']
                castDict['gender'] = onecast['gender']
                castData.append(castDict)
        else : 
            castData = ''
        
#         print(crewData)
#         print('-'*20+'crew'+'-'*20)
#         print(castData)
#         print('-'*20+'cast'+'-'*20)

        
        keyUrl = "/3/movie/"
        keyUrl += str(id)
        keyUrl += "/keywords?api_key=2b4a725a283b9fa435aca3507c61bae2"
        try:
            conn = http.client.HTTPSConnection("api.themoviedb.org")
            conn.request("GET", keyUrl, payload)
            key_res = conn.getresponse()
            if key_res.getcode() == 200:
                print('[keyUrl] Connected!')
                json_key = json.loads(key_res.read().decode('utf-8'))
       
        except Exception as e:
            print('[keyUrl] Access failed.', e)
            continue
            
        key_list = json_key['keywords']
        
#         print(key_list)

        keyWord = []
        if key_list != []:
            for onekey in key_list:
                keyWord.append( onekey['name'])
        else:
            keyWord = ''
                

            
#         print(movieNm)
#         print('key:',keyword)
#         print('-'*50)

        TMDBData.append([movieNm, movieOriNm, openDt, movieDr, budget, ori_lang, series, crewData, castData, keyWord])
# # #     print(TMDBData)
# # #     print('-'*50)
# # #     print('#'*50)
        print('-'*50)
    print('#'*50)


# print(TMDBData)

TMDBDf = pd.DataFrame(TMDBData, columns=['movieNm', 'movieOriNm', 'openDt', 'movieDr', 'budget', 'ori_lang', 'series', 'crewData', 'castData', 'keyWord'])

print(TMDBDf)
print('-'*50)

TMDBDf.to_csv('TMDB(1)_oriNm.csv', header=True, index = False, encoding='utf-8')
# TMDBDf.to_csv('TMDB(2)_oriNm.csv', header=True, index = False, encoding='utf-8')

print('finished')
    

# ### gender - 1: 여자 / 2: 남자 / 0 : 결측?
# ### 시리즈 - 0: 없음 / 1: 있음
