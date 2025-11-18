SELECT Name
FROM volcanoes
WHERE Country IN (
	SELECT Country
	FROM volcanoes
	GROUP BY Country
	HAVING COUNT(*) < 3
);