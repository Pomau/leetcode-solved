# Write your MySQL query statement below
SELECT C.name as Customers FROM Customers C LEFT JOIN Orders O ON O.customerId = C.id WHERE O.customerId IS NULL