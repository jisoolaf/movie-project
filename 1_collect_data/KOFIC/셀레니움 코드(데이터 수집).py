# 셀레니움 이용 KOBIS 홈페이지 영화 관객수 크롤링

import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('http://www.kobis.or.kr/kobis/business/stat/offc/searchOfficHitTotList.do?searchMode=year')
driver.find_element_by_xpath("//option[@value='" + str(2010) + "']").click()
driver.find_element_by_xpath("//button[@class='btn_blue']").click()
time.sleep(5)     

totacc=[]
totmovienm=[]
for nextpagenum in range(0, 104):
    
    imsiacc=[]
    imsimovienm=[]
    strpage = 0
    endpage = 10
    
    if nextpagenum != 0:
        strpage += 10*nextpagenum
        endpage += 10*nextpagenum
        
    for pagenum in range(strpage,endpage):
        driver.find_element_by_xpath("//a[@onclick=\"goPage('" + str(pagenum+1) + "')\"]").click()
        time.sleep(3) 
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        tag_body = soup.find('tbody')
        tags_tr = tag_body.findAll('tr')
#         print(tags_tr)
        movienm=[]
        audiacc=[]

        for tr in tags_tr:
            tds = list(tr.find_all('td'))
            for td in tds:
                movie = tds[1].text
                peoplecount = tds[11].text
            audiacc.append(peoplecount)
            movienm.append(movie.strip())
        imsiacc.append(audiacc)
        imsimovienm.append(movienm)
    driver.find_element_by_xpath("//a[@class='btn next']").click()
#     print(soup)
    time.sleep(4)
    totacc.append(imsiacc)
    totmovienm.append(imsimovienm)
    
for pagenum in range(1040,1047):
    driver.find_element_by_xpath("//a[@onclick=\"goPage('" + str(pagenum+1) + "')\"]").click()
    time.sleep(3) 
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    tag_body = soup.find('tbody')
    tags_tr = tag_body.findAll('tr')
#         print(tags_tr)
    for tr in tags_tr:
        tds = list(tr.find_all('td'))
        for td in tds:
            movie = tds[1].text
            peoplecount = tds[11].text
        audiacc.append(peoplecount)
        movienm.append(movie.strip())
    imsiacc.append(audiacc)
    imsimovienm.append(movienm)
totacc.append(imsiacc)
totmovienm.append(imsimovienm)

# print(totmovienm)
# print(totacc)
    


koficdata = pd.DataFrame()
koficdata = koficdata.append({'movieNm':'', 'audiAcc':''}, ignore_index=True)

outnum = len(totmovienm)
midnum = len(imsimovienm)
innum = len(movienm)
for myout in range(0, outnum):
    for mymid in range(0, midnum):
        for myin in range(0, innum):
            if(koficdata.ix[(100*myout + 10*mymid + myin), 'movieNm'] == None):
                return None
            else:
                koficdata.ix[(100*myout + 10*mymid + myin), 'movieNm'] = totmovienm[myout][mymid][myin]
                koficdata.ix[(100*myout + 10*mymid + myin), 'audiAcc'] = totacc[myout][mymid][myin]
    
# print(koficdata)

filename = 'imsii.csv'
 
koficdata.to_csv( filename, encoding = 'utf-8')
print(filename + '파일로 저장됨')
         