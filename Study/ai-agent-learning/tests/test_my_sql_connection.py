from database import get_db_connection

connection = get_db_connection()

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        print(f"Connected to database: {result[0]}")
finally:
    connection.close()