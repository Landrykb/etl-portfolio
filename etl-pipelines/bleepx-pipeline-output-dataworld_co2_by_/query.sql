SELECT country_name,
       MIN(value) AS min_kt,
       MAX(value) AS max_kt,
       (MAX(value) - MIN(value)) AS growth_kt
FROM dataset
WHERE year BETWEEN 2010 AND 2019
GROUP BY country_name
ORDER BY growth_kt DESC;