SELECT Name
FROM volcanoes
WHERE Volcano_ID IN (
	SELECT MAX(Volcano_ID)
	FROM volcanoes
	GROUP BY Country
);