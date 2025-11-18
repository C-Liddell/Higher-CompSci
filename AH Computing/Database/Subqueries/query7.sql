SELECT Country
FROM volcanoes
WHERE Name IN (
	SELECT Name
	FROM volcanoes
	WHERE Name LIKE "%GROUP%"
)
GROUP BY Country;