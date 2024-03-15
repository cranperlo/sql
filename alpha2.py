import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Sixflags@1234", database="bhav"
)
mycursor = mydb.cursor()


while True:
    print("1) Add new passowrd")
    print("2) Show passowrds")
    print("3) Show whole list")
    print("4) Wipe table")
    print("5) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("enter name of the site: ")
        username = input("enter the username: ")
        passowrd = input("enter the password: ")
        time = datetime.now()
        sql = (
            "INSERT INTO alpha2 (username, passwords,site,datetime) VALUES(%s,%s,%s,%s)"
        )
        values = (username, passowrd, site, time)
        mycursor.execute(sql, values)
        mydb.commit()
    elif choice == "5":
        break
    elif choice == "2":
        site1 = input("Give name of site: ")

        sql = f"SELECT * FROM alpha2 WHERE site=%s"
        values = (site1,)
        mycursor.execute(sql, values)

        result = mycursor.fetchall()

        for x in result:
            print(x)
    elif choice == "3":
        sql = "SELECT * FROM alpha2"
        mycursor.execute(sql)

        result = mycursor.fetchall()
        for x in result:
            print(x)
    elif choice == "4":
        sql = "DELETE FROM alpha2"
        mycursor.execute(sql)
        mydb.commit()
