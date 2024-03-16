import mysql.connector
import hashlib
import random
import sys


def sql_connector():
    mydb = mysql.connector.connect(
        host="127.0.0.1", user="root", password="Sixflags@1234", database="keyrecord"
    )
    mycursor = mydb.cursor()
    return mydb, mycursor


def IDgenerator():
    alphabetsup = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",
        14: "O",
        15: "P",
        16: "Q",
        17: "R",
        18: "S",
        19: "T",
        20: "U",
        21: "V",
        22: "W",
        23: "X",
        24: "Y",
        25: "Z",
    }
    alphabetsdown = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",
        8: "i",
        9: "j",
        10: "k",
        11: "l",
        12: "m",
        13: "n",
        14: "o",
        15: "p",
        16: "q",
        17: "r",
        18: "s",
        19: "t",
        20: "u",
        21: "v",
        22: "w",
        23: "x",
        24: "y",
        25: "z",
    }
    symbols = [
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "'",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        ".",
        "/",
        ":",
        ";",
        "<",
        "=",
        ">",
        "?",
        "@",
        "[",
        "]",
        "^",
        "_",
        "`",
        "{",
        "|",
        "}",
        "~",
    ]
    uniqueID = ""
    for i in range(20):
        if i % 2 == 0:
            uniqueID += alphabetsup[random.randint(0, 25)]
        elif i % 5 == 0:
            uniqueID += symbols[random.randint(0, 31)]
        else:
            uniqueID += alphabetsdown[random.randint(0, 25)]
    return uniqueID


def uniquecheck():
    mydb, mycursor = sql_connector()

    sql = "SELECT * FROM password WHERE ID=%s"
    while True:
        val = (IDgenerator(),)
        mycursor.execute(sql, val)
        if mycursor.fetchone():
            pass
        else:
            return val[0]


def hashpassword():
    password = input("Enter your password: ")
    t = password.encode("utf-8")
    hashpassword = hashlib.sha256(t).hexdigest()
    return hashpassword


def authorization(username):
    mydb, mycursor = sql_connector()
    hpass = hashpassword()
    uniqueID = input("Enter your ID: ")
    sql = "SELECT * FROM password WHERE ID=%s"
    val = (uniqueID,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()

    for x in result:
        password = x[2]
        name = x[1]
    if password == hpass and name == username:
        print("yes")
    else:
        print("no")
        sys.exit()


def enternewrecord():
    mydb, mycursor = sql_connector()
    uniqueID = uniquecheck()
    username = input("Enter your first name: ")
    password = hashpassword()

    sql = "INSERT INTO password(ID,username,password) VALUES(%s,%s,%s)"
    val = (uniqueID, username, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Your Unique ID is: ", uniqueID)
    print("MAKE SURE TO REMEMBER THIS ALONG WITH YOUR PASSWORD!!!!!!")
