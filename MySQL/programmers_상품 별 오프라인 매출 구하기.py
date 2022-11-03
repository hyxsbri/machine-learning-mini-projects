

select a.product_code, (a.price * b.amounts) SALES
from product a
join (select product_id, sum(sales_amount) amounts
     from offline_sale
     group by product_id) b
on a.product_id = b.product_id
order by SALES desc, product_code asc

