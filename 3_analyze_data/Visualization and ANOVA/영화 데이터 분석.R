library(tidyverse) #데이터 분석을 위한 패키지
library(corrplot) #상관행렬그래프를 위한 패키지
library(ggthemes) #그래프 설정을 위한 패키지
library(viridis) #그래프에 어여쁜 색칠을 위한 패키지
library(VIM) # 결측치 시각화를 위한 패키지
library(lawstat) # 세 집단이상간 차이 분석을 위한 패키지




getwd()
movie <- read.csv('movie_analysis.csv', na.strings = c(''))
glimpse(movie)




movie$ORI_BOOK <- factor(movie$ORI_BOOK)
glimpse(movie)
table(movie$ORI_BOOK)
# ggplot(movie, aes(x=ORI_BOOK, y=AUDI_ACC, fill=ORI_BOOK)) + geom_boxplot() + scale_y_continuous(breaks=c(0,5000000,10000000,15000000), labels=c('없음','오백만명','천만명','천오백만명')) + theme_classic() + theme(legend.position = 'none') + labs(title='원작도서유무에 따른 관객수 비교', x='원작도서유무', y='관객수')
ggplot(filter(movie, !is.na(ORI_BOOK)), aes(x=ORI_BOOK, y=AUDI_ACC, fill=ORI_BOOK)) + stat_summary_bin(fun.y = median, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(25000,50000,75000,100000), labels=c('25000명','50000명','75000명','100000명')) + scale_x_discrete(breaks=c(0,1), labels=c('없음','있음')) + theme_classic() + labs(title='원작도서유무에 따른 관객수 중앙값', x='원작도서', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')



# glimpse(movie)
# sum(is.na(movie$AWARDS))
# table(movie$AWARDS)
# movie$AWARDS <- factor(movie$AWARDS)
# glimpse(movie)
# ggplot(movie, aes(x=AWARDS, y=AUDI_ACC, fill=AWARDS)) + geom_boxplot() + scale_y_continuous(breaks=c(0,5000000,10000000,15000000), labels=c('없음','오백만명','천만명','천오백만명')) + theme_classic() + theme(legend.position = 'none') + labs(title='수상여부에 따른 관객수 비교', x='수상여부', y='관객수')




sum(is.na(movie$SERIES))
table(movie$SERIES)
movie$SERIES <- factor(movie$SERIES)
glimpse(movie)
# ggplot(filter(movie, !is.na(SERIES)), aes(x=SERIES, y=AUDI_ACC, fill=SERIES)) + geom_boxplot() + scale_y_continuous(breaks=c(0,5000000,10000000,15000000), labels=c('없음','오백만명','천만명','천오백만명')) + theme_classic() + theme(legend.position = 'none') + labs(title='시리즈물여부에 따른 관객수 비교', x='시리즈물여부', y='관객수')
ggplot(filter(movie, !is.na(SERIES)), aes(x=SERIES, y=AUDI_ACC, fill=SERIES)) + stat_summary_bin(fun.y = median, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,200000,400000,600000), labels=c('0명','200000명','400000명','600000명')) + scale_x_discrete(breaks=c(0,1), labels=c('비시리즈','시리즈')) + theme_classic() + labs(title='시리즈작품여부에 따른 관객수 중앙값', x='시리즈작품여부', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')




glimpse(movie)
sum(is.na(movie$WATCH_GRADE_NM))
table(movie$WATCH_GRADE_NM)
ggplot(movie, aes(x=WATCH_GRADE_NM, y=AUDI_ACC, fill=WATCH_GRADE_NM)) + stat_summary_bin(fun.y = median, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,10000,20000), labels=c('0명','10000명','20000명')) + theme_classic() + labs(title='관람등급에 따른 관객수 중앙값', x='관람등급', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')




glimpse(movie)
sum(is.na(movie$SHOW_TM))
ggplot(movie,aes(x=SHOW_TM, y=AUDI_ACC, color=SHOW_TM)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('0명', '오백만명', '천만명', '천오백만명')) + scale_x_continuous(breaks=c(60,120,180,240), labels=c('1시간','2시간','3시간','4시간')) + theme_classic()  + labs(title='상영시간에 따른 관객수', x='상영시간', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$SHOW_TM, movie$AUDI_ACC, use='complete.obs')






glimpse(movie)
sum(is.na(movie$BUDGET))
ggplot(filter(movie, !is.na(BUDGET)),aes(x=BUDGET, y=AUDI_ACC, color=BUDGET)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('0명', '오백만명', '천만명', '천오백만명')) + scale_x_continuous(breaks=c(0,100000000,200000000,300000000,400000000, 500000000), labels=c('0','1억','2억','3억','4억','5억')) + theme_classic()  + labs(title='예산에 따른 관객수', x='예산(Dollar)', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$BUDGET, movie$AUDI_ACC, use='complete.obs')






glimpse(movie)
sum(is.na(movie$NAVER_CMT_NN))
ggplot(filter(movie, !is.na(NAVER_CMT_NN)),aes(x=NAVER_CMT_NN, y=AUDI_ACC, color=NAVER_CMT_NN)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000, 20000000), labels = c('0명', '오백만명', '천만명', '천오백만명', '이천만명')) + scale_x_continuous(breaks=c(0, 5000, 10000, 15000, 20000, 25000), labels=c('0건','5000건','10000건','15000건','20000건','25000건'))+ theme_classic()  + labs(title='개봉전 네이버 댓글수에 따른 관객수', x='네이버 댓글수', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$NAVER_CMT_NN, movie$AUDI_ACC, use='complete.obs')





