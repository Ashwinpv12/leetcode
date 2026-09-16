-- second highest salary in employee table
select (
select distinct salary 
 from Employee
order by salary DESC
LIMIT 1 
OFFSET 1)
AS SecondHighestSalary;