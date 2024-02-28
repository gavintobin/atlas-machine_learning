-- ranks origins of bands
SELECT origin, SUM(nb_fans) AS total_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