glimpse(movie)
ggplot(filter(movie, !is.na(NAVER_PRE_EVAL)),aes(x=NAVER_PRE_EVAL, y=AUDI_ACC, color=NAVER_PRE_EVAL)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('0명', '오백만명', '천만명', '천오백만명')) + scale_x_continuous(breaks=c(0, 2.5, 5.0, 7.5, 10.0), labels=c('0점','2.5점','5점','7.5점','10점'))+ theme_classic() + labs(title='개봉전 네이버 평점에 따른 관객수', x='네이버 평점', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$NAVER_PRE_EVAL, movie$AUDI_ACC, use='complete.obs')





ggplot(filter(movie, !is.na(NAVER_PRE_EVAL_MUL)),aes(x=NAVER_PRE_EVAL_MUL, y=AUDI_ACC, color=NAVER_PRE_EVAL_MUL)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000, 20000000), labels = c('0명', '오백만명', '천만명', '천오백만명','이천만명'))+ theme_classic() + labs(title='개봉전 네이버 평점x네이버 댓글수에 따른 관객수', x='네이버 평점x네이버 댓글수', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$NAVER_PRE_EVAL_MUL, movie$AUDI_ACC, use='complete.obs')




glimpse(movie)
ggplot(filter(movie, !is.na(NAVER_EX_PT)),aes(x=NAVER_EX_PT, y=AUDI_ACC, color=NAVER_EX_PT)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('0명', '오백만명', '천만명', '천오백만명')) + theme_classic() + labs(title='개봉전 네이버 기대지수에 따른 관객수', x='기대지수', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
ggplot(filter(movie, !is.na(NAVER_EX_PT)),aes(x=log1p(NAVER_EX_PT), y=AUDI_ACC, color=log1p(NAVER_EX_PT))) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('0명', '오백만명', '천만명', '천오백만명')) + theme_classic() + labs(title='개봉전 네이버 기대지수(로그)에 따른 관객수', x='log(1+기대지수)', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$NAVER_EX_PT, movie$AUDI_ACC, use='complete.obs')





glimpse(movie)
corrplot.mixed(
  corr = cor(movie[c('AUDI_ACC','SHOW_TM', 'BUDGET', 'NAVER_CMT_NN', 'NAVER_PRE_EVAL', 'NAVER_PRE_EVAL_MUL','NAVER_EX_PT')], use = 'complete.obs'), 
  tl.col = "red",  
  upper = "ellipse", tl.pos = "lt", mar=c(0,0,0,0)) 




ggplot(movie, aes(x=AUDI_ACC)) + geom_histogram()
geom_histogram




glimpse(movie)
movie$OPEN_YEAR <- factor(movie$OPEN_YEAR)
movie$OPEN_MONTH <- factor(movie$OPEN_MONTH)
movie$OPEN_DAY <- factor(movie$OPEN_DAY)
movie$OPEN_WEEKDAY <- factor(movie$OPEN_WEEKDAY)
movie$OPEN_QUARTER <- factor(movie$OPEN_QUARTER)
movie$OPEN_WEEK <- factor(movie$OPEN_WEEK)



# summary(aov(AUDI_ACC~TITLE, data = movie))

# 데이터의 정규분포 여부 확인
shapiro.test(movie$AUDI_ACC)


