import mysql.connector
from mysql.connector import Error
def create_database():
    try:
        # Connect to MySQL Server (not a specific database yet)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='information&&123'  # ← replace with your MySQL root password
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")
if __name__ == "__main__":
    create_database()

