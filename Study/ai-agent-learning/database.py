import os
import pymysql
from dotenv import load_dotenv
from datetime import date
from decimal import Decimal

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
    (Description, Amount, currency, category, purchase_date)
    VALUES(%s ,%s ,%s ,%s ,%s )
    """

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query,
                (spending["description"], spending["amount"], spending["currency"], spending["category"], spending["purchase_date"]))

            connection.commit()
    except pymysql.MySQLError:
        connection.rollback()
        raise
    finally:
        connection.close()


def get_spending_by_month(year, month):
    query = """
        SELECT 
            Description,
            Amount,
            currency, 
            category,
            purchase_date
        FROM spending
        WHERE purchase_date >= %s AND purchase_date < %s
        ORDER BY purchase_date DESC
        """

    start_date = date(year, month, 1)

    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)

    connection = get_db_connection()

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query, (start_date, end_date))
            return cursor.fetchall()
    finally:
        connection.close()


def get_monthly_summary(year, month):
    spendings = get_spending_by_month(year, month)

    totals = {}

    for spending in spendings:
        currency = spending["currency"]

        if currency not in totals:
            totals[currency] = Decimal("0.00")

        totals[currency] += spending["Amount"]

    most_expensive_by_currency = {}

    for spending in spendings:
        currency = spending["currency"]

        if currency not in most_expensive_by_currency:
            most_expensive_by_currency[currency] = spending
        elif spending["Amount"] > most_expensive_by_currency[currency]["Amount"]:
            most_expensive_by_currency[currency] = spending

    return {
        "totals_by_currency": totals,
        "most_expensive_by_currency": most_expensive_by_currency 
    }