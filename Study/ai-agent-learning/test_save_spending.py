from database import save_spending
from database import get_db_connection

spending = {
    "description": "test book",
    "amount": 18.00,
    "currency": "EUR",
    "category": "education"
}

save_spending(spending)

connection = get_db_connection()

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE()")
        print("Current database:", cursor.fetchone())
        cursor.execute("SELECT * FROM spending LIMIT 1")
        print(cursor.fetchall())

        # result = cursor.fetchone()
        # print(result)
finally:
    connection.close()