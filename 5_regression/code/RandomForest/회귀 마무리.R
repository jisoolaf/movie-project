# install.packages('randomForest')
# install.packages('caret')
library(randomForest)
library(caret)

setwd('C:/Users/3731h/Desktop')

#파일 불러오기
traindata<-read.csv('train_regression_hwook.csv',header=T)

head(traindata)

str(traindata)

# #달,분기 factor변수로 변환
# traindata<-transform(traindata,OPEN_MONTH=as.factor(OPEN_MONTH))
# 
# traindata<-transform(traindata,OPEN_QUARTER=as.factor(OPEN_QUARTER))

str(traindata)

plot(traindata)

#RandomForest 모형 만들기
rf.fit<-randomForest(AUDI_ACC~OPEN_MONTH+OPEN_QUARTER+SHOW_TM+NATION_NM+TOP_COMPANY_NM+PRI_GENRE_NM+WATCH_GRADE_NM+SERIES+NAVER_CMT_NN+NAVER_EX_PT+ORI_BOOK,data=traindata,mtry=floor(11/3),ntree=500,nodesize=12,importance=T)

rf.fit
