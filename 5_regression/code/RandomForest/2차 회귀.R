train <- read.csv('train_regression(2차).csv',na.strings = c(''))
glimpse(train)

#사용하지 않는 변수 제거
real_train <- train[-3]


#범주형 변수로 변경
glimpse(real_train)
real_train$OPEN_MONTH <- factor(real_train$OPEN_MONTH)
real_train$OPEN_QUARTER <- factor(real_train$OPEN_QUARTER)
real_train$SERIES <- factor(real_train$SERIES)
real_train$ORI_BOOK <- factor(real_train$ORI_BOOK)
glimpse(real_train)



#결측치 처리
aggr(real_train, sortVars=T,prop=F, cex.axis=0.45, numbers=T)
real_train$SERIES[is.na(real_train$SERIES)] <- 0
real_train <- na.omit(real_train)
aggr(real_train, sortVars=T,prop=F, cex.axis=0.45, numbers=T)
glimpse(real_train)
summary(real_train)


#최소값과 최대값의 차이가 큰 변수들에 로그를 씌워서 편차를 줄인다.
real_train <- mutate(real_train, NAVER_CMT_NN = log10(NAVER_CMT_NN+1), NAVER_EX_PT = log10(NAVER_EX_PT+1), AUDI_ACC = log10(AUDI_ACC))
summary(real_train)




#랜덤포레스트를 이용한 영화데이터 기계학습(선형회귀)
set.seed(222)
model <- randomForest(AUDI_ACC ~ .,data = real_train, ntree = 501, replace = TRUE, nodesize = 9,importance = TRUE)
model


#변수 중요도 확인 
imp <- importance(model)
fraimp <- as.data.frame(imp)
fraimp$var <- row.names(fraimp)
ggplot(fraimp,aes(x=var)) + geom_line(aes(y=`%IncMSE`*10,group=1, col='%IncMSE'), size=2) + geom_line(aes(y=IncNodePurity,group=1, col='IncNodePurity'), size=2) + scale_y_continuous(sec.axis = sec_axis(~./10, name = "%IncMSE")) + theme_classic() + guides(color=guide_legend(title="변수 중요도")) + theme(legend.title.align = 0.5, plot.title=element_text(hjust=0.5, face='bold')) + scale_x_discrete(breaks=c('COMPANY_NM','NATION_NM','NAVER_CMT_NN','NAVER_EX_PT','OPEN_MONTH','OPEN_QUARTER','ORI_BOOK','PRI_GENRE_NM','SERIES','SHOW_TM','WATCH_GRADE_NM'), labels=c('배급사','제작국가','댓글개수','기대지수','개봉월','개봉분기','원작도서','장르','시리즈','상영시간','관람등급')) + labs(title='2차회귀결과 변수중요도', x='변수명', y='IncNodePurity')


#예측영화 로딩
test <- read.csv('test.csv',na.strings = c(''))

#필요한 컬럼 추출 
glimpse(test)
test <- test[-c(1,2)]
test <- test[-3]
glimpse(test)


#factor타입 동일조건 설정
test$AUDI_ACC <- NA
test
imsi <- rbind(real_train,test)
glimpse(imsi)
test <- imsi[4188:4207,]
glimpse(test)
test <- test[-12]
glimpse(test)
real_train$PRI_GENRE_NM
test$PRI_GENRE_NM


#예측데이터 정규화
test <- mutate(test, NAVER_CMT_NN = log10(NAVER_CMT_NN+1), NAVER_EX_PT = log10(NAVER_EX_PT+1))
summary(test)

#관객수 예측
y_pred <- predict(model,test)
test$AUDI_ACC_PRED <- y_pred
test <- mutate(test, AUDI_ACC_PRED=10^(AUDI_ACC_PRED))
test
test$AUDI_ACC_PRED <- floor(test$AUDI_ACC_PRED)
write.csv(test,'prediction(2차).csv',row.names = F, fileEncoding = 'cp949')
