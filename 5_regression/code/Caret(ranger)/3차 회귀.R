library(caret) #여러가지 예측 모델을 제공해주는 패키지


#훈련데이터 loading
newdata <- read.csv('train_regression(최종).csv',na.strings=c(''))
glimpse(newdata)



#결측치 처리
aggr(newdata, sortVars=T,prop=F, cex.axis=0.45, numbers=T)
newdata$SERIES[is.na(newdata$SERIES)] <- 0
newdata <- na.omit(newdata)
aggr(newdata, sortVars=T,prop=F, cex.axis=0.45, numbers=T)


#범주형 변수로 변경
glimpse(newdata)
newdata$OPEN_WEEK <- factor(newdata$OPEN_WEEK)
newdata$SERIES <- factor(newdata$SERIES)
newdata$ORI_BOOK <- factor(newdata$ORI_BOOK)
glimpse(newdata)


#최소값과 최대값의 차이가 큰 변수들에 로그를 씌워서 편차를 줄인다.
summary(newdata)
newdata <- mutate(newdata, NAVER_CMT_NN = log10(NAVER_CMT_NN+1), NAVER_EX_PT = log10(NAVER_EX_PT+1), AUDI_ACC = log10(AUDI_ACC))
summary(newdata)



#필요한 변수 추출
glimpse(newdata)
fitdata <- newdata[c('TOP_DIRECTOR','OPEN_WEEK', 'SHOW_TM', 'NATION_NM', 'COMPANY_NM', 'PRI_GENRE_NM', 'WATCH_GRADE_NM','TOP_ACTOR', 'SERIES', 'NAVER_CMT_NN', 'NAVER_EX_PT', 'AUDI_ACC')]



#예측모델 'ranger'를 이용한 영화데이터 기계학습(선형회귀)
glimpse(fitdata)
set.seed(10)
rfcr.fit <- train(AUDI_ACC~., data=fitdata, method='ranger')
rfcr.fit

#예측영화 loading
test <- read.csv('test(최종).csv', na.strings=c(''))



#필요한 컬럼 추출
glimpse(test)
names(fitdata)
test <- test[-c(1,3,4,5,16)]


#결측치 처리
test <- na.omit(test)
aggr(test, sortVars=T,prop=F, cex.axis=0.45, numbers=T)



#factor타입 동일조건 설정
glimpse(test)
glimpse(fitdata)
test$AUDI_ACC <- NA
imsi <- rbind(fitdata,test)
test <- imsi[4188:4197,]
glimpse(test)
test <- test[-12]
glimpse(test)
test$OPEN_WEEK
test$TOP_ACTOR
summary(test)


#예측데이터 정규화
test <- mutate(test, NAVER_CMT_NN = log10(NAVER_CMT_NN+1), NAVER_EX_PT = log10(NAVER_EX_PT+1))
summary(test)


#관객수 예측
y_pred <- predict(rfcr.fit,test)
test$AUDI_ACC_PRED <- y_pred
test
test <- mutate(test, AUDI_ACC_PRED=10^(AUDI_ACC_PRED))
test
test$AUDI_ACC_PRED <- floor(test$AUDI_ACC_PRED)
test
write.csv(test,'prediction(3차).csv',row.names = F, fileEncoding = 'cp949')

