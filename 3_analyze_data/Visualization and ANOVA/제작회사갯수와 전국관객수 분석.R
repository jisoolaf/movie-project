setwd('C:/Users/3731h/Desktop')

library(dplyr)

par(mfrow=c(1,1))

#파일 불러오기
testdata<-read.csv('movie_regression.csv',header=T)



#필요한 컬럼만 불러오기
mydf<-subset(testdata,select = c(NATION_NM_NUM,COMPANY_NM_NUM,GENRE_NM_NUM,SP_LANG_NUM,AUDI_ACC))

head(mydf)

mydf<-mydf%>%filter(!is.na(NATION_NM_NUM) & !is.na(COMPANY_NM_NUM)& !is.na(GENRE_NM_NUM)& !is.na(SP_LANG_NUM)& !is.na(AUDI_ACC))

#회사 갯수로 그룹 나누기
unique(mydf$COMPANY_NM_NUM) #1~3

group1<-subset(mydf,COMPANY_NM_NUM==1)
group2<-subset(mydf,COMPANY_NM_NUM==2)
group3<-subset(mydf,COMPANY_NM_NUM==3)


group1<-group1$AUDI_ACC
group2<-group2$AUDI_ACC
group3<-group3$AUDI_ACC

#
str(group1)


y1<-as.factor(group1)
y2<-as.factor(group2)
y3<-as.factor(group3)


#타입맞추기

y<-as.numeric(c(y1,y2,y3))

#check each row length
#

length(group1) #2013 행
length(group2) #170
length(group3) #5

#grouping
n<- c(2013,170,5)


group<-rep(1:3,n)
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
        main='Boxplot of 전국관객수 by 제작회사 갯수',
        xlab='Factor Levels:제작회사 갯수 1/2/3',
        ylab='전국관객수')

#summary
tapply(y,group,summary)

detach(group_df)

#one-way ANOVA
aov(y~group, data=group_df)

summary(aov(y~group, data=group_df))

#Bartlett test
bartlett.test(y~group, data=group_df)
