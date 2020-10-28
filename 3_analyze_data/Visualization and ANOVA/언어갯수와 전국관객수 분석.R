setwd('C:/Users/3731h/Desktop')

library(dplyr)

par(mfrow=c(1,1))

#파일 불러오기
testdata<-read.csv('movie_regression.csv',header=T)



#필요한 컬럼만 불러오기
mydf<-subset(testdata,select = c(NATION_NM_NUM,COMPANY_NM_NUM,GENRE_NM_NUM,SP_LANG_NUM,AUDI_ACC))

head(mydf)

mydf<-mydf%>%filter(!is.na(NATION_NM_NUM) & !is.na(COMPANY_NM_NUM)& !is.na(GENRE_NM_NUM)& !is.na(SP_LANG_NUM)& !is.na(AUDI_ACC))

#언어 갯수로 그룹 나누기
unique(mydf$SP_LANG_NUM) #1~9

group1<-subset(mydf,SP_LANG_NUM==1)
group2<-subset(mydf,SP_LANG_NUM==2)
group3<-subset(mydf,SP_LANG_NUM==3)
group4<-subset(mydf,SP_LANG_NUM==4)
group5<-subset(mydf,SP_LANG_NUM==5)
group6<-subset(mydf,SP_LANG_NUM==6)
group7<-subset(mydf,SP_LANG_NUM==7)
group8<-subset(mydf,SP_LANG_NUM==8)
group9<-subset(mydf,SP_LANG_NUM==9)

group1<-group1$AUDI_ACC
group2<-group2$AUDI_ACC
group3<-group3$AUDI_ACC
group4<-group4$AUDI_ACC
group5<-group5$AUDI_ACC
group6<-group6$AUDI_ACC
group7<-group7$AUDI_ACC
group8<-group8$AUDI_ACC
group9<-group9$AUDI_ACC

#
str(group1)


y1<-as.factor(group1)
y2<-as.factor(group2)
y3<-as.factor(group3)
y4<-as.factor(group4)
y5<-as.factor(group5)
y6<-as.factor(group6)
y7<-as.factor(group7)
y8<-as.factor(group8)
y9<-as.factor(group9)


#타입맞추기

y<-as.numeric(c(y1,y2,y3,y4,y5,y6,y7,y8,y9))

#check each row length
#

length(group1) #1820 행
length(group2) #220
length(group3) #90
length(group4) #34 행
length(group5) #16
length(group6) #5
length(group7) #1
length(group8) #1
length(group9) #1


#grouping
n<- c(1820,220,90,34,16,5,1,1,1)


group<-rep(1:9,n)
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
        main='Boxplot of 전국관객수 by 언어 갯수',
        xlab='Factor Levels:언어 갯수 1/2/3/4/5/6/7/8/9',
        ylab='전국관객수')

#summary
tapply(y,group,summary)

detach(group_df)

#one-way ANOVA
aov(y~group, data=group_df)

summary(aov(y~group, data=group_df))

#Bartlett test
bartlett.test(y~group, data=group_df)
