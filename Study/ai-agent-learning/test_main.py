from main import parse_spending
import pytest
import json
import main
import pymysql
from unittest.mock import patch
from google.genai import errors


def test_parse_spending_returns_valid_data():
    raw_response = '{"description": "coffee", "amount": 3.50, "currency": "EUR", "category": "food", "purchase_date": "2026-10-26"}'

    result = parse_spending(raw_response)

    assert result == {
        "description": "coffee",
        "amount": 3.50,
        "currency": "EUR",
        "category": "food",
        "purchase_date": "2026-10-26"
    }


def test_parse_spending_incorrect_json_returns_error():
    raw_response = '{"description": "coffee", "amount": '

    with pytest.raises(json.JSONDecodeError):
        parse_spending(raw_response)


def test_parse_spending_json_contains_invalid_value_returns_error():
    raw_response = '{"description": "coffee", "amount": -5, "currency": "EUR", "category": "food"}'

    with pytest.raises(ValueError):
        parse_spending(raw_response)


def test_ask_gemini_api_error(capsys):
    with patch("builtins.input", side_effect=["coffee 3 EUR", "exit"]):
        with patch("main.ask_gemini", side_effect=errors.APIError(
            code=500,
            response_json={"error": {"message": "Test error"}}
        )) as mock_gemini:
            with patch("main.save_spending") as mock_save:
                main.main()

    output = capsys.readouterr().out

    assert "Gemini API request failed" in output 
    mock_gemini.assert_called_once()
    mock_save.assert_not_called()


def test_main_handles_mysql_error(capsys):
    with patch("builtins.input", side_effect=["coffee 3 EUR", "exit"]):
        with patch("main.ask_gemini", return_value='{"description": "coffee", "amount": 3, "currency": "EUR", "category": "food", "purchase_date": null}') as mock_gemini:
            with patch("main.save_spending", side_effect=pymysql.MySQLError("Database error")) as mock_save:
                main.main()

    output = capsys.readouterr().out

    assert "Failed to save spending" in output
    assert "Database error" in output
    mock_gemini.assert_called_once()
    mock_save.assert_called_once()


def test_main_exits_without_processing(capsys):
    with patch("builtins.input", side_effect= ["exit"]):
        with patch("main.ask_gemini") as mock_gemini:
            with patch("main.save_spending") as mock_save:
                main.main()

    output = capsys.readouterr().out
    assert "Goodbye" in output
    mock_gemini.assert_not_called()
    mock_save.assert_not_called()