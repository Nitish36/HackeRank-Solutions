SELECT DISTINCT CITY
FROM STATION
WHERE ((CITY regexp '^[bcdfghjklmnpqrstvwxyz]') OR (CITY regexp '[bcdfghjklmnpqrstvwxyz]$'));
