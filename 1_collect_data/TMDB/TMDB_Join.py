import pandas as pd

### Kofic
KoficData = pd.read_csv('koapitotal.csv', error_bad_lines=False) 
print(KoficData.columns)
print('-'*50)

# KoficData['movieNm'] = KoficData['movieNm'].str.replace('[\W]+','')
# KoficData['movieNm'] = KoficData['movieNm'].str.lower()
# print(KoficData['movieNm'])

KoficData['﻿movieNm'] = KoficData['﻿movieNm'].str.replace(' ','') 
KoficData['﻿movieNm'] = KoficData['﻿movieNm'].str.replace('[\W]+','')
KoficData['﻿movieNm'] = KoficData['﻿movieNm'].str.lower()
 
KoficData['directorNmEn'] = KoficData['directorNmEn'].str.replace('[\W]+','')
KoficData['directorNmEn'] = KoficData['directorNmEn'].str.lower()
 
print(KoficData.head(10))
print('-'*50)
 
print(KoficData.info())
print('-'*50)
### Kofic
 
 
### TMDB 
TMDBData = pd.read_csv('TMDB_alltrue_rename.csv', error_bad_lines=False)
print(TMDBData.columns)
print('-'*50)
   
TMDBData.columns = ['﻿movieNm', 'movieNmEn', 'openDt', 'directorNmEn', 'budget', 'ori_lang', 'series', 'crewData', 'castData', 'keyWord']
    
TMDBData['openDt'] = TMDBData['openDt'].astype('object')
TMDBData['openDt'] = TMDBData['openDt'].replace(' 00:00:00', '')
TMDBData['openDt'] = TMDBData['openDt'].replace('-', '')
# print(TMDBData['openDt'])
# print('-'*50)
     
# TMDBData['movieNm'] = TMDBData['movieNm'].str.replace('[\W]+','')
# TMDBData['movieNm'] = TMDBData['movieNm'].str.lower()
# print(TMDBData['movieNm'])

TMDBData['﻿movieNm'] = TMDBData['﻿movieNm'].str.replace(' ','')      
TMDBData['﻿movieNm'] = TMDBData['﻿movieNm'].str.replace('[\W]+','')
TMDBData['﻿movieNm'] = TMDBData['﻿movieNm'].str.lower()
# print(TMDBData['movieNmEn'])
    
TMDBData['directorNmEn'] = TMDBData['directorNmEn'].str.lower()
TMDBData['directorNmEn'] = TMDBData['directorNmEn'].str.strip("[")
TMDBData['directorNmEn'] = TMDBData['directorNmEn'].str.strip("]")
TMDBData['directorNmEn'] = TMDBData['directorNmEn'].str.replace("'", "")
TMDBData['directorNmEn'] = TMDBData['directorNmEn'].str.split(',')
TMDBData['directorNmEn'] = TMDBData['directorNmEn'].str[0]
TMDBData['directorNmEn'] = TMDBData['directorNmEn'].str.replace('[\W]+','')
    
print( TMDBData['directorNmEn'] )
    
print(TMDBData.head(10))
print('-'*50)
# 
print(TMDBData.info())
print('-'*50)
# ### TMDB 
    
    
innerJoin = pd.merge(KoficData, TMDBData, on = ['﻿movieNm', 'directorNmEn'], how='inner', suffixes = ('Kofic', 'TMDB'), indicator=True)
# innerJoin = pd.merge(KoficData, TMDBData, on = ['﻿movieNm'], how='inner', suffixes = ('Kofic', 'TMDB'), indicator=True)
# print(innerJoin)
# print('-'*50)

print(len(innerJoin))
innerJoin = innerJoin.drop_duplicates()
print(len(innerJoin))

print(innerJoin.info())
print('-'*50)
innerJoin.to_csv('Kofic_TMDB_innerJoin_movie_director.csv', header=True, index = False, encoding='utf-8')
             
# print(innerJoin['_merge'].unique())
           
           
outerJoin = pd.merge(KoficData, TMDBData, on = ['﻿movieNm', 'directorNmEn'], how='outer', suffixes = ('Kofic', 'TMDB'), indicator=True)
# outerJoin = pd.merge(KoficData, TMDBData, on = ['﻿movieNm'], how='outer', suffixes = ('Kofic', 'TMDB'), indicator=True)
# print(outerJoin)
# print('-'*50)
           
notJoin = outerJoin[ outerJoin['_merge'] != 'both' ]
# print(notJoin['_merge'].unique())

print(len(notJoin))
innerJoin = innerJoin.drop_duplicates()
print(len(notJoin))

print(notJoin.info())
print('-'*50)
notJoin.to_csv('Kofic_TMDB_notJoin_movie_director.csv', header=True, index = False, encoding='utf-8')
             
# print(innerJoin['_merge'].unique())
           
          
          
print('finished')

