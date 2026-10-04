import os

from dotenv import load_dotenv
import mysql.connector

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

print(connection.is_connected())

cursor = connection.cursor()

name = "Peter Novak"

cursor.execute("SELECT * FROM customers WHERE name = %s",
               (name,))

customer = cursor.fetchone()

print(customer)

cursor.close()
connection.close()