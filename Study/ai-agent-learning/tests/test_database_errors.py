import pytest
import pymysql
from unittest.mock import MagicMock, patch, ANY
from database import save_spending

def test_save_spending_rolls_back_on_mysql_error():
    fake_connection = MagicMock()

    mock_cursor = (
        fake_connection.cursor.return_value.__enter__.return_value
    )

    mock_cursor.execute.side_effect = pymysql.MySQLError(
        "Test Database Error"
    )

    with patch("database.get_db_connection",
               return_value = fake_connection):
        spending = {
            "description": "test book",
            "amount": 18.00,
            "currency": "EUR",
            "category": "education",
            "purchase_date": None
        }

        with pytest.raises(pymysql.MySQLError, match="Test Database Error"):
            save_spending(spending)

    fake_connection.rollback.assert_called_once()
    fake_connection.close.assert_called_once()
    fake_connection.commit.assert_not_called()


def test_save_spending_handles_connection_error():
    with patch("database.get_db_connection", 
               side_effect=pymysql.MySQLError("Connection Failed")):
        spending = {
                                "description": "test book",
                                "amount": 18.00,
                                "currency": "EUR",
                                "category": "education"
                            }
        with pytest.raises(pymysql.MySQLError, match="Connection Failed"):
            save_spending(spending)


def test_save_spending_executes_query_with_correct_values():
    fake_connection = MagicMock()

    mock_cursor = (
        fake_connection.cursor.return_value.__enter__.return_value
    )

    with patch("database.get_db_connection",
          return_value=fake_connection):

        spending = {
            "description": "coffee",
            "amount": 3.50,
            "currency": "EUR",
            "category": "food",
            "purchase_date": None
        }

        save_spending(spending)
        actual_query, actual_values = mock_cursor.execute.call_args.args
        assert "INSERT INTO spending" in actual_query
        mock_cursor.execute.assert_called_once_with(
            ANY,
            ("coffee", 3.50, "EUR", "food", None)
        )


def test_save_spending_rolls_back_on_commit_error():
    fake_connection = MagicMock()

    mock_cursor = (
            fake_connection.cursor.return_value.__enter__.return_value
    )
    
    fake_connection.commit.side_effect = pymysql.MySQLError("Commit failed")

    with patch("database.get_db_connection",
               return_value=fake_connection):
        spending = {
                    "description": "coffee",
                    "amount": 3.50,
                    "currency": "EUR",
                    "category": "food",
                    "purchase_date": None
                }
        with pytest.raises(pymysql.MySQLError, match="Commit failed"):
            save_spending(spending)

    fake_connection.rollback.assert_called_once()
    fake_connection.close.assert_called_once()
    fake_connection.commit.assert_called_once()

    mock_cursor.execute.assert_called_once()