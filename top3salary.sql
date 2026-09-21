select
    Department, 
    Employee,
    Salary
from(
select 
    d.name as Department,
    e.name as Employee,
    e.salary as Salary,
    DENSE_RANK() over (
        partition by e.departmentId
        order by e.salary desc

    )as salary_rank

from Employee e 
join Department d
    on e.departmentId = d.id
)t
where salary_rank<= 3
order by
    Department,
    Salary desc,
    Employee;
 