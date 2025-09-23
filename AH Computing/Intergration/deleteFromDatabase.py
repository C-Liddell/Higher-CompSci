import mysql.connector

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='sloco')
c = con.cursor()

c.execute("""DELETE FROM client WHERE Client_ID = 3;""")

print(c.rowcount)

con.commit()
c.close()