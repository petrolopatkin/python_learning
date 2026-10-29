from database import save_spending, get_db_connection


def test_save_spending():
    spending = {
        "description": "test book",
        "amount": 18.00,
        "currency": "EUR",
        "category": "education",
        "purchase_date": "2026-10-26"
    }

    save_spending(spending)

    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT Description, Amount, currency, category, purchase_date
                FROM spending
                WHERE Description = %s
                ORDER BY Id DESC
                LIMIT 1
                """,
                (spending["description"],)
            )
            result = cursor.fetchone()

        assert result is not None
        assert result[0] == spending["description"]
        assert float(result[1]) == spending["amount"]
        assert result[2] == spending["currency"]
        assert result[3] == spending["category"]
        assert result[4].isoformat() == spending["purchase_date"]

    finally:
        connection.close()