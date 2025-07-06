#!/usr/bin/env python3

import mysql.connector
from mysql.connector import errorcode

print("Script started...")

config = {
    "user": "root",
    "password": "Gabby247marho",  # Replace with your real password
    "host": "localhost"
}

try:
    print("Connecting to MySQL server...")
    conn = mysql.connector.connect(**config)
    print("Connected to server!")

    cursor = conn.cursor()
    print("Running CREATE DATABASE query...")
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")

except Exception as e:
    print(f"General Error: {e}")

finally:
    print("Running cleanup...")
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
    print("Connection closed.")
