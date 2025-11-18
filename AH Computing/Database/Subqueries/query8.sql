SELECT Name
FROM volcanoes
WHERE Volcano_ID IN (
	SELECT Volcano_ID
	FROM volcanoes
	WHERE Volcano_ID BETWEEN 1000 AND 1100
);