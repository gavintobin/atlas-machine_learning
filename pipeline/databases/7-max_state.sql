-- max state sql
SELECT State, MAX(Temperature) AS Max_Temperature
FROM Temperatures
GROUP BY State
ORDER BY State
