import requests
import logging

# Configure logging
logging.basicConfig(filename='weather_update.log', level=logging.INFO, format='%(asctime)s %(message)s')

# API URL (using OpenWeatherMap as an example)
api_url = 'http://api.openweathermap.org/data/2.5/weather?q=Stockholm&appid=514508dee52c1783b85ae9268ef053df'

# Function to fetch data from API
def fetch_data_from_api():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an error for bad responses
        logging.info("Data fetched successfully from API.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f'Failed to fetch data from API: {e}')
        return None

if __name__ == '__main__':
    data = fetch_data_from_api()
    if data:
        print(data)  # Print the fetched data
    else:
        print("No data fetched.")
