import pandas as pd
import datetime
import re

df1 = pd.read_csv('영진위최종(4262개).csv', encoding='utf-8')
df2 = pd.read_csv('allcolumn.csv')

df1.ix[:,1] = df1.ix[:,1].astype(str)
type(df1.ix[1,1])
df1.ix[:,1] = df1.ix[:,1].str[0:4] + '-' + df1.ix[:,1].str[4:6] + '-' + df1.ix[:,1].str[6:8]
imsi = df1.ix[:, [0,1,9]]
imsi.columns = ['MOVIE_NM', 'OPEN_DT', 'ACTOR_NM']
imsi.to_csv('OPENDT변경.csv')

imsi.fillna('')

imsi['ACTOR1'] = imsi['ACTOR_NM'].str.strip('[]')
imsi['ACTOR1'] = imsi['ACTOR1'].str.split(',')
imsi['ACTOR2'] = imsi['ACTOR1'].str[2]
imsi['ACTOR2'] = imsi['ACTOR2'].str.strip("'")
imsi['ACTOR2'] = imsi['ACTOR2'].str[3:]
imsi['ACTOR1'] = imsi['ACTOR1'].str[0]
imsi['ACTOR1'] = imsi['ACTOR1'].str.strip("'")
imsi['ACTOR1'] = imsi['ACTOR1'].str[2:]

actor = pd.merge(df2, imsi, on=['MOVIE_NM', 'OPEN_DT'])
actor.to_csv('movieactor.csv', encoding= 'utf-8')
print('파일이 저장됨')