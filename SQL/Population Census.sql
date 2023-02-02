SELECT SUM(C.Population)
FROM CITY C
INNER JOIN Country Co
ON C.CountryCode = Co.Code
WHERE Co.Continent = "Asia";
