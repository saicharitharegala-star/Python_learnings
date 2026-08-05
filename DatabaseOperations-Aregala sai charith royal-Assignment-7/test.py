import psycopg2 #this is a library used to connect to the database and perform operations on it

def table():  #this function is used to create a table in the database
  connect = psycopg2.connect(dbname="postgres", user="postgres", password="B@rcelon@12", host="localhost", port="5432")
  
  cursor = connect.cursor()
  cursor.execute('''CREATE TABLE employees(name text, ID int, age int);''')
  print("Table created successfully")



  psycopg2.connect.commit()
  psycopg2.connect.close()

def data(): # this function is used to insert data into the table
 connect = psycopg2.connect(dbname="postgres", user="postgres", password="B@rcelon@12", host="localhost", port="5432")
 cursor = connect.cursor()
 name = input("Enter name: ")
 ID = int(input("Enter ID: "))
 age = int(input("Enter age: "))
 cursor.execute('''insert into employees(name, ID, age) values(%s, %s, %s);''', (name, ID, age))
 print("Data inserted successfully")
 connect.commit()
 connect.close()

data()
def extract(): # this function is used to extract data from the table
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="B@rcelon@12", host="localhost", port="5432")
    cursor = connect.cursor()
    cursor.execute('''SELECT * FROM employees;''')
    print(cursor.fetchall())
    connect.commit()
    connect.close()

extract()