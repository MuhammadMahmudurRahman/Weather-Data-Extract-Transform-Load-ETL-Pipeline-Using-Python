import logging

# Configure logging
logging.basicConfig(filename='weather_update.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Function to transform data
def transform_data(api_data):
    try:
        # Extract relevant data from API response
        location = api_data['name']
        temperature_kelvin = api_data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        feels_like_kelvin = api_data['main']['feels_like']
        feels_like_celsius = feels_like_kelvin - 273.15
        temp_min_kelvin = api_data['main']['temp_min']
        temp_min_celsius = temp_min_kelvin - 273.15
        temp_max_kelvin = api_data['main']['temp_max']
        temp_max_celsius = temp_max_kelvin - 273.15

        # Log transformed data
        logging.info(f"Transformed data - Location: {location}, Temperature: {temperature_celsius}, Feels Like: {feels_like_celsius}, Min Temp: {temp_min_celsius}, Max Temp: {temp_max_celsius}")

        # Create a dictionary with transformed data
        transformed_data = {
            'location': location,
            'temperature': temperature_celsius,
            'feels_like': feels_like_celsius,
            'temp_min': temp_min_celsius,
            'temp_max': temp_max_celsius
        }
        
        return transformed_data
    except KeyError as e:
        logging.error(f'Missing data in API response: {e}')
        return None

if __name__ == '__main__':
    # Example usage: Simulating an API response for transformation
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
    if transformed_data:
        print(transformed_data)  # Print the transformed data
    else:
        print("Transformation failed.")
