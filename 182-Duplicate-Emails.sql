# Write your MySQL query statement below

SELECT Email


FROM Person p 

GROUP BY Email

HAVING count(*)>1


