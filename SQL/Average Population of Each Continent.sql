SELECT Co.Continent,FLOOR(AVG(C.Population))
FROM City C
INNER JOIN Country Co
on C.CountryCode = Co.Code
GROUP BY Co.Continent;
