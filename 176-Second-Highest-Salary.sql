select max(salary) as  secondHighestSalary
from Employee e
where salary<>(
    select max(salary)
    from Employee
)