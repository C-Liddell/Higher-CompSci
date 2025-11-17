SELECT r.resortName , COUNT(h.hotelRef) AS "Number of Hotels"
FROM Resort r, Hotel h
WHERE r.resortID = h.resortID
GROUP BY r.resortID
HAVING "Number of Hotels" >= 2
ORDER BY "Number of Hotels" DESC;