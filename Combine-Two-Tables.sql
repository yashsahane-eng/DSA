# Write your MySQL query statement below
select 
p.firstName,
p.lastname,
a.city,
a.state

from 
Person p
left join
Address a 
ON p.personId=a.personId 
