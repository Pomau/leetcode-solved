# Write your MySQL query statement below
SELECT E.name as Employee FROM Employee E LEFT JOIN Employee E2 ON E.managerId = E2.id WHERE E.salary > E2.salary