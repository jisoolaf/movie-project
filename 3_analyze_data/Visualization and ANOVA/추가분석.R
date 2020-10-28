movie <- read.csv('train_regression(2차).csv', na.strings = c(''))

glimpse(movie)
top10_company <- movie %>% group_by(COMPANY_NM) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(COMPANY_NM)&!(COMPANY_NM=='기타')) %>% head(10)
ggplot(top10_company, aes(x=reorder(COMPANY_NM,audi_median),y=audi_median,fill=COMPANY_NM)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,500000,1000000,1500000), labels=c('0','50만명','100만명','150만명'))  + theme_classic() + labs(title='빈도수 top10배급사의 관객수 중앙값', x='배급사', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none') + coord_flip()




genre <- movie %>% group_by(PRI_GENRE_NM) %>% summarise(cnt = n(), audi_median=median(log(AUDI_ACC))) %>% arrange(desc(cnt)) %>% filter(!is.na(PRI_GENRE_NM))
ggplot(genre, aes(x=reorder(PRI_GENRE_NM,audi_median), y=audi_median, fill=PRI_GENRE_NM)) + geom_bar(stat='identity')+ scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + coord_flip() + theme_classic() + labs(title='장르에 따른 관객수(로그) 중앙값', x='장르', y='log(관객수) 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')





nation <- movie %>% group_by(NATION_NM) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(NATION_NM)) %>% head(20)
ggplot(nation, aes(x=reorder(NATION_NM,audi_median),y=audi_median,fill=NATION_NM)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,20000,40000,60000), labels=c('0','2만명','4만명','6만명'))  + theme_classic() + labs(title='빈도수 top20제작국가의 관객수 중앙값', x='제작국가', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none') + coord_flip()





movie <- read.csv('movie_analysis.csv', na.strings = c(''))
glimpse(movie)





top10_actor <- movie %>% group_by(ACTOR1) %>% summarise(cnt = n(), audi_sum=sum(AUDI_ACC)) %>% arrange(desc(audi_sum)) %>% filter(!is.na(ACTOR1)) %>% head(10)
ggplot(top10_actor, aes(x=reorder(ACTOR1,audi_sum), y=audi_sum, fill=ACTOR1)) + geom_bar(stat = 'identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,20000000,40000000,60000000), labels=c('0','2000만명','4000만명','6000만명'))  + theme_classic() + labs(title='관객수 TOP10 주인공출연배우', x='배우', y='관객수 총합') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none') + coord_flip()





top10_director <- movie %>% group_by(DIRECTOR) %>% summarise(cnt = n(), audi_sum=sum(AUDI_ACC)) %>% arrange(desc(audi_sum)) %>% filter(!is.na(DIRECTOR)) %>% head(10)
ggplot(top10_director, aes(x=reorder(DIRECTOR,audi_sum), y=audi_sum, fill=DIRECTOR)) + geom_bar(stat = 'identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,10000000,20000000,30000000), labels=c('0','1000만명','2000만명','3000만명'))  + theme_classic() + labs(title='관객수 TOP10 감독', x='감독', y='관객수 총합') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none') + coord_flip()
