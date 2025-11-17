SELECT c.firstname, c.surname, COUNT(b.hotelRef) AS "Total Bookings"
FROM Booking b, Customer c
WHERE c.customerNo = b.customerNo
GROUP BY c.customerNo
HAVING "Total Bookings" BETWEEN 2 AND 4
ORDER BY "Total Bookings" DESC;