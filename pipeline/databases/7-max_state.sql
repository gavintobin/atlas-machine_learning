-- max state sql
SELECT state, MAX(values) AS Max_Temp
FROM Temperatures
GROUP BY state
ORDER BY state
