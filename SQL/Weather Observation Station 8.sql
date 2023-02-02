SELECT DISTINCT CITY 
FROM STATION
WHERE ((CITY regexp '^[aeiou]') and (CITY regexp '[aeiou]$'));
