import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Sixflags@1234", database="bhav"
)
mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE alpha2 ADD COLUMN datetime DATETIME")
print("1) Add data")
print("2) Edit RollNo")
print("3) Show data")
print("4) Show all")

choice = input("Enter your choice: ")
if choice == "1":
    name = input("enter name of student: ")
    rollno = input("give rollno of student: ")
    uniqueid = input("give ID: ")
    time = datetime.now()

    sql = "INSERT INTO test (name, rollno, ID, datetime) VALUES (%s,%s,%s,%s)"
    val = (name, rollno, uniqueid, time)
    mycursor.execute(sql, val)

    mydb.commit()
elif choice == "2":
    uniqueid = input("Give ID of student: ")
    newrn = input("Give new roll no: ")
    sql = f"UPDATE test SET rollno = %s WHERE ID = %s"
    values = (newrn, uniqueid)
    mycursor.execute(sql, values)

    mydb.commit()
elif choice == "3":
    uniqueid = input("Give ID of student: ")
    sql = f"SELECT * FROM test WHERE ID=%s"
    val = (uniqueid,)
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
