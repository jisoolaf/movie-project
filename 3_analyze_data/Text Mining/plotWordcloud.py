import pandas as pd 
import nltk
from konlpy.tag import Okt
from wordcloud.wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv('D:/myworkspace/github/movie.csv')
  
text = ' '.join([onePlot for onePlot in data['PLOT'].fillna(' ')])

stop_words = ['은', '는', '이', '가', '을', '를', '에', '의', '과', '와', '둘', '등',\
              '그', '저', '이것', '그것', '저것', '것', '곳', '때', '건',\
              '당신', '인간', '누구', '사람', '남자', '여자', '처', '이름', '우리', \
              '딸', '엄마', '아들', '아버지', '어머니', '아내', '아빠', '남편', '동생', '형',\
              '그녀', '여인', '소녀', '소년', '아이',\
              '나', '자신', '제', '내', '남', \
              '시작', '끝', '전', '후', '중', '지금', '과거', '사이', '마지막', \
              '앞', '뒤', '위', '속',\
              '다시', '처음', '첫', '이제', '이후', '또', '갑자기', '한편', '동안', '채', '매일', \
              '로', '로부터', '때문', '통해', '대한', '위해',\
              '과연', '마침내', '순간', '바로', '단',\
              '감독', '영화', '이야기', '작품', \
              '사실', '상황', '진짜', '일', '생활', '발견',\
              '못', '안',\
              '간다', '만난', '번', '다른', '모두', '모든', '낯선', \
              '가장', '최고', '점점', '더', '최대', '최강', \
              '구', '길', '날', '눈', '두', '세', '말', '개', '명', '향', \
              '살', '수', '알', '온', '하나', '손', '이자', '서로', '분',\
              '모습', '존재', '생각', '정체', '이상', '세계', '세상', '마음', '결심', \
              '계획', '몸', '관계', '발생', '가지', '이유', '음', '계속', '준비', '홀로', '혼자',\
              '한번', '도', '존', '놈', '거', '아무', '보고', '사상', '잠시', '상치', '의문', '자',\
              '줄', '마주', '현실', '더욱', '무엇', '그린', '찾기', '등장', '자리', '절대']

def get_tags(text, ntags):
    spliter = Okt()
    nouns = spliter.nouns(text)
    nouns = [each_word for each_word in nouns if each_word not in stop_words ]
    nouns = nltk.Text(nouns)
    wcData = nouns.vocab().most_common(ntags)
    wcDict = dict(wcData)
    return wcDict
  
wcInput = get_tags(text, 100)
print(sorted(wcInput.items(), key=lambda x:x[1], reverse=True))

wordcloud = WordCloud(font_path='c:/Windows/fonts/malgun.ttf', 
                      relative_scaling=0.2, 
                      background_color='black').generate_from_frequencies(wcInput)
                         
plt.figure(figsize=(30, 50))                    
plt.imshow(wordcloud)
plt.title('Top keyword')
plt.axis('off')
plt.show()
plt.savefig('D:/myworkspace/github/텍스트분석/plotWordcloud.png', dpi=400, bbox_inches='tight')
  
print('finished')