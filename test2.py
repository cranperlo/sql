import beta1

mydb, mycursor = beta1.connect_to_database()
if __name__ == "__main__":
    beta1.passwordmanager(mycursor, mydb)
