library(MASS) 
library(randomForest) 
library(caret)

newdata <- read.csv('C:/Users/user/Documents/github/train_regression(2차).csv')
tail(newdata, 100)
names(newdata)
summary(newdata)
str(newdata)

newdata$SERIES[is.na(newdata$SERIES)] <- 0
newdata$OPEN_WEEK <- as.factor(newdata$OPEN_WEEK)
newdata$SERIES <- as.factor(newdata$SERIES)

newdata['AUDI_ACC'] <- log( newdata['AUDI_ACC'] )
newdata['NAVER_CMT_NN'] <- log( newdata['NAVER_CMT_NN'] )
newdata['NAVER_EX_PT'] <- log( newdata['NAVER_EX_PT'] )
# newdata['OPEN_WEEK'] <- log( newdata['OPEN_WEEK'] )
# newdata['SHOW_TM'] <- log( newdata['SHOW_TM'] )

newdata$AUDI_ACC[is.infinite(newdata$AUDI_ACC)] <- 0
newdata$NAVER_CMT_NN[is.infinite(newdata$NAVER_CMT_NN)] <- 0
newdata$NAVER_EX_PT[is.infinite(newdata$NAVER_EX_PT)] <- 0
# newdata$OPEN_WEEK[is.infinite(newdata$OPEN_WEEK)] <- 0
# newdata$SHOW_TM[is.infinite(newdata$v)] <- 0

set.seed(10)


fitdata = newdata[c('OPEN_WEEK', 'SHOW_TM', 'NATION_NM', 'COMPANY_NM', 'PRI_GENRE_NM', 'WATCH_GRADE_NM', 'SERIES', 'NAVER_CMT_NN', 'NAVER_EX_PT', 'AUDI_ACC')]

dim(fitdata)

fitdata <- na.omit(fitdata)

dim(fitdata)

names(fitdata)

# rfcr.fit <- train(AUDI_ACC~., data=fitdata, method='rf')
rfcr.fit <- train(AUDI_ACC~., data=fitdata, method='ranger')



test_x <- fitdata[c('OPEN_WEEK', 'SHOW_TM', 'NATION_NM', 'COMPANY_NM', 'PRI_GENRE_NM', 'WATCH_GRADE_NM', 'SERIES', 'NAVER_CMT_NN', 'NAVER_EX_PT')]

test_y = fitdata$AUDI_ACC

y_pred = predict(rfcr.fit, test_x)

cbind(exp(test_y), exp(y_pred))
cbind(test_y, y_pred)

head( fitdata )

result <- cbind(fitdata, y_pred, exp(test_y), exp(y_pred)) 

write.csv(result, 'C:/Users/user/Documents/github/영화 예측 관련/caretResult_김지수/caretResult.csv', row.names=F, quote=F, fileEncoding='UTF-8')

summary(rfcr.fit)

capture.output(rfcr.fit, file = 'C:/Users/user/Documents/github/영화 예측 관련/caretResult_김지수/rfcr.fit.txt', append=TRUE)

capture.output(summary(rfcr.fit), file = 'C:/Users/user/Documents/github/영화 예측 관련/caretResult_김지수/summary_rfcr.fit.txt', append=TRUE)




################예측



test <- read.csv('C:/Users/user/Documents/github/영화 예측 관련/test.csv')
names(test)

testdata <- test[c('OPEN_WEEK', 'SHOW_TM', 'NATION_NM', 'COMPANY_NM', 'PRI_GENRE_NM', 'WATCH_GRADE_NM', 'SERIES', 'NAVER_CMT_NN', 'NAVER_EX_PT')]
tail(testdata)
names(testdata)
summary(testdata)
str(testdata)

testdata$AUDI_ACC <- NA

names(fitdata)
names(testdata)

imsi <- rbind(fitdata, testdata)

dim(imsi)
tail(imsi, 25)

testdata <- imsi[4189:4208,]

dim(testdata)
str(testdata)

testdata['NAVER_CMT_NN'] <- log( testdata['NAVER_CMT_NN'] )
testdata['NAVER_EX_PT'] <- log( testdata['NAVER_EX_PT'] )
# testdata['OPEN_WEEK'] <- log( testdata['OPEN_WEEK'] )
# testdata['SHOW_TM'] <- log( testdata['SHOW_TM'] )

testdata$NAVER_CMT_NN[is.infinite(testdata$NAVER_CMT_NN)] <- 0
testdata$NAVER_EX_PT[is.infinite(testdata$NAVER_EX_PT)] <- 0
# testdata$OPEN_WEEK[is.infinite(testdata$OPEN_WEEK)] <- 0
# testdata$SHOW_TM[is.infinite(testdata$v)] <- 0

set.seed(10)

testdata <- testdata[c('OPEN_WEEK', 'SHOW_TM', 'NATION_NM', 'COMPANY_NM', 'PRI_GENRE_NM', 'WATCH_GRADE_NM', 'SERIES', 'NAVER_CMT_NN', 'NAVER_EX_PT')]

dim(testdata)
names(testdata)

y_pred_test = predict(rfcr.fit, testdata)

result <- cbind(test, y_pred_test, exp(y_pred_test))

write.csv(result, 'C:/Users/user/Documents/github/영화 예측 관련/caretResult_김지수/caret_predict.csv', row.names=F, quote=F, fileEncoding='UTF-8')
