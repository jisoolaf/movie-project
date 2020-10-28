import pandas as pd
import re
from konlpy.tag import Okt 

data = pd.read_csv('C:/Users/user/Documents/github/movie.csv', encoding='utf-8')
data = data[['TITLE', 'OPEN_DT', 'NAVER_CMT', 'NAVER_PRE_EVAL', 'AUDI_ACC']]
data = data.dropna()

# data = data[60:65]
# print(data)
# print(type(data))

# data = data[0:2]
  
data['NAVER_CMT'] = data['NAVER_CMT'].apply(lambda x : re.sub('[^0-9a-zA-Zㄱ-힗 ]', '', str(x)))
# print(cmt.head())
# print('-'*50)





   
okt = Okt()
def tokenizer_okt_nouns(doc):
    return okt.nouns(doc)
 
data['TOKEN_CMT'] = data['NAVER_CMT'].apply(tokenizer_okt_nouns)
# print(data['TOKEN_CMT'].iloc[0])
# print(data.head())
# print(sentDict.keys())

# stop_words = ['은', '는', '이', '가', '을', '를', '에', '의', '과', '와', '둘', '등', '때', '로', '한', '그']

# data['TOKEN_CMT'] = [each_word for each_word in data['TOKEN_CMT'] if each_word not in stop_words]




table = dict() 
polarity = pd.read_csv('C:/Users/user/Documents/github/텍스트분석/polarity.csv')

# print(polarity.head())

# n gram Negative, Neutrual, Positive 
for idx in range(len(polarity)): 
#     print(polarity.iloc[idx]['﻿ngram'])
    line = polarity.iloc[idx]
    for word in line['﻿ngram'].split(';'):
        key = ''
        key += word.split('/')[0] 
        if key in table.keys() :
            table[key] = {'Neg': table[key]['Neg'] + line['NEG'], 'Neut': table[key]['Neut'] + line['NEUT'], 'Pos': table[key]['Pos'] + line['POS']} 
        else : 
            table[key] = {'Neg': line['NEG'], 'Neut': line['NEUT'], 'Pos': line['POS']} 
                  
# print(table['영화'])
# print(type(table))

total_list = []

for token in data['TOKEN_CMT']:
    if token != '':
        total = 0
        wordcnt = 0
        for word in token:           
            if word in table.keys(): 
#                 print(word)
                negative = float( table[word]['Neg'] )
                neutral = float( table[word]['Neut'] )
                positive = float( table[word]['Pos'] )
                
                if positive > negative and positive > neutral :
                    total += 1
#                     print('긍정') 
                elif negative > positive and negative > neutral :
                    total += (-1)
#                     print('부정') 
    #             else :
    #                 print('중립')
                wordcnt += 1
#         print(total)
#         print(wordcnt) 
        
        if wordcnt > 0:
            total = total / wordcnt
        else : 
            total = ''
#         print(total)
    else :
        total = ''
        
    total_list.append(total)  
    
print(total_list)
print('-'*50)    

data['CMT_SCORE'] = total_list 

print(data.head())
print('-'*50)

data = data[['TITLE', 'OPEN_DT', 'NAVER_CMT', 'NAVER_PRE_EVAL', 'AUDI_ACC']]

data.to_csv('cmtScore_audiAcc.csv', header=True, index = False, encoding='cp949')  


print('finished')

