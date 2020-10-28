data <- read.csv('C:/myworkspace/pydevProject/polarityDict/cmtScore_audiAcc.csv')

head(data)
str(data)
dim(data)

data <- na.omit(data)

data$AUDI_ACC <- as.numeric(data$AUDI_ACC)

# help(cor)

######### CMT_SCORE - AUDI_ACC �������
library(viridis)
library(ggplot2)

chartdata <- cbind(data$CMT_SCORE, data$AUDI_ACC)
class(chartdata)
mode(chartdata)

chartdata <- data.frame(chartdata)

head(chartdata)

ggplot(chartdata , aes( x=X1, y=X2, fill=X1 )) + geom_point(colour='grey', shape=21, size=2) + labs(x='���� ����', y='���� ������', title='���� ������ ���� ������', fill='���� ����') + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method='auto', color='red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('', '���鸸��', 'õ����', 'õ���鸸��')) + scale_x_continuous(breaks=c(-1, -0.5, 0, 0.5, 1), labels=c('-1��','-0.5��', '0��', '0.5��','1��'))



ggplot(chartdata , aes( x=X1, y=X2, fill=X1 )) + geom_point(colour='grey', shape=21, size=2) + labs(x='���� ����', y='���� ������', title='���� ������ ���� ������(�α�)', fill='���� ����') + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method='auto', color='red3') + scale_y_continuous( trans = 'log10') + scale_x_continuous(breaks=c(-1, -0.5, 0.5, 1), labels=c('-1��','-0.5��','0.5��','1��'))



help(geom_smooth)




chartdata <- cbind(data$CMT_SCORE, log(data$AUDI_ACC))
plot(data$CMT_SCORE, log(data$AUDI_ACC))

chartdata <- cbind(data$CMT_SCORE, data$AUDI_ACC)
plot(data$CMT_SCORE, sqrt(data$AUDI_ACC))

cordata <- subset(data, select=c(CMT_SCORE, AUDI_ACC))

pearson <- cor(cordata, method='pearson')
kendall <- cor(cordata, method='kendall')
spearman <- cor(cordata, method='spearman')

# help(corrplot)

# install.packages('corrplot')
library(corrplot)

corrplot(pearson, method='ellipse', addCoef.col='red', title='�������� - ���� ������ corrplot(pearson)', mar=c(1,1,1,1))

corrplot(kendall, method='ellipse', addCoef.col='red', title='�������� - ���� ������ corrplot(kendall)', mar=c(1,1,1,1))

corrplot(spearman, method='ellipse', addCoef.col='red', title='�������� - ���� ������ corrplot(spearman)', mar=c(1,1,1,1))



######### CMT_SCORE - NAVER_PRE_EVAL �������

plot(data$CMT_SCORE, data$NAVER_PRE_EVAL)

cordata <- subset(data, select=c(CMT_SCORE, NAVER_PRE_EVAL))

pearson <- cor(cordata, method='pearson')
kendall <- cor(cordata, method='kendall')
spearman <- cor(cordata, method='spearman')

# help(corrplot)

# install.packages('corrplot')
# library(corrplot)

corrplot(pearson, method='ellipse', addCoef.col='red', title='�������� - ���� ���� corrplot(pearson)', mar=c(1,1,1,1))

corrplot(kendall, method='ellipse', addCoef.col='red', title='�������� - ���� ���� corrplot(kendall)', mar=c(1,1,1,1))

corrplot(spearman, method='ellipse', addCoef.col='red', title='�������� - ���� ���� corrplot(spearman)', mar=c(1,1,1,1))
