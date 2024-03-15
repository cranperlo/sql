import time
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Sixflags@1234", database="bhav"
)
mycursor = mydb.cursor()

number_of_rows = mycursor.execute("SELECT * FROM alpha3")
rows = mycursor.fetchall()
number_of_rows = len(rows)

print(number_of_rows)


def addnewrecords(site, username, password, uniqueID):
    currentdate = datetime.today()
    curr_time = time.strftime("%H:%M:%S", time.localtime())

    sql = "INSERT INTO alpha3(ID,username,password,site,date,time) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (uniqueID, username, password, site, currentdate, curr_time)

    mycursor.execute(sql, val)
    mydb.commit()


def showpasswords(site1):
    sql = f"SELECT * FROM alpha3 WHERE site=%s"
    val = (site1,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()

    for x in result:
        print("ID:", x[0])
        print("Username:", x[1])
        print("Password:", x[2])
        print("Site:", x[3])
        print("Date:", x[4])
        print("Time:", x[5])


def showeverything():
    sql = "SELECT * FROM alpha3"
    mycursor.execute(sql)

    result = mycursor.fetchall()
    for x in result:
        print("ID:", x[0])
        print("Username:", x[1])
        print("Password:", x[2])
        print("Site:", x[3])
        print("Date:", x[4])
        print("Time:", x[5])


def alterrecord(uniqueID, username, password):
    currentdate = datetime.today()
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    sql = "UPDATE alpha3 SET username = %s, password =%s, date = %s, time = %s WHERE ID = %s"
    val = (username, password, currentdate, curr_time, uniqueID)

    mycursor.execute(sql, val)
    mydb.commit()


def deleterecord():
    print(
        "WARNING! THIS WILL RECORD A SINGULAR RECORD CORRESPONDING TO THE ID ENTERERD"
    )
    print("MAKE SURE TO ENTER THE CORRECT ID!!!")
    uniqueID = input("Enter the ID: ")
    sql = "DELETE FROM alpha3 WHERE ID= %s"
    val = (uniqueID,)
    mycursor.execute(sql, val)
    mydb.commit()


def deleterecords():
    print("WARNING! THIS WILL DELETE ALL RECORDS")
    ans = input("Do you wish to delete all records?(y/n): ")
    if ans == "y":
        sql = "DELETE FROM alpha3"
        mycursor.execute(sql)
        mydb.commit()
        print("RECORDS ARE DELETED")
    else:
        print("RECORDS NOT DELETED")
        print("CHECK THE RECORDS TO MAKE SURE ALL RECORDS EXIST AS THEY SHOULD")


while True:
    print("1) Add new record")
    print("2) Show record")
    print("3) Show everything")
    print("4) Alter record")
    print("5) Delete record")
    print("6) Wipe records")
    print("7) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter name of the site: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        uniqueID = number_of_rows + 1
        addnewrecords(site, username, password, uniqueID)

    elif choice == "2":
        site1 = input("Give name of the site: ")

        showpasswords(site1)

    elif choice == "3":
        showeverything()

    elif choice == "4":
        uniqueID = input("Give ID of the record to be changed: ")
        username = input("Give the new username: ")
        password = input("Give the new password: ")
        alterrecord(uniqueID, username, password)

    elif choice == "5":
        deleterecord()

    elif choice == "6":
        deleterecords()

    elif choice == "7":
        break
    else:
        break
