import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection


def save_spending(spending):
    query = """INSERT INTO spending
    (Description, Amount, currency, category)
    VALUES(%s ,%s ,%s ,%s )
    """

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query,
                (spending["description"], spending["amount"], spending["currency"], spending["category"]))

            connection.commit()
    finally:
        connection.close()