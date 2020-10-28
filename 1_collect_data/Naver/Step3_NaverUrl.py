from naver_Oribook_Expt.Step2_Naver_API_MovieDict import runClassNaverAPI
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re


class getBookExpt:
    def getOribook_expt(self, filename):
        self.filename = filename

        getMovieList = runClassNaverAPI()
        
        movieList = getMovieList.getKoficData(self.filename)
        # print(movieList)
        
        oribook_expt = []
    
        for oneList in movieList:
            koficNm = oneList[0]
            koficDr = oneList[1]
            naverResult = oneList[2]
            if naverResult != None:
                naverDictList = naverResult['items']
                for naverDict in naverDictList:
                    movieNm = naverDict['title'].replace('<b>','').replace('</b>','')
                    movieEnNm = naverDict['subtitle']
                    openYr = naverDict['pubDate']
                    movieDr = naverDict['director'].replace('<b>','').replace('</b>','')
                    movieDr = movieDr.rstrip('|').replace('|',',')                     
                    naverUrl = naverDict['link']                                            
                    response = urlopen(naverUrl)                                       
                    soup = BeautifulSoup(response, 'html.parser')
                    #print(soup)                                            
                    ###### 원작 도서 시작 
                    # 원작도서 있음 : 1 / 없음 : 0
                    myLi = soup.find('a', attrs={'title':'원작 도서'})
                    
                    if myLi != None:
                        ori_book = 1
                    else:
                        ori_book = 0
                    
                    print('원작도서 : %d' % (ori_book))
                    ###### 원작 도서 끝
                                              
                    ###### 기대지수 시작
                    naver_ex_pt = soup.select_one('span#interest_cnt_basic')
                    if naver_ex_pt != None:
                        naver_ex_pt = naver_ex_pt.get_text()
                        naver_ex_pt = re.sub('[가-힣]+','', naver_ex_pt)
                        naver_ex_pt = naver_ex_pt.replace(',', '')
                        naver_ex_pt = int(naver_ex_pt)                    
                        print('기대지수 : %s' % (naver_ex_pt))
                        ###### 기대지수 끝
                    else:
                        naver_ex_pt = ''
                        
                    oribook_expt.append([movieNm, movieEnNm, openYr, movieDr, ori_book, naver_ex_pt])
                    print('-'*50)  
                                 

                            # if movieDr[0][0:2] == koficDr[0][0:2]:
                                # naverUrl = naverDict['link'] 
                                # print([koficNm, movieNm, koficDr, movieDr, naverUrl])  
                            # elif movieDr[0][-2:] == koficDr[0][-2:]:
                                # naverUrl = naverDict['link'] 
                                # print([koficNm, movieNm, koficDr, movieDr, naverUrl])
                            # else :
                                # print('감독 다름') 
                                # print([koficNm, movieNm, koficDr, movieDr])
                                # pass


        return oribook_expt
        
            


# print(UrlList)


getNaverData = getBookExpt()

NaverData = getNaverData.getOribook_expt('KOFIC_data(2010-2019).csv')
                
NaverDf = pd.DataFrame(NaverData, columns=['movieNm', 'movieEnNm', 'openYr', 'movieDr', 'ori_book', 'naver_ex_pt'])
print('@'*50)
print(NaverDf)

# NaverDf.to_csv('naver_Oribook_Expt(1).csv', header=True, index = False, encoding='utf-8')
# NaverDf.to_csv('naver_Oribook_Expt(2).csv', header=True, index = False, encoding='utf-8')
# NaverDf.to_csv('naver_Oribook_Expt(3).csv', header=True, index = False, encoding='utf-8')
# NaverDf.to_csv('naver_Oribook_Expt(4).csv', header=True, index = False, encoding='utf-8')
# NaverDf.to_csv('naver_Oribook_Expt(5).csv', header=True, index = False, encoding='utf-8')
# NaverDf.to_csv('naver_Oribook_Expt(6).csv', header=True, index = False, encoding='utf-8')
NaverDf.to_csv('naver_Oribook_Expt(2)_second.csv', header=True, index = False, encoding='utf-8')


print('finished')   
   
   
   
   
