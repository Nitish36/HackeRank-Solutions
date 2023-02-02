SELECT C.Name 
FROM CITY C
INNER JOIN COUNTRY Co
ON C.CountryCode = Co.Code
WHERE Co.Continent = "Africa";
