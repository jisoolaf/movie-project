import pandas as pd 
import nltk
from konlpy.tag import Okt
from wordcloud.wordcloud import WordCloud
import re

# data = pd.read_csv('C:/Users/user/Documents/github/movie.csv')
data = pd.read_csv('C:/Users/3731h/Documents/GitHub/project/movie.csv')

# data = data.iloc[0:2, :]

over_10mil=data.loc[data['AUDI_ACC']>=10000000]
over_mil=data.loc[data['AUDI_ACC']>=2200000]#100만 오류뜸 150만 오류 200오류 250 통과 225통과 212.5에러 215에러
# print(top10)

# print(data.columns)

# print(type(data['NAVER_CMT'].values))
    
# text = ' '.join([re.sub('\W',' ',str(oneCmt)) for oneCmt in data['NAVER_CMT'][0:2]])
text = ' '.join([re.sub('\W',' ',str(oneCmt)) for oneCmt in over_mil['NAVER_CMT']]) #전체
# print(text)

     
stop_words = ['은', '는', '이', '가', '을', '를', '에', '의', '과', '와', '둘', '등','저','내','그','것','점',
            '말','더','거','척','수','왜','때','볼','개','임','알','영화','정말','진짜','보고','완전','좀','뭐','요',
            '분','그냥','제','나','노','이건','천','또','우리','무조건','때문','안','이영화','역시','듯','정도','편',
            '이번','한번','함','번','꼭','지금','일단','이야기','중','언제','난','이상','날','만','이제','보기','걸','해',
            '모두','도','애','바로','가장']
   
def get_tags(text, ntags):
#     try : 
    spliter = Okt()
    nouns = spliter.nouns(text)
#         komoran = Komoran()
#         nouns = komoran.nouns(text)
#         nouns = [each_word for each_word in nouns if each_word not in stop_words ]
    newlist=list()
    for each_word in nouns:
        if each_word not in stop_words:
            newlist.append(each_word)
#         print(nouns[0])
    nouns = nltk.Text(newlist)
    wcData = nouns.vocab().most_common(ntags)
    wcDict = dict(wcData)
    return wcDict
#     except Exception as e:
#         print(e)
#         print(text)
#         break
    
     
     
     
wcInput = get_tags(text, 100)
     
# jpype._jexception.OutOfMemoryErrorPyRaisable: java.lang.OutOfMemoryError: Java heap space
# jpype._jexception.NullPointerExceptionPyRaisable: java.lang.NullPointerException
     
print(wcInput)
print(sorted(wcInput.items(), key=lambda x:x[1], reverse=True))
           
wordcloud = WordCloud(font_path='c:/Windows/fonts/malgun.ttf', 
                    relative_scaling=0.2, 
                    background_color='black').generate_from_frequencies(wcInput)
                                    
plt.figure(figsize=(30, 50))                    
plt.imshow(wordcloud)
plt.title('Top keyword')
plt.axis('off')
plt.show()
plt.savefig('cmtWordcloud.png', dpi=400, bbox_inches='tight')
# #          
# # print('finished')