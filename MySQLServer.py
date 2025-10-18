import mysql.connector
from mysql.connector import Error

try:
# Connect to MySQL server
connection = mysql.connector.connect(
host='localhost',
user='root', # change this if your username is different
password='Fromme2you@1' 
)

if connection.is_connected():
    cursor = connection.cursor()
    # Create database (will not fail if it already exists)
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except Error as e:
print(f"Error while connecting to MySQL: {e}")

finally:
# Close connection
if 'connection' in locals() and connection.is_connected():
cursor.close()
connection.close()
print("MySQL connection closed.")