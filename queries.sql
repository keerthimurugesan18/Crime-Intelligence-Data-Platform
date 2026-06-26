SELECT COUNT(*) AS Total_Crimes
FROM Crime;

SELECT Location,
COUNT(*) AS Total
FROM Crime
GROUP BY Location
ORDER BY Total DESC;

SELECT Crime_Type,
COUNT(*) AS Total
FROM Crime
GROUP BY Crime_Type;

SELECT Status,
COUNT(*) AS Total
FROM Crime
GROUP BY Status;

SELECT *
FROM Crime
WHERE Crime_Time='Night';

SELECT *
FROM Crime
WHERE Victim_Age > 30;

SELECT *
FROM Crime
WHERE Gender='Female';

SELECT Location,
COUNT(*) AS Crimes
FROM Crime
GROUP BY Location
ORDER BY Crimes DESC
LIMIT 5;