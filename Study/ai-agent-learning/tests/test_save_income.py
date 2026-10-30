from database import get_db_connection, save_income


def test_save_income():
    income = {
        "description": "part-time job",
        "amount": 40.00,
        "currency": "EUR",
        "income_date": "2026-10-30"
    }

    save_income(income)

    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT description, amount, currency, income_date
                FROM income
                WHERE description = %s
                ORDER BY id DESC
                LIMIT 1
                """,
                (income["description"],)
            )

            result = cursor.fetchone()

        assert result is not None
        assert result[0] == income["description"]
        assert float(result[1]) == income["amount"]
        assert result[2] == income["currency"]
        assert result[3].isoformat() == income["income_date"]

    finally:
        connection.close()