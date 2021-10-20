
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)


# preparing a cursor object
cursorObject = dataBase.cursor()

# Creating Table
# studentRecord = """CREATE TABLE STUDENT (
#                    NAME  VARCHAR(20) NOT NULL,
#                    BRANCH VARCHAR(50),
#                    ROLL INT NOT NULL,
#                    SECTION VARCHAR(5),
#                    AGE INT
#                    )"""

# cursorObject.execute(studentRecord)

# Inserting into table STUDENT
# sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
# VALUES (%s, %s, %s, %s, %s)"
# val = [("Nikhil", "CSE", "98", "A", "18"),
#        ("Nisha", "CSE", "99", "A", "18"),
#        ("Rohan", "MAE", "43", "B", "20"),
#        ("Amit", "ECE", "24", "A", "21"),
#        ("Anil", "MAE", "45", "B", "20"),
#        ("Megha", "ECE", "55", "A", "22"),
#        ("Sita", "CSE", "95", "A", "19")]

# cursorObject.executemany(sql, val)
# dataBase.commit()


# Query 1
query1 = "SHOW DATABASES"
cursorObject.execute(query1)

myresult = cursorObject.fetchall()

for i in myresult:
    for j in i:
        print(j)

# Query 2
query2 = "SELECT * FROM STUDENT"
cursorObject.execute(query2)

myresult = cursorObject.fetchall()

print(myresult)

# disconnecting from server
dataBase.close()
