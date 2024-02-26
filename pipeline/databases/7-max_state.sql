-- max state sql
SELECT state, MAX(values) AS Max_Temperature
FROM Temperatures
GROUP BY state
ORDER BY state
