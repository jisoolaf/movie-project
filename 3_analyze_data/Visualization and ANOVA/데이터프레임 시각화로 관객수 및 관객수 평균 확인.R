data <- read.csv('movie_regression.csv')
data[1:2,]
str(data)
summary(data)

install.packages('ggplot2')
library(ggplot2)

install.packages('rpart')
library(rpart)

install.packages('forcats')
library(forcats) # fct_lump함수를 이용하여 주요한 n개를 제외하고 다른 값들은 기타로 지정한다.

data$OPEN_YEAR <- as.factor(data$OPEN_YEAR)
data$OPEN_MONTH <- as.factor(data$OPEN_MONTH)
data$OPEN_DAY <- as.factor(data$OPEN_DAY)
data$OPEN_WEEKDAY <- as.factor(data$OPEN_WEEKDAY)
data$OPEN_QUARTER <- as.factor(data$OPEN_QUARTER)
data$OPEN_WEEK <- as.factor(data$OPEN_WEEK)
data$ORI_BOOK <- as.factor(data$ORI_BOOK)
data$AWARDS <- as.factor(data$AWARDS)
data$SERIES <- as.factor(data$SERIES)

str(data)


label_ko_num = function(num) {
  ko_num = function(x) {
    new_num = x %/% 10000
    return(paste(new_num, '만명', sep = ''))
  }
  return(sapply(num, ko_num))
}

ggplot(data, aes(OPEN_MONTH, AUDI_ACC, fill=OPEN_MONTH)) + geom_bar(stat="identity") + scale_y_continuous(labels = label_ko_num) + labs(x='개봉월', y='관객수', fill="개봉월") 

ggplot(data, aes(OPEN_YEAR, AUDI_ACC, fill=OPEN_YEAR)) + geom_bar(stat="identity") + scale_y_continuous(labels = label_ko_num) + labs(x='개봉연도', y='관객수', fill="개봉연도") 


audience <- aggregate(AUDI_ACC~ORI_BOOK,data,mean)
ggplot(audience, aes(ORI_BOOK, AUDI_ACC, fill=ORI_BOOK)) + geom_bar(stat="identity") + scale_y_continuous(labels = label_ko_num) + labs(x='원작도서유무', y='관객수 평균', fill="원작도서유무") 

aud <- aggregate(AUDI_ACC~NAVER_EX_PT,data,mean)
ggplot(aud, aes(NAVER_EX_PT, AUDI_ACC, fill=NAVER_EX_PT)) + geom_point(aes(color=NAVER_EX_PT)) + scale_y_continuous(labels = label_ko_num) + labs(x='네이버기대지수', y='관객수 평균') + geom_smooth(method="lm", se=FALSE)

aud1 <- aggregate(AUDI_ACC~SERIES,data,mean)
ggplot(aud1, aes(SERIES, AUDI_ACC, fill=SERIES)) + geom_bar(stat="identity") + scale_y_continuous(labels = label_ko_num) + labs(x='속편유무', y='관객수 평균', fill="속편유무") 

audience3 <- aggregate(AUDI_ACC~WATCH_GRADE_NM,data,mean)
ggplot(audience3,aes(x=WATCH_GRADE_NM,y=AUDI_ACC,fill=WATCH_GRADE_NM)) + geom_bar(stat="identity",position="dodge") + labs(x='관람등급', y='관객수 평균', fill="관람등급") + scale_y_continuous(labels = label_ko_num)

audience4 <- aggregate(AUDI_ACC~SHOW_TM,data,mean)
ggplot(audience4,aes(x=SHOW_TM,y=AUDI_ACC,fill=SHOW_TM)) + geom_bar(stat="identity",position="dodge")  + labs(x='상영시간', y='관객수',fill="상영시간") + scale_y_continuous(labels = label_ko_num)

rating1 <- aggregate(NAVER_PRE_EVAL~OPEN_MONTH,data,median) 
ggplot(rating1,aes(OPEN_MONTH,exp(NAVER_PRE_EVAL),fill=OPEN_MONTH)) + geom_bar(position="dodge",stat="identity") + theme(axis.text.x=element_text(angle=90, hjust=1)) + labs(x='개봉월', y='네이버평점수치화') + coord_flip()

rating3 <- aggregate(NAVER_PRE_EVAL~WATCH_GRADE_NM,data,mean) 
ggplot(rating3,aes(WATCH_GRADE_NM,exp(NAVER_PRE_EVAL),fill=WATCH_GRADE_NM)) + geom_bar(position="dodge",stat="identity") + labs(x='관람등급', y='네이버평점수치화')


png(filename='D:/Rclick/속편유무에 따른 관객수 평균 .png', height=500, width=500, bg='white')
dev.off()

