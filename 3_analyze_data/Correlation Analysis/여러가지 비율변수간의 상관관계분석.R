setwd('C:/Users/3731h/Desktop')

library(dplyr)

par(mfrow=c(1,1))

#파일 불러오기
testdata<-read.csv('분석용 데이터 프레임.csv',header=T)


#케이스 6
#전체 묶어서 해보기
mydf<-subset(testdata,select = c(SHOW_TM,BUDGET,NAVER_CMT_NN,NAVER_PRE_EVAL,NAVER_EX_PT,AUDI_ACC))

mydf

mydf<-mydf%>%filter(!is.na(SHOW_TM) & !is.na(BUDGET)& !is.na(NAVER_CMT_NN)& !is.na(NAVER_PRE_EVAL)& !is.na(NAVER_EX_PT)& !is.na(AUDI_ACC))

mydf

result<-cor(mydf)

#시각화
# install.packages('corrplot')
library(corrplot)

# 그래프 그려보기
corrplot(result)
corrplot(result,method='ellipse',addCoef.col='red')

library(corrgram)
corrgram(result,lower.panel = panel.conf)

plot(mydf)
