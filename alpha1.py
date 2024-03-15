import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Sixflags@1234", database="bhav"
)
mycursor = mydb.cursor()


while True:
    print("1) Add new password")
    print("2) Show passwords")
    print("3) Show whole table")
    print("4) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter name of the site: ")
        username = input("Enter your username: ")
        user_password = input("Enter your password: ")

        try:
            # Corrected INSERT query
            sql = "INSERT INTO passwords (usernamename, password, site) VALUES (%s, %s, %s)"
            values = (username, user_password, site)
            mycursor.execute(sql, values)

            # Commit the changes to the database
            mydb.commit()

            print("Password added successfully.")
        except Exception as e:
            print(f"Error adding password: {e}")

    elif choice == "2":
        site1 = input("Give name of site: ")

        try:
            # Using parameterized query to prevent SQL injection
            sql = "SELECT * FROM passwords WHERE site = %s"
            value = (site1,)
            mycursor.execute(sql, value)

            result = mycursor.fetchall()
            for row in result:
                print("ID:", row[0])
                print("Username:", row[1])
                print("Password:", row[2])
                print("Site:", row[3])
                print("-------------------------")

            # This line should not have any arguments
            mydb.commit()
        except Exception as e:
            print(f"Error fetching passwords: {e}")
    elif choice == "3":
        try:
            # Show the entire table
            mycursor.execute("SELECT * FROM passwords")
            result = mycursor.fetchall()
            for row in result:
                print("ID:", row[0])
                print("Username:", row[1])
                print("Password:", row[2])
                print("Site:", row[3])
                print("-------------------------")

            # This line should not have any arguments
            mydb.commit()
        except Exception as e:
            print(f"Error fetching passwords: {e}")
    elif choice == "4":
        break
