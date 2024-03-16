import passwordmanager
import autho

print("1)Enter new employee record")
print("2)Log in")
choice = input("Enter your choice: ")
if choice == "1":
    autho.enternewrecord()
elif choice == "2":
    username = input("Enter your name: ")
    autho.authorization(username)
    mydb, mycursor = passwordmanager.connect_to_database(username)
    if __name__ == "__main__":
        passwordmanager.passwordmanager(mycursor, mydb)
