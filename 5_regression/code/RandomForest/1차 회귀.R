#훈련 전 전처리
train <- read.csv('train_regression(1차).csv')
train$OPEN_MONTH <- factor(train$OPEN_MONTH)
train$OPEN_QUARTER <- factor(train$OPEN_QUARTER)
train$SERIES <- factor(train$SERIES)
train$ORI_BOOK <- factor(train$ORI_BOOK)
glimpse(train)
summary(train)
train <- mutate(train, NAVER_CMT_NN = log10(NAVER_CMT_NN+1), NAVER_EX_PT = log10(NAVER_EX_PT+1), AUDI_ACC = log10(AUDI_ACC))

#학습용 데이터와 검증용 데이터 분리
sample <- sample.split(train$AUDI_ACC,SplitRatio = 0.80)
real_train <- subset(train, sample==T)
test <- subset(train, sample==F)


#랜덤포레스트를 이용한 영화데이터 기계학습(선형회귀)
set.seed(222)
model <- randomForest(AUDI_ACC ~ .,data = real_train, ntree = 501, replace = TRUE, nodesize = 9,importance = TRUE)




#변수중요도와 노드불순도확인
imp <- importance(model)
fraimp <- as.data.frame(imp)
fraimp$var <- row.names(fraimp)
ggplot(fraimp,aes(x=var)) + geom_line(aes(y=`%IncMSE`*10,group=1, col='%IncMSE'), size=2) + geom_line(aes(y=IncNodePurity,group=1, col='IncNodePurity'), size=2) + scale_y_continuous(sec.axis = sec_axis(~./10, name = "%IncMSE")) + theme_classic() + guides(color=guide_legend(title="변수 중요도")) + theme(legend.title.align = 0.5, plot.title=element_text(hjust=0.5, face='bold')) + scale_x_discrete(breaks=c('NATION_NM','NAVER_CMT_NN','NAVER_EX_PT','OPEN_MONTH','OPEN_QUARTER','ORI_BOOK','PRI_GENRE_NM','SERIES','SHOW_TM','TOP_COMPANY_NM','WATCH_GRADE_NM'), labels=c('제작국가','댓글개수','기대지수','개봉월','개봉분기','원작도서','장르','시리즈','상영시간','배급사','관람등급')) + labs(title='1차회귀결과 변수중요도', x='변수명', y='IncNodePurity')



#검증용데이터로 예측
pred <- predict(model, test[-12])
test$AUDI_ACC_PRED <- pred
test <- test[-13]
test <- mutate(test, AUDI_ACC = 10^AUDI_ACC, AUDI_ACC_PRED = 10^pred)
write.csv(test,'prediction(1차).csv',row.names = F, fileEncoding = 'cp949')
