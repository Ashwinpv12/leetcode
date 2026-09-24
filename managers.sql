--managers with at least 5 direct reports
select m.name
from Employee e
join Employee m
  on e.managerId = m.id
where e.managerId is not null
group by m.id,m.name
having count(*)>=5;