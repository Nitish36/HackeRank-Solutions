SELECT MAX(salary*months),COUNT(employee_id)
FROM Employee
GROUP BY (salary*months)
ORDER BY (salary*months) DESC
LIMIT 1;
