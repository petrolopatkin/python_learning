import pytest
import pymysql
from unittest.mock import MagicMock, patch, ANY
from database import save_spending, save_income, save_operations

def test_save_operations_rolls_back_on_mysql_error():
    fake_connection = MagicMock()

    mock_cursor = (
        fake_connection.cursor.return_value.__enter__.return_value
    )

    mock_cursor.execute.side_effect = pymysql.MySQLError(
        "Test Database Error"
    )

    operations = [
        {
            "type": "spending",
            "data": {
                "description": "test book",
                "amount": 18.00,
                "currency": "EUR",
                "category": "education",
                "purchase_date": None
            }
        }
    ]

    with patch("database.get_db_connection", return_value=fake_connection):
        with pytest.raises(pymysql.MySQLError, match="Test Database Error"):
            save_operations(operations)

    fake_connection.rollback.assert_called_once()
    fake_connection.close.assert_called_once()
    fake_connection.commit.assert_not_called()


def test_save_operations_handles_connection_error():
    operations = [
        {
            "type": "spending",
            "data": {
                "description": "test book",
                "amount": 18.00,
                "currency": "EUR",
                "category": "education",
                "purchase_date": None
            }
        }
    ]

    with patch("database.get_db_connection", side_effect=pymysql.MySQLError("Connection failed")):
        with pytest.raises(pymysql.MySQLError, match="Connection failed"):
            save_operations(operations)


def test_save_spending_executes_query_with_correct_values():
    fake_connection = MagicMock()

    mock_cursor = (
        fake_connection.cursor.return_value.__enter__.return_value
    )

    spending = {
        "description": "coffee",
        "amount": 3.50,
        "currency": "EUR",
        "category": "food",
        "purchase_date": None
    }

    save_spending(spending, fake_connection)

    actual_query, actual_values = mock_cursor.execute.call_args.args

    assert "INSERT INTO spending" in actual_query

    mock_cursor.execute.assert_called_once_with(
        ANY,
        ("coffee", 3.50, "EUR", "food", None)
    )

    fake_connection.commit.assert_not_called()
    fake_connection.rollback.assert_not_called()
    fake_connection.close.assert_not_called()


def test_save_income_executes_query_with_correct_values():
    fake_connection = MagicMock()

    mock_cursor = (
        fake_connection.cursor.return_value.__enter__.return_value
    )

    income = {
        "description": "salary",
        "amount": 100.00,
        "currency": "EUR",
        "income_date": "2026-10-30"
    }

    save_income(income, fake_connection)

    actual_query, actual_values = mock_cursor.execute.call_args.args

    assert "INSERT INTO income" in actual_query

    mock_cursor.execute.assert_called_once_with(
        ANY,
        ("salary", 100.00, "EUR", "2026-10-30")
    )

    fake_connection.commit.assert_not_called()
    fake_connection.rollback.assert_not_called()
    fake_connection.close.assert_not_called()


def test_save_operations_rolls_back_on_commit_error():
    fake_connection = MagicMock()

    mock_cursor = (
            fake_connection.cursor.return_value.__enter__.return_value
    )
    
    fake_connection.commit.side_effect = pymysql.MySQLError("Commit failed")

    operations = [
            {
                "type": "spending",
                "data": {
                    "description": "test book",
                    "amount": 18.00,
                    "currency": "EUR",
                    "category": "education",
                    "purchase_date": None
                }
            }
        ]

    with patch("database.get_db_connection", return_value=fake_connection):
        with pytest.raises(pymysql.MySQLError, match="Commit failed"):
            save_operations(operations)

    fake_connection.rollback.assert_called_once()
    fake_connection.close.assert_called_once()
    fake_connection.commit.assert_called_once()

    mock_cursor.execute.assert_called_once()