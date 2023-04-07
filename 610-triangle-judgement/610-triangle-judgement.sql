# Write your MySQL query statement below
SELECT x, y, z, 
CASE
    WHEN (x + z > y AND x + y > z AND y + z > x) = 1
    THEN "Yes"
    ELSE "No"
END as triangle 

FROM Triangle