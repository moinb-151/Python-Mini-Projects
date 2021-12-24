import hashlib
import mysql.connector as c

conn = c.connect(host="localhost", database="simple_login", user="root", password="")


def signup(conn):
    mydb = conn.cursor()
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode("utf-8")
        hash1 = hashlib.md5(enc).hexdigest()
        query = "INSERT INTO user_table(username,pwd) VALUES('{}','{}')".format(
            email, hash1
        )
        mydb.execute(query)
        conn.commit()
        print("Account created successfully! \n")
    else:
        print("Password is not same as above! \n")
        signup(conn)


def login(conn):
    mydb = conn.cursor()
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode("utf-8")
    auth_hash = hashlib.md5(auth).hexdigest()
    query = "SELECT username,pwd FROM user_table WHERE username = '{}' AND pwd = '{}'".format(
        email, auth_hash
    )
    mydb.execute(query)
    result = mydb.fetchall()
    if len(result) == 0:
        print("Login Failed! \n")
    else:
        print("Logged in successfully! \n")


while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup(conn)
    elif ch == 2:
        login(conn)
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
