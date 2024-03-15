import time
import mysql.connector
from datetime import datetime
host1 = input("Give host name: ")
user1 = input("Give user: ")
password1 = input("Give password: ")
database1 = input("Give database name: ")

mydb = mysql.connector.connect(
    host = host1 , user = user1, password = password1, database = database1
)
mycursor = mydb.cursor()

number_of_rows = mycursor.execute("SELECT * FROM alpha3")
rows = mycursor.fetchall()
number_of_rows = len(rows)

print(number_of_rows)

while True:
    print("1) Add new record")
    print("2) Show passwords")
    print("3) Show everything")
    print("4) Alter record")
    print("5) Wipe record")
    print("6) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter name of the site: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        uniqueID = number_of_rows + 1
        currentdate = datetime.today()
        curr_time = time.strftime("%H:%M:%S", time.localtime())

        sql = "INSERT INTO alpha3(ID,username,password,site,date,time) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (uniqueID, username, password, site, currentdate, curr_time)

        mycursor.execute(sql, val)
        mydb.commit()

    elif choice == "2":
        site1 = input("Give name of the site: ")

        sql = f"SELECT * FROM alpha3 WHERE site=%s"
        val = (site1,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        for x in result:
            print(x)

    elif choice == "3":
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

    elif choice == "4":
        uniqueID = input("Give ID of the record to be changed: ")
        username = input("Give the new username: ")
        password = input("Give the new password: ")
        currentdate = datetime.today()
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        sql = "UPDATE alpha3 SET username = %s, password =%s, date = %s, time = %s WHERE ID = %s"
        val = (username, password, currentdate, curr_time, uniqueID)

        mycursor.execute(sql, val)
        mydb.commit()

    elif choice == "5":
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

    elif choice == "6":
        break
    else:
        break
