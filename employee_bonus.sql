select
e.name as name,
m.bonus as bonus
from Employee e
left join Bonus m
on e.empId =m.empId
where m.bonus<1000 or m.empId is null;