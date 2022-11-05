

select a.INGREDIENT_TYPE, sum(b.total_order) TOTAL_ORDER
from icecream_info a
join first_half b
on a.flavor = b.flavor
group by a.ingredient_type
order by sum(b.total_order)

