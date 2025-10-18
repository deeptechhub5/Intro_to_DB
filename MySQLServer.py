import mysql.connector

try:
# Connect to MySQL server
connection = mysql.connector.connect(
host='localhost',
user='root', # change this if your username is different
password='Fromme2you@1' # replace with your actual MySQL password
)
if connection.is_connected():
    cursor = connection.cursor()
    # Create the database (will not fail if it already exists)
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
print(f"Error while connecting to MySQL: {e}")

finally:
# Safely close the connection
if 'connection' in locals() and connection.is_connected():
cursor.close()
connection.close()
print("MySQL connection closed.")