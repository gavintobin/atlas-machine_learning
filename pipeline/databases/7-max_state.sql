-- max state sql
SELECT state, MAX(values) AS max_temp
FROM Temperatures
GROUP BY state
ORDER BY state
