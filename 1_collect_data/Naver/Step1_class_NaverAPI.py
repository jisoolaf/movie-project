import urllib.request
import json
import datetime

###### 클래스 NaverAPI
class NaverAPI:
    ###### API 계정으로 접속
    def get_request_url(self, url):
        self.url = url
        client_id='crz2qOgxFNZE9g3n7Zxg'
        client_secret='ebKzukzImT'
        
        req=urllib.request.Request(self.url)
        req.add_header("X-Naver-Client-Id", client_id)
        req.add_header("X-Naver-Client-Secret",client_secret)
        
        try:
            response=urllib.request.urlopen(req)
            print( '[%s] Url Request Success' % (datetime.datetime.now()) )
            return response.read().decode('utf-8')
        
        except Exception as err:
            print(err)
            print( '[%s] Url Request Fail [url : %s]' % (datetime.datetime.now(), self.url) )
            return None
    
    ###### 네이버 영화 홈페이지에서 영화명 검색
    def getNaverMovieResult(self, movieNm, display):
        self.movieNm = movieNm
        self.display = display
        url='https://openapi.naver.com/v1/search/movie.json'
        url+='?query=%s'%(urllib.parse.quote(self.movieNm))
        url+='&display=%s'%(self.display)
        
        retData = self.get_request_url(url)
        
        if(retData == None):
            return None
        else:
            return json.loads(retData)
###### 클래스 NaverAPI







       
    
