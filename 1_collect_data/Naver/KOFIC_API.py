import urllib.request
import json
import datetime
import os
from pandas import DataFrame

class Kofic:
    def __init__(self):
        self.boxtype='searchMovieList'
    
    ###API에서 불러온 정보 json파일로 저장
    def toJson(self,result):
        with open('C:/myworkspace/MyPython/project1906/KOFIC_json/{}-{}movielist{}.json'.format(self.openStartDt,self.openEndDt,self.curPage.zfill(3)), 'w', encoding='utf-8') as file :
            json.dump(result, file, ensure_ascii=False, indent='\t')

    
    def getKOFIC_API_Result(self,boxtype,itemPerPage,curPage,openStartDt,openEndDt):
        self.url='http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/'+str(self.boxtype)+'.json'
        self.boxtype=boxtype
        self.openStartDt=openStartDt
        self.openEndDt=openEndDt
        self.curPage=curPage
        self.itemPerPage=itemPerPage
#         self.targetDt=targetDt
        key='128050ed13a19d060748d99577169d58'
        self.url+='?key=%s'%(key)
        self.url+='&curPage=%s'%(self.curPage)
        self.url+='&itemPerPage=%s'%(self.itemPerPage)
        self.url+='&openStartDt=%s'%(self.openStartDt)
        self.url+='&openEndDt=%s'%(self.openEndDt)
#         self.url+='&targetDt=%s'%(self.targetDt)
#         url+='&yearfrom=%d'%(2018)
#         url+='&yearto=%d'%(2019)
        
        retData = self.get_request_url(self.url)
        
        if(retData == None):
            return None
        
        else:
#             return json.loads(retData)
            self.toJson(json.loads(retData))
            print('{}년도부터 {}년도_{}영화리스트 정보가 저장되었습니다.'.format(self.openStartDt,self.openEndDt,self.curPage))
            
    def get_request_url(self,url):
        self.req=urllib.request.Request(self.url)
        try:
            response=urllib.request.urlopen(self.req)
            if response.getcode()==200:
                print('[%s] Url Request Success'%(datetime.datetime.now()))
                return response.read().decode('utf-8')
        except Exception as e:
            print(e)
            print('[%s] Url Request Success'%(datetime.datetime.now(),self.url))
            return None
    
    def get_movie_list(self,filename):
        rfile=open(filename,'rt',encoding='utf-8')
        rfile=rfile.read()
        result=json.loads(rfile)
        movieListResult=result['movieListResult']
        movielist=movieListResult['movieList'] #영화 묶음 리스트(100개)
        
        mymovie=list()    
            
        for onemovie in movielist: #onemovie는 사전타입
            imsi=onemovie['movieNm']
            mymovie.append(imsi)
        
        return mymovie
###20100101부터 20190609까지 날짜정리

import pandas

dt_index = pandas.date_range(start='20100101', end='20190609')
# pandas.date_range(start='20160901', end='20161031',freq='W-MON')
# 을 하면 해당 기간 매주 월요일들만 추출합니다.

# type(dt_index) => DatetimeIndex
# DatetimeIndex => list(str)
dt_list = dt_index.strftime("%Y%m%d").tolist()

# print(dt_list) #보이지 않지만 정리가 되어있음.

########################################
#클래스 실행(객체 생성)
kofic1=Kofic()
#영진위 api에서 데이터 불러오고 파일저장
# for idx in range(111):
#     kofic1.getKOFIC_API_Result('searchMovieList','100',str(idx+1),'2010','2019')

mylist=list()
#영화명 리스트에 모으기

for idx in range(111):
    #imsi는 각 파일 영화명묶음이고 타입은 리스트
    imsi=kofic1.get_movie_list('C:/myworkspace/MyPython/project1906/KOFIC_json/2010-2019movielist'+str(idx+1).zfill(3)+'.json') 
    for onename in imsi:
        mylist.append(onename)
print(len(mylist))

#리스트를 csv파일로 저장하기
myframe=DataFrame(mylist)

filename='영진위 영화목록(2010-2019).csv'

myframe.to_csv(filename,encoding='utf-8')

print(filename+'저장 완료되었습니다.')



# imsi=kofic1.get_movie_list('C:/myworkspace/MyPython/project1906/KOFIC_json/2010-2019movielist001.json')
# print(imsi)
##################클래스마무리###############
 
########밑에는 제이슨 파일 불러오는 코드 (영화명 불러오기)
# myfile='C:/myworkspace/MyPython/project1906/KOFIC_json/2010-2019movielist1.json'
# rfile=open(myfile,'rt',encoding='utf-8')
# # print(type(rfile))
# rfile=rfile.read()
# # print(type(rfile))
# jsonData=json.loads(rfile)
# # print(type(jsonData))
#   
# movieListResult=jsonData['movieListResult']
# # print(type(movieListResult))
# print(movieListResult)
# # print(movieListResult.keys())
# # print(movieListResult['movieNm'])    
# movielist=movieListResult['movieList']
# # print(type(movielist))
# # print(len(movielist))
# # for onedata in movielist:
# #     print(onedata)
