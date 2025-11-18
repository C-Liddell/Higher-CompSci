SELECT r.ResortName, AVG(h.pricePersonNight) AS "Avg Price PPPN"
FROM Hotel h, Resort r
WHERE r.resortID = h.resortID
GROUP BY r.resortID
HAVING "Avg Price PPPN" > 100
ORDER BY "Avg Price PPPN" DESC;