#두 집단간 차이 분석
str(movie)
wilcox.test(AUDI_ACC~SERIES,data=movie)
glimpse(movie)
movie$AWARDS <- factor(movie$AWARDS)
wilcox.test(AUDI_ACC~AWARDS,data=movie)


#세 집단이상간 차이 분석
levene.test(movie$AUDI_ACC, movie$OPEN_YEAR, location='mean')
summary(aov(AUDI_ACC~OPEN_YEAR, data=movie))
kruskal.test(AUDI_ACC~NATION_NM_NUM, data=movie)






top20_actor <- movie %>% group_by(ACTOR1) %>% summarise(actor_n = n(), audi_median=median(AUDI_ACC), audi_mean=mean(AUDI_ACC)) %>% arrange(desc(actor_n)) %>% filter(!is.na(ACTOR1)) %>% head(20) 
ggplot(top20_actor, aes(x=ACTOR1,y=audi_median,fill=ACTOR1)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,1000000,2000000,3000000,4000000,5000000), labels=c('0','백만명','이백만명','삼백만명','사백만명','오백만명'))  + theme_classic() + labs(title='주인공출연빈도 top20배우의 관객수 중앙값', x='배우', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none', axis.text.x = element_text(angle=90))





glimpse(movie)
top10_company <- movie %>% group_by(COMPANY_NM) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC), audi_mean=mean(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(COMPANY_NM)) %>% head(10)
ggplot(top10_company, aes(x=COMPANY_NM,y=audi_median,fill=COMPANY_NM)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,200000,400000,600000,800000), labels=c('0','20만명','40만명','60만명','80만명'))  + theme_classic() + labs(title='빈도수 top10배급사의 관객수 중앙값', x='배급사', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none') + coord_flip()
top10_company




table(movie$PRI_GENRE_NM)
glimpse(movie)
movie %>% group_by(PRI_GENRE_NM) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC), audi_mean=mean(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(PRI_GENRE_NM)) %>% head(20)
ggplot(filter(movie, !is.na(PRI_GENRE_NM)), aes(x=PRI_GENRE_NM, y=log(AUDI_ACC), fill=PRI_GENRE_NM)) + stat_summary_bin(fun.y = mean, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + coord_flip() + theme_classic() + labs(title='장르에 따른 관객수(로그) 평균', x='장르', y='log(관객수) 평균') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')







top20_nation <- movie %>% group_by(NATION_NM) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC), audi_mean=mean(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(NATION_NM)) %>% head(20)
ggplot(top20_nation, aes(x=NATION_NM,y=audi_median,fill=NATION_NM)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0)  + coord_flip() + scale_y_continuous(breaks=c(0,20000,40000,60000), labels=c('0','2만명','4만명','6만명'))  + theme_classic() + labs(title='빈도수 top20제작국가의 관객수 중앙값', x='제작국가', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')




table(movie$SP_LANG_NUM)
top20_lang <- movie %>% group_by(SP_LANG) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC), audi_mean=mean(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(SP_LANG)) %>% head(20)
ggplot(top20_lang, aes(x=SP_LANG,y=audi_median,fill=SP_LANG)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + coord_flip() + scale_y_continuous(breaks=c(0,200000,400000), labels=c('0','20만명','40만명')) + theme_classic() + labs(title='top20사용언어에 따른 관객수 중앙값', x='사용언어', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')





glimpse(movie)
ggplot(filter(movie, !is.na(AWARDS)), aes(x=AWARDS, y=AUDI_ACC, fill=AWARDS)) + stat_summary_bin(fun.y = median, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,10000,20000), labels=c('0','만명','2만명')) + scale_x_discrete(breaks=c(0,1), labels=c('비수상','수상')) + theme_classic() + labs(title='개봉전 수상여부에 따른 관객수 중앙값', x='수상여부', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')




# Median VS Mean; 정규분포를 따르지 않을 때는 Median을 쓴다.
summary(train)
ggplot(train,aes(x=NAVER_EX_PT)) + geom_histogram()
ggplot(train,aes(x=NAVER_CMT_NN)) + geom_histogram()
ggplot(train,aes(x=SHOW_TM)) + geom_histogram()
shapiro.test(train$NAVER_EX_PT)
shapiro.test(train$NAVER_CMT_NN)
shapiro.test(train$SHOW_TM)



# 결측치 정보 확인
aggr(train, sortVars=T,prop=F, cex.axis=0.45, numbers=T)
aggr
glimpse(train)


