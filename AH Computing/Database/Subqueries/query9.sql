SELECT Country
FROM volcanoes
WHERE Country NOT IN (
	SELECT Country
	FROM volcanoes
	WHERE Name LIKE "%CALDERA%"
	GROUP BY Country
)
GROUP BY Country;