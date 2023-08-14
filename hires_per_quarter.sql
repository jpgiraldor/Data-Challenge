SELECT a.department, b.job, SUM(case when EXTRACT(MONTH FROM c.datetime) in (1,2,3) then 1 else 0 end) Q1, SUM(case when EXTRACT(MONTH FROM c.datetime) in (4,5,6) then 1 else 0 end) Q2, SUM(case when EXTRACT(MONTH FROM c.datetime) in (7,8,9) then 1 else 0 end) Q3, SUM(case when EXTRACT(MONTH FROM c.datetime) in (10,11,12) then 1 else 0 end) Q4
from departments a
join hired_employees c
on a.id = c.department_id
join jobs b
on b.id = c.job_id
where c.datetime < '2022-01-01'::date
group by a.department , b.job
order by a.department asc, b.job asc


