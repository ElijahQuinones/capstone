import sqlite3

connection = sqlite3.connect("Login.db")
cursor = connection.cursor()

#       was used to create the table 
#       command = """ CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT) """  
#       cursor.execute(command)

cursor.execute("INSERT INTO users Values('EJ','test')")
cursor.execute("INSERT INTO users Values('Bello','test')")
cursor.execute("INSERT INTO users Values('Xinrong','test')")
cursor.execute("INSERT INTO users Values('Nikolas','test')")
connection.commit()
