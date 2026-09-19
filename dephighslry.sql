--highest salary in each department
select 
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
from employee e
join department d
    on e.departmentId = d.id
where e.salary=(
    select MAX(e2.salary)
    from Employee e2
    where e2.departmentId = e.departmentId
);    
