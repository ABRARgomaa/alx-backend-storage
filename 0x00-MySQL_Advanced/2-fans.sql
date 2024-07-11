-- table

WITH COUNTRYBANDS AS(
    SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
)

SELECT origin, nb_fans
FROM COUNTRYBANDS
ORDER BY nb_fans DESC;
