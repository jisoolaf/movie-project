load data
infile 'movie.csv'
insert into table movie
fields terminated by ',' 
trailing nullcols(movie_Id "movieseq.nextval",
                  movie_Nm char(2000),
                  director_Nm char(2000),
                  open_Dt char(2000),
                  show_Tm char(2000),
                  nation_Nm char(2000),
                  genre_Nm char(2000),
                  watch_Grade_Nm char(2000),
                  company_Nm char(2000),
                  sp_Lang char(2000),
                  budget char(2000),
                  actor char(100000),
                  staff char(300000),
                  series char(2000),
                  keywords char(2000),
                  awards char(10000),
                  naver_Cmt char(3000000),
                  naver_Cmt_Nn char(2000),
                  naver_Pre_Eval char(2000),
                  naver_Ex_Pt char(2000),
                  ori_Book char(2000),
                  plot char(10000),
                  audi_Acc char(2000)
)