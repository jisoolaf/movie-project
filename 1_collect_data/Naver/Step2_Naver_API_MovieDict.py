from naver_Oribook_Expt.Step1_class_NaverAPI import NaverAPI
import pandas as pd
import time

class runClassNaverAPI:
    ###### KOFIC 영화명, 감독명 추출
    def getKoficData(self, filename):
        self.filename = filename
        
        koficData = pd.read_csv(self.filename)
        koficData.fillna('NaN', inplace=True)
        # print(koficData)
        
        koficNmDr = koficData[['영화명', '감독']]
        # print(koficNmDr)
        # print(type(koficNmDr))
        movieList = self.getMovieList(koficNmDr)
        return movieList
    
    ###### 영화리스트 : [kofic영화명, kofic감독, NaverAPI검색결과]
    def getMovieList(self, dataframe):
        self.dataframe = dataframe 
        naver = NaverAPI()
        length = len(self.dataframe)
        movieList = []
        
#         print(length)
        
#         for idx in range(length):
#         for idx in range(10):
#         for idx in range(2000):
#        for idx in range(2000, 4000):
#         for idx in range(4000, 6000):
#         for idx in range(6000, 8000):
#         for idx in range(8000, 10000):
#         for idx in range(10000, 10465):
            print('%d번째 영화 크롤링'%(idx+1))
            koficNm = self.dataframe.iloc[idx, 0]
            koficDr = self.dataframe.iloc[idx, 1]
            # print(idx)
            # print(koficNm)
            # print(koficDr)
            # print('-'*50)
                      
            display_count=100
              
            ###### Naver API에서 해당 영화명 검색 결과 추출 Start    
            naverResult=naver.getNaverMovieResult(koficNm, display_count)
            movieList.append([koficNm, koficDr, naverResult])
            # print(naverResult) 
            # print('#'*50)  
                
            # HTTP Error 429: Too Many Requests
            # 에러를 방지하기 위한 시간차 
            time.sleep(0.5)
            ###### Naver API에서 해당 영화명 검색 결과 추출 End
        # print(movieList)
        return movieList

# run = runClassNaverAPI()
# 
# run.getKoficData('KOFIC_data(2010-2019).csv')


