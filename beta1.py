import time
from datetime import datetime
import mysql.connector


def connect_to_database():
    host1 = input("Give host name: ")
    user1 = input("Give user: ")
    password1 = input("Give password: ")
    database1 = input("Give database name: ")
    mydb = mysql.connector.connect(
        host=host1, user=user1, password=password1, database=database1
    )
    mycursor = mydb.cursor()
    return mydb, mycursor


def numberofrows(mycursor):
    mycursor.execute("SELECT * FROM alpha3")
    rows = mycursor.fetchall()
    return len(rows)


def addnewrecords(mycursor, mydb):
    site = input("Enter name of the site: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    uniqueID = numberofrows() + 1
    currentdate = datetime.today()
    curr_time = time.strftime("%H:%M:%S", time.localtime())

    sql = "INSERT INTO alpha3(ID,username,password,site,date,time) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (uniqueID, username, password, site, currentdate, curr_time)

    mycursor.execute(sql, val)
    mydb.commit()


def showpasswords(mycursor):
    site1 = input("Give name of the site: ")
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


def showeverything(mycursor):
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


def alterrecord(mycursor, mydb):
    uniqueID = input("Give ID of the record to be changed: ")
    username = input("Give the new username: ")
    password = input("Give the new password: ")
    currentdate = datetime.today()
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    sql = "UPDATE alpha3 SET username = %s, password =%s, date = %s, time = %s WHERE ID = %s"
    val = (username, password, currentdate, curr_time, uniqueID)

    mycursor.execute(sql, val)
    mydb.commit()


def deleterecord(mycursor, mydb):
    print(
        "WARNING! THIS WILL RECORD A SINGULAR RECORD CORRESPONDING TO THE ID ENTERERD"
    )
    print("MAKE SURE TO ENTER THE CORRECT ID!!!")
    uniqueID = input("Enter the ID: ")
    sql = "DELETE FROM alpha3 WHERE ID= %s"
    val = (uniqueID,)
    mycursor.execute(sql, val)
    mydb.commit()


def deleterecords(mycursor, mydb):
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


def passwordmanager(mycursor, mydb):

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
            print("Number of records are: ", numberofrows(mycursor))
            addnewrecords(mycursor, mydb)
        elif choice == "2":
            showpasswords(mycursor)
        elif choice == "3":
            showeverything(mycursor)
        elif choice == "4":
            alterrecord(mycursor, mydb)
        elif choice == "5":
            deleterecord(mycursor, mydb)
        elif choice == "6":
            deleterecords(mycursor, mydb)
        elif choice == "7":
            break
        else:
            print("Invalid choice, please enter number 1-7 as the input!!")
