import numpy as np
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import re

no_use_words='[^a-zA-Z0-9가-힣]'

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
myfile='네이버 크롤링 추가작업할 목록_190628.csv'
 
df=pd.read_csv(myfile,encoding='cp949')
# print(df['링크'][0])

mycolumn=['영화명','감독','개봉전 평점','총댓글수(개봉전)','댓글모음']

title_col=df['영화명']
director_col=df['감독']
link_col=df['링크']
    
title_list=title_col.values.flatten().tolist()  #영화명 리스트
director_list=director_col.values.flatten().tolist()    #감독 리스트
result=link_col.values    #ndarray 타입
result=result.tolist() #link 리스트

# print(result[:10])

###전체 개봉전 덧글 및 총 덧글갯수, 평점 구하기
##각 영화별로 실행하기
# idx=3896
wait=0.125

complete_df=pd.DataFrame()
error_list=list()

for idx in range(len(result)): #영화갯수만큼 반복
    datalist=list() # 각 행을 저장할 리스트
    title=title_list[idx]
    director=director_list[idx]
    
    try:
        total_reply=get_totalNo_reply(result[idx]) #영화 별 전체댓글수
        before_score=get_before_score(result[idx])#영화 별 개봉전 총평점
        total_page=get_total_page(result[idx]) #우선 전체 댓글 페이지수를 구한다.
        mylink=result[idx].replace('basic','pointWriteFormList')+'&type=before&page={}'
     
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
      
        all_reply=np.array(save_Reply) #전체 댓글 모음
        all_reply_=''
        for reply in all_reply:
            all_reply_ +=str(reply)
        all_reply=all_reply_ #전체댓글
         
        #데이터 리스트에 정보 추가
        
        datalist.append(title) #영화명
        datalist.append(director) #감독
        datalist.append(before_score) #'개봉전 평점'
        datalist.append(total_reply)#,'총댓글수(개봉전)' 
        datalist.append(all_reply)#'댓글모음'
        
        result_frame=pd.DataFrame(np.reshape(np.array(datalist),(1,5)),index=None,columns=mycolumn)
                 
        complete_df=pd.concat([complete_df,result_frame])
        
        print(title+'저장 완료')
    
    except Exception as e:
        print(e)
        error_list.append((e,title))
         
    time.sleep(wait)         

complete_df.to_csv('네이버크롤링 추가작업 _190628.csv',index=None,encoding='utf-8')
print('csv 파일 저장 완료')
print(error_list)
# print(complete_df)

##모든 영화 마무리.

print('fin')        