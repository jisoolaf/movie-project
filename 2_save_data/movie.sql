drop table movie;

create table movie(movie_Id number primary key, 
                   movie_Nm varchar2(200) not null,
                   director_Nm varchar2(200),
                   open_Dt date,
                   show_Tm number check(show_Tm >=0),
                   nation_Nm varchar2(200),
                   genre_Nm varchar2(200),
                   watch_Grade_Nm varchar2(30) check(watch_Grade_Nm in('전체관람가','12세이상관람가','15세이상관람가','청소년관람불가')),
                   company_Nm varchar2(255),
                   sp_Lang varchar2(100),
                   budget number check(budget >=0),
                   actor nclob,
                   staff nclob,                  
                   series number check(series in (0,1)),
                   keywords varchar2(700),
                   awards nclob,
                   naver_Cmt nclob,
                   naver_Cmt_Nn number check(naver_Cmt_Nn >=0),
                   naver_Pre_Eval number check(naver_Pre_Eval >=0),
                   naver_Ex_Pt number check(naver_Ex_Pt >=0),
                   ori_Book number check(ori_Book in(0,1)),                   
                   plot nclob,
                   audi_Acc number not null);

                 
select * from movie;


