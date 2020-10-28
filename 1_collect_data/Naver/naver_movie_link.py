import os
import json
from pandas import DataFrame
import re

path='C:/myworkspace/MyPython/project1906/Naver_movie_json/'
filelists=os.listdir(path)
mylist=list() #사전이 있을경우 링크를 저장할 리스트
no_dict_list=list() #사전이 없을경우 영화제목을 저장할 리스트
for onestr in filelists:
    onejson=path+onestr
#     print(onejson)

    rfile=open(onejson,'rt',encoding='utf-8')
    rfile=rfile.read()
    result=json.loads(rfile) #전체 제이슨파일 내용
    # print(result)
    itemlist=result['items'] #전체 제이슨 중 items 내용 (사전을 갖고 있는 리스트 타입)
#     print(itemlist) 
    if len(itemlist)!=0:
        itemDict=itemlist.pop(0) #리스트에서 사전을 꺼냄
    # print(itemDict)
    # print(type(itemDict))
    
    # 제목 전환
        regExp='[<b>/]'   
        title=itemDict['title']
        title=re.sub(regExp,'',title)
        link=itemDict['link'] #해당 영화 링크
        mylist.append((title,link)) #제목 링크 저장
#         mylist.append(link) #링크만 저장
    # print(link)
    # print(type(link))
    
    else:
        no_dict_list.append(onestr)
# print(len(mylist))
# print(len(no_dict_list))


###
#리스트를 csv파일로 저장하기
myframe=DataFrame(mylist)
 
filename='링크모음.csv'
 
myframe.to_csv(filename,index=False,encoding='utf-8')
 
print(filename+'저장 완료되었습니다.')



##### 함수용 테스트
# def get_link_list(path):
#     filelists=os.listdir(path)
#     end=True    
#     
#     for onejson in filelists:
#         
#         onemovie=path + onejson
#         rfile=open(onemovie,'rt',encoding='utf-8')
#         rfile=rfile.read()
#         result=json.loads(rfile) #전체 제이슨파일 내용
#         end=False
#         try:
#             itemlist=result['items'] #전체 제이슨 중 items 내용 (사전을 갖고 있는 리스트 타입)    
#         
#             itemDict=itemlist.pop(0) #리스트에서 사전을 꺼냄
#            
#             link=itemDict['link'] #해당 영화 링크
#        
#             link_list=list() #link를 저장할 리스트    
#       
#             link_list.append(link)
# 
#         except Exception as e:
#             no_json_list=list()
#             print(e)
# #                 print('{}파일에서 오류 발생'.format(onejson))
#             no_json_list.append(onejson)
# #                 print(len(no_json_list))
#             end=True
#             
#     
#     if end==False:
# #           return no_json_list
#         return link_list
# 
# mypath='C:/myworkspace/MyPython/project1906/Naver_movie_json/'
# 
# mylist=get_link_list(mypath)
# print(mylist)

###테스트용
# mypath='C:/myworkspace/MyPython/project1906/Naver_movie_json/'
# filelists=os.listdir(mypath)
# print(type(filelists))
# print(filelists.index('박물관이 살아있다  비밀의 무덤.json'))
# print(filelists[:5])