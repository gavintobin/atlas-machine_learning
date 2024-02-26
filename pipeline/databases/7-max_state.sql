-- max state sql
SELECT State, MAX(values) AS Max_Temperature
FROM Temperatures
GROUP BY State
ORDER BY State
