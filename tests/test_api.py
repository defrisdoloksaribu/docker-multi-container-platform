import os
import unittest
from unittest.mock import MagicMock, patch

os.environ.setdefault(
    "DATABASE_URL",
    "postgresql://test:test@localhost:5432/test",
)

from fastapi.testclient import TestClient
from app.main import app

class InventoryAPITests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    @patch("app.main.get_connection")
    def test_health_endpoint(self, mock_connection):
        connection = MagicMock()
        cursor = MagicMock()
        mock_connection.return_value.__enter__.return_value = connection
        connection.cursor.return_value.__enter__.return_value = cursor

        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")

    @patch("app.main.get_connection")
    def test_create_item(self, mock_connection):
        connection = MagicMock()
        cursor = MagicMock()
        mock_connection.return_value.__enter__.return_value = connection
        connection.cursor.return_value.__enter__.return_value = cursor
        cursor.fetchone.return_value = (1, "Keyboard", 10)

        response = self.client.post(
            "/items",
            json={"name": "Keyboard", "quantity": 10},
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            {"id": 1, "name": "Keyboard", "quantity": 10},
        )

    def test_reject_negative_quantity(self):
        response = self.client.post(
            "/items",
            json={"name": "Keyboard", "quantity": -1},
        )

        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
