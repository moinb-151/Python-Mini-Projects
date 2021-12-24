import sqlite3
import tabulate

#database connection & creation
conn = sqlite3.connect("contacts.db",timeout = 10)

def setup(conn):
	c = conn.cursor()	
	c.execute(""" CREATE TABLE call_directory (
				first_name text,
				last_name text,
				phone_no integer
		)""")

	conn.commit()
	print("Contact book is ready to use! \n")

def create_contact(conn):
	c = conn.cursor()
	fname = input("Enter first name: ")
	lname = input("Enter last name: ")
	number = int(input("Enter phone number: "))
	query = "INSERT INTO call_directory (first_name, last_name, phone_no) VALUES ('{}','{}',{})".format(fname,lname,number)
	c.execute(query)
	conn.commit()
	print("Contact created successfully!")


def display_contacts(conn):
	c = conn.cursor()
	query = "SELECT * FROM call_directory"
	c.execute(query)
	results = c.fetchall()
	print(tabulate.tabulate(results))

def search_contacts(conn):
	c = conn.cursor()
	print("Search by.....\n")
	print("1.First Name")
	print("2.Last Name")
	print("3.Phone Number \n")
	ch = int(input("Enter your choice: "))

	match ch:
		case 1:
			fname = input("First Name: ")
			query = "SELECT * FROM call_directory WHERE first_name LIKE '%{}%'".format(fname)
			c.execute(query)
			results = c.fetchall()
			print(tabulate.tabulate(results))

		case 2:
			lname = input("Last Name: ")
			query = "SELECT * FROM call_directory WHERE last_name LIKE '%{}%'".format(lname)
			c.execute(query)
			results = c.fetchall()
			print(tabulate.tabulate(results))

		case 3:
			no = input("Phone Number: ")
			query = "SELECT * FROM call_directory WHERE phone_no LIKE '%{}%'".format(no)
			c.execute(query)
			results = c.fetchall()
			print(tabulate.tabulate(results))

		case _:
			print("Wrong Choice!")

def delete_contact(conn):
	c = conn.cursor()
	print("Delete by.....\n")
	print("1.First Name")
	print("2.Last Name")
	print("3.Phone Number \n")
	ch = int(input("Enter your choice: "))

	match ch:
		case 1:
			fname = input("First Name: ")
			query = "DELETE FROM call_directory WHERE first_name = '{}'".format(fname)
			c.execute(query)
			conn.commit()
			print("Contact deleted successfully! \n")

		case 2:
			lname = input("First Name: ")
			query = "DELETE FROM call_directory WHERE last_name = '{}'".format(lname)
			c.execute(query)
			conn.commit()
			print("Contact deleted successfully! \n")

		case 3:
			fname = input("Phone Number: ")
			query = "DELETE FROM call_directory WHERE phone_no = {}".format(fname)
			c.execute(query)
			conn.commit()
			print("Contact deleted successfully! \n")

		case _:
			print("Wrong Choice!")

while True:
	print("******** Phonebook ********")
	print("1.Setup")
	print("2.Create a new contact")
	print("3.Display contacts")
	print("4.Search in contacts")
	print("5.Delete contact")
	print("6.Exit")
	print("\nNote: Run 'Setup' before any other operations if your running program for the very first time.\n")
	ch = int(input("Enter your choice: "))

	match ch:
		case 1:
			setup(conn)

		case 2:
			create_contact(conn)

		case 3:
			display_contacts(conn)

		case 4:
			search_contacts(conn)

		case 5:
			delete_contact(conn)

		case 6:
			break

		case _:
			print("Wrong Choice!")

conn.close()