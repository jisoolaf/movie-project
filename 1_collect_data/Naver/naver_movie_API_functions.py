import json
import urllib.request
import datetime
import pandas as pd 
import time
import re

class Naver_movie_API():
    
    def __init__(self,moviename):
        self.moviename=moviename

    ##api계정으로 접속
    def get_request_url(self,url):
        client_id='sQ_53I11un7a4GN_0E_v'
        client_secret='BylBuZooyk'
        
        req=urllib.request.Request(self.url)
        req.add_header("X-Naver-Client-Id", client_id)
        req.add_header("X-Naver-Client-Secret",client_secret)
        try:
            response=urllib.request.urlopen(req)
            if response.getcode()==200:
                print('[%s] Url Request Success'%(datetime.datetime.now()))
                return response.read().decode('utf-8')
        except Exception as e:
            print(e)
    #         print(url)##190617
            print('[%s] Url Request Success'%(datetime.datetime.now(),self.url))
            return None
    
    #영화 홈페이지에서 영화명검색
    def getNaverMovieResult(self,moviename,display,yearfrom=2010,yearto=2019):
            no_use_words=(' / ,:, * ,?, " ,<, >, |')
            self.url='https://openapi.naver.com/v1/search/movie.json'
            self.url+='?query=%s'%(urllib.parse.quote(self.moviename.replace(no_use_words,'')))
            self.url+='&display=%s'%(display)
            self.url+='&yearfrom=%d'%(yearfrom)
            self.url+='&yearto=%d'%(yearto)
            
            retData = self.get_request_url(self.url)
            
            if(retData == None):
                return None
            
            else:
                return json.loads(retData)
    
    ###API에서 불러온 정보 json파일로 저장
    def toJson(self,result,Savepath='C:/myworkspace/MyPython/project1906/Naver_movie_omitted_json/'):
        no_use_words='[/:*?"<>|]'
        save_name=re.sub(no_use_words,'',self.moviename)
        with open(Savepath+'{}.json'.format(save_name), 'w', encoding='utf-8') as file :
            json.dump(result, file, ensure_ascii=False, indent='\t')
