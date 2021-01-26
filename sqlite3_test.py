import sqlite3

# connect to data base
conn = sqlite3.connect('hardware.db')
# create a cursor
c = conn.cursor()

# create a table
##c.execute("CREATE TABLE products (name text,price real)")

# add items to the table
## c.execute("INSERT INTO products VALUES (?, ?, ?")

# add many item into the table
#data = [('NVIDIA RTX 2070', 300), ('NVIDIA RTX 1070', 200)]
#c.executemany("INSERT INTO products VALUES (?, ?)", data)

#update records
#c.execute("""UPDATE products SET name = 'Nvidia RTX 2070', price = 379.99
			#WHERE rowid = 5
			#""")


# how to delite an item
#c.execute("DELETE from products WHERE rowid = ?")


# order by
#c.execute("SELECT rowid, * FROM products ORDER BY rowid")

#print values
#c.execute("SELECT rowid, * FROM products")
#items = c.fetchall()
# print a table
#print("ITEM NUMBER:" + "\tPRODUCT NAME:" + "        \tPRODUCT PRICE(USD):")
#print("___________" + "_____________" +"____________________________________")
#for item in items:
	#print(str(item[0]) + "\t\t" + item[1] + "\t\t" + str(item[2])+" $")


# commit our comand
conn.commit()


#close our connection
conn.close()


def create_table():
	# connect to data base
	conn = sqlite3.connect('hardware.db')
	# create a cursor
	c = conn.cursor()
	# create a table
	c.execute("CREATE TABLE products (name text,price real)")
	# commit our comand
	conn.commit()
	#close our connection
	conn.close()

 
def show_all():
	# connect to data base
	conn = sqlite3.connect('hardware.db')
	# create a cursor
	c = conn.cursor()
	#select all values from the table include rowid's
	c.execute("SELECT rowid, * FROM products WHERE name LIKE 'Nvidia RTX 3080'")
	# print a table(as a good looking table)
	print("ITEM NUMBER:" + "\tPRODUCT NAME:" + "        \tPRODUCT PRICE(USD):")
	print("___________" + "_____________" +"____________________________________")
	items = c.fetchall()
	for item in items:
		print(str(item[0]) + "\t\t" + item[1] + "\t\t" + str(item[2])+" $")
	# commit our comand
	conn.commit()
	#close our connection
	conn.close()

#add a new record to the table
def add_one(p_name,p_price):
	# connect to data base
	conn = sqlite3.connect('hardware.db')
	# create a cursor
	c = conn.cursor()
	c.execute("INSERT INTO products VALUES (?, ?)", (p_name, float(p_price)))
	# commit our comand
	conn.commit()
	#close our connection
	conn.close()




def delete_row(id):
	# connect to data base
	conn = sqlite3.connect('hardware.db')
	# create a cursor
	c = conn.cursor()
	# deletes one row please input a snum iside a string (dont ask why just do it)
	c.execute("DELETE from products WHERE rowid = (?)", id)
	# commit our comand
	conn.commit()
	#close our connection
	conn.close()


def add_many(data):
	# connect to data base
	conn = sqlite3.connect('hardware.db')
	# create a cursor
	c = conn.cursor()
	# add many item into the table
	c.executemany("INSERT INTO products VALUES (?, ?)", (list))
	# commit our comand
	conn.commit()
	#close our connection
	conn.close()


def take_all():
	items = ()
	# connect to data base
	conn = sqlite3.connect('hardware.db')
	# create a cursor
	c = conn.cursor()
	#select all values from the table include rowid's
	c.execute("SELECT rowid, * FROM products")
	items = c.fetchall()
	# commit our comand
	conn.commit()
	#close our connection
	conn.close()


def search(p_name):
	conn = sqlite3.connect('hardware.db')
	c = conn.cursor()
	names = c.execute("SELECT rowid, * FROM products WHERE {} LIKE '%{}%'".format('name',p_name))
	conn.commit()
		

def update():
	conn = sqlite3.connect('hardware.db')
	c = conn.cursor()
	c.execute("""UPDATE products SET name = 'Nvidia RTX 3090'
			WHERE rowid = 1
			""")
	conn.commit()
	conn.close()