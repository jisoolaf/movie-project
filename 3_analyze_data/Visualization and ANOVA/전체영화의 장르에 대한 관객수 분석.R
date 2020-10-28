install.packages('dplyr')
library(dplyr)

install.packages('car')
library(car)

data <- read.csv('movie_regression.csv')
str(data)
data[1:3,]
genre <- data['GENRE_NM']
x <- subset(genre, genre == '')
x
genre[genre == '' ] <- '장르없음'
unique(genreaud[, c('GENRE_NM')])
aud <- data['AUDI_ACC']
title <- data['TITLE']
genreaud <- data.frame(cbind(aud, genre))
distinct(genreaud, GENRE_NM)
genreaud$GENRE_NM[is.na(genreaud$GENRE_NM)] <- '없음'
genres_new <- data.frame()
n <- nrow(genreaud)
for ( i in 1:n){
  print(i)
  name_index <- as.numeric(genreaud[i, 1])
  item_index <- as.character(genreaud[i, 2])
  item_index_split_temp <- data.frame(strsplit(item_index, split='/'))
  genres_temp <- data.frame(cbind(name_index, item_index_split_temp))
  names(genres_temp) <- c('name', 'item')
  genres_new <- rbind(genres_new, genres_temp)
  print(genres_temp)
}
rm(name_index, item_index, item_index_split_temp, genres_temp)

distinct(genres_new)
genres_new
genres_new$name <- as.numeric(genres_new$name)
str(genres_new)

library(ggplot2)

install.packages('forcats')
library(forcats) # fct_lump함수를 이용하여 주요한 n개를 제외하고 다른 값들은 기타로 지정한다.

label_ko_num = function(num) {
  ko_num = function(x) {
    new_num = x %/% 10000
    return(paste(new_num, '만명', sep = ''))
  }
  return(sapply(num, ko_num))
}


genreaud <- aggregate(name~item,genres_new,mean)
ggplot(genreaud, aes(item, name, fill=item)) + geom_bar(stat="identity") + scale_y_continuous(labels = label_ko_num) + labs(x='장르', y='관객수', fill="장르")  + coord_flip()

 
png(filename='D:/Rclick/장르에 따른 관객수평균 .png', height=500, width=500, bg='white')
dev.off()
