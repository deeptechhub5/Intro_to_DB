if connection.is_connected():
    cursor = connection.cursor()
    # Create database (will not fail if it already exists)
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
