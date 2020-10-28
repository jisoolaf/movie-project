import numpy as np
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import re

no_use_words='[/:*?"<>|]'

#총댓글수 구하기
def get_totalNo_reply(link):
    link=link.replace('basic','pointWriteFormList')
    link+='&type=before&page=1' #1페이지 한해서만 가지고오는것이므로 페이지에 대하여 정의필요
    resp=requests.get(link)
    html=BeautifulSoup(resp.content,'html.parser')
    
    score_total=html.find('div',{'class':'score_total'})
    ems=score_total.findAll('em')
    
    if ems == None:
        
        total_reply=0
        
    else:
        
        total_reply=ems[1].getText().replace(',','') #str 타입 #전체 개봉전 댓글수 #1000단위 이상의 경우 ,로 구분해놔서 주의요함
        total_reply=int(total_reply)
    
    return total_reply


#1페이지당 총 게시글수 10
#먼저 전체 게시글수를 구하고 10으로 나눈것 +1 = 전체페이지 수
#전체 댓글페이지수 구하기
def get_total_page(link):
    total_reply=get_totalNo_reply(link)
   
    total_page=int(total_reply/10)+1 

    return total_page


#개봉전 전체 평점
def get_before_score(link):
    link=link.replace('basic','point')
    resp=requests.get(link)
    html=BeautifulSoup(resp.content,'html.parser')
    
    try:
        beforePoinArea=html.find(id='beforePointArea')
        
        starscore=beforePoinArea.find('div',{'class':'star_score'})
        scorelist=starscore.findAll('em')
            
        score=''
        for oneitem in scorelist:
            number1=oneitem.getText()
            score+=number1

    except Exception as e:
        print(e)
        score='None'

    return score



######코드 실행문 시작
myfile='링크모음.csv'

mylink=pd.read_csv(myfile)
result=mylink.values    #ndarray 타입
result=result.tolist() #[title,link] 뭉치 리스트
# result=result.flatten().tolist() #하나의 리스트로 만들기
# onelink=result[0]


###전체 개봉전 덧글 및 총 덧글갯수, 평점 구하기
##각 영화별로 실행하기
idx=3896
wait=0.125
for title,onelink in result[3896:]:
    idx+=1
# for title,onelink in result[:2]:
    total_reply=get_totalNo_reply(onelink) #영화 별 전체댓글수
    before_score=get_before_score(onelink)#영화 별 개봉전 총평점
    total_page=get_total_page(onelink) #우선 전체 댓글 페이지수를 구한다.
    mylink=onelink.replace('basic','pointWriteFormList')+'&type=before&page={}'
    
    ##댓글저장하기
    save_Reply=list() #댓글을 저장할 리스트
    for page_idx in range(1,total_page+1):
        imsi_link=mylink.format(page_idx) #page_idx:1~total_page
        
        resp=requests.get(imsi_link)
        html=BeautifulSoup(resp.content,'html.parser')
 
        score_result=html.find('div',{'class':'score_result'})
        
        if score_result !=None:
            for li in score_result.findAll('li'):
                reply=li.find('p').getText()
                save_Reply.append(reply)
        
        else:
            save_Reply.append('무플(댓글없음)')
        ##1페이지에 대한 댓글 리스트에 추가 완료
    
    #댓글리스트 뒤에서 두번째 개봉전 전체 평점 추가
    
    save_Reply.append('개봉전 평점: {}'.format(before_score))
    
    #댓글리스트 마지막에 총 댓글수 추가
    save_Reply.append('전체 댓글수: {}'.format(total_reply))
    
    #각 영화마다 댓글리스트 csv파일로 저장하기
    mypath='C:/myworkspace/MyPython/project1906/Naver_reply_list/'
      
    data=pd.DataFrame(save_Reply)
    data.to_csv(mypath+str(idx).zfill(5)+'_{}_영화 개봉전 댓글모음,평점,전체댓글 수.csv'.format(re.sub(no_use_words,'',title)),
                    encoding='utf-8',index=False)
    print('{}_영화 개봉전 댓글모음,평점,전체댓글 수.csv 저장완료'.format(re.sub(no_use_words,'',title)))
#     time.sleep(wait)         
    
##모든 영화 마무리.

print('fin')        