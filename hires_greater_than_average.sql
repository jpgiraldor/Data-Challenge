with base_count as (
select d.id, d.department, count(he.id) hired
from departments d
join hired_employees he
on d.id = he.department_id
where he.datetime < '2022-01-01'::date
group by d.id, d.department
), base_avg as(
select avg(hired)
from base_count
)select * from base_count
where hired > (select * from base_avg)