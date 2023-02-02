SELECT DISTINCT CITY
FROM STATION
WHERE ((CITY regexp '^[bcdfghjklmnpqrstvwxyz]') AND (CITY regexp '[bcdfghjklmnpqrstvwxyz]$'));
