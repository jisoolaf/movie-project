setwd('C:/Users/3731h/Desktop')

library(dplyr)

par(mfrow=c(1,1))

#파일 불러오기
testdata<-read.csv('movie_regression.csv',header=T)



#필요한 컬럼만 불러오기
mydf<-subset(testdata,select = c(NATION_NM_NUM,COMPANY_NM_NUM,GENRE_NM_NUM,SP_LANG_NUM,AUDI_ACC))

head(mydf)

mydf<-mydf%>%filter(!is.na(NATION_NM_NUM) & !is.na(COMPANY_NM_NUM)& !is.na(GENRE_NM_NUM)& !is.na(SP_LANG_NUM)& !is.na(AUDI_ACC))

#제작국가 갯수로 그룹 나누기
unique(mydf$NATION_NM_NUM) #1~6

group1<-subset(mydf,NATION_NM_NUM==1)


group2<-subset(mydf,NATION_NM_NUM==2)
group3<-subset(mydf,NATION_NM_NUM==3)
group4<-subset(mydf,NATION_NM_NUM==4)
group5<-subset(mydf,NATION_NM_NUM==5)
group6<-subset(mydf,NATION_NM_NUM==6)


group1<-group1$AUDI_ACC
group2<-group2$AUDI_ACC
group3<-group3$AUDI_ACC
group4<-group4$AUDI_ACC
group5<-group5$AUDI_ACC
group6<-group6$AUDI_ACC

#
str(group1)


y1<-as.factor(group1)
y2<-as.factor(group2)
y3<-as.factor(group3)
y4<-as.factor(group4)
y5<-as.factor(group5)
y6<-as.factor(group6)


#전국관객수를 넣어야 하는가? 일단 제외하고 시작

y<-as.numeric(c(y1,y2,y3,y4,y5,y6))

#check each row length
#

length(group1) #1934 행
length(group2) #170
length(group3) #54
length(group4) #18
length(group5) #10
length(group6) #2

#grouping
n<- c(1934,170,54,18,10,2)


group<-rep(1:6,n)
group

length(y)
length(group)

#combining into data.frame
group_df<-data.frame(y,group)
group_df

#check type
sapply(group_df,class) #int int

group_df<-transform(group_df,group=factor(group))

sapply(group_df,class)

#시각화
attach(group_df)

boxplot(y~group,
        main='Boxplot of 전국관객수 by 제작국가 갯수',
        xlab='Factor Levels:제작국가 갯수 1/2/3/4/5/6',
        ylab='전국관객수')

#summary
tapply(y,group,summary)

detach(group_df)

#one-way ANOVA
aov(y~group, data=group_df)

summary(aov(y~group, data=group_df))

#Bartlett test
bartlett.test(y~group, data=group_df)
