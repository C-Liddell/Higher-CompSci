SELECT c.firstname, c.surname, SUM(h.pricePersonNight*b.numberNights*b.numberInParty) AS "Total Cost"
FROM Booking b, Customer c, Hotel h
WHERE c.customerNo = b.customerNo
AND h.hotelRef = b.hotelRef
GROUP BY c.customerNo
HAVING "Total Cost" > 2000
ORDER BY "Total Cost" DESC;