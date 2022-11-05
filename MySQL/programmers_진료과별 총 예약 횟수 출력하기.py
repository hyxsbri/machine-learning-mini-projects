

select mcdp_cd '진료과코드', count(*) '5월예약건수'
from appointment
where apnt_ymd like '2022-05%'
group by mcdp_cd
order by count(*), mcdp_cd

