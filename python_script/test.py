import unittest
from unittest.mock import patch, MagicMock
from extract import fetch_data_from_api
from transfer import transform_data
from load import update_sql_table

class TestWeatherETL(unittest.TestCase):

    @patch('extract.requests.get')
    def test_fetch_data_from_api(self, mock_get):
        # Simulate a successful API response
        mock_get.return_value = MagicMock(status_code=200)
        mock_get.return_value.json.return_value = {
            'name': 'Stockholm',
            'main': {
                'temp': 288.15,
                'feels_like': 285.32,
                'temp_min': 287.04,
                'temp_max': 289.82
            }
        }

        data = fetch_data_from_api()
        self.assertIsNotNone(data, "Failed to fetch data from API.")
        self.assertIn('name', data, "Response data does not contain 'name'.")
        self.assertIn('main', data, "Response data does not contain 'main'.")
        print("fetch_data_from_api test passed.")

    def test_transform_data(self):
        example_api_data = {
            'name': 'Stockholm',
            'main': {
                'temp': 288.15,
                'feels_like': 285.32,
                'temp_min': 287.04,
                'temp_max': 289.82
            }
        }
        transformed_data = transform_data(example_api_data)
        self.assertIsNotNone(transformed_data, "Transformation failed.")
        self.assertEqual(transformed_data['location'], 'Stockholm', "Location mismatch.")
        self.assertAlmostEqual(transformed_data['temperature'], 15.0, places=1, msg="Temperature conversion error.")
        print("transform_data test passed.")

    @patch('load.pyodbc.connect')
    def test_update_sql_table(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        example_data = {
            'location': 'Stockholm',
            'temperature': 15.0,
            'feels_like': 12.0,
            'temp_min': 10.0,
            'temp_max': 20.0
        }

        # Test the update_sql_table function
        update_sql_table(example_data)
        
        # Check if the SQL command was executed
        mock_cursor.execute.assert_called()
        mock_conn.commit.assert_called()
        print("Data loaded into SQL table successfully.")

if __name__ == '__main__':
    unittest.main()
