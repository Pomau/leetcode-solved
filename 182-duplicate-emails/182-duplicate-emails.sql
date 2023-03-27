# Write your MySQL query statement below
SELECT P.email as Email From Person P LEFT JOIN Person P2 ON P.email = P2.email GROUP BY P.email HAVING COUNT(*) > 1