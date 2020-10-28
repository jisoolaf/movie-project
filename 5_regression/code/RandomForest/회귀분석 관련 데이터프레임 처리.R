setwd('C:/Users/3731h/Desktop')

# install.packages('UsingR')
library(UsingR)
library(dplyr)

#파일 불러오기
testdata<-read.csv('movie_regression.csv',header=T)


#필요한 컬럼만 불러오기

mydf<-subset(testdata,select = c())

mydf<-mydf%>%filter(!is.na(SHOW_TM)&!is.na(NATION_NM_NUM)&!is.na(COMPANY_NM_NUM)&!is.na(GENRE_NM_NUM)&!is.na(SP_LANG_NUM)&!is.na(BUDGET)&!is.na(NAVER_CMT_NN)&!is.na(NAVER_EX_PT)&!is.na(AUDI_ACC))

##개략적 파악
head(mydf)

summary(mydf$AUDI_ACC)

par(mfrow=c(1,1))
hist(mydf$AUDI_ACC)

#정규분포화

#로그변환
mydf<-transform(mydf,AUDI_ACC_log=log(AUDI_ACC+1))

hist(mydf$AUDI_ACC_log,freq=T)

#제곱근변환
mydf<-transform(mydf,AUDI_ACC_sqrt=sqrt(AUDI_ACC+1))

hist(mydf$AUDI_ACC_sqrt,freq=T)