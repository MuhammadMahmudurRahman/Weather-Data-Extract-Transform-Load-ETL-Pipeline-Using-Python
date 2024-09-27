import pyodbc
import logging

# Configure logging
logging.basicConfig(filename='weather_update.log', level=logging.INFO, format='%(asctime)s %(message)s')

# SQL Server connection details
server = 'RUMON_LENOVO'
database = 'Python_Kunskapskontroll_2'
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# Function to update SQL table
def update_sql_table(data):
    if data is None:
        logging.error('No data to update the SQL table.')
        return
    
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Update or insert the data into WeatherData table
        cursor.execute(""" 
            IF EXISTS (SELECT * FROM WeatherData WHERE Location = ?)
            BEGIN
                UPDATE WeatherData SET Temperature = ?, FeelsLike = ?, TempMin = ?, TempMax = ? WHERE Location = ?
            END
            ELSE
            BEGIN
                INSERT INTO WeatherData (Location, Temperature, FeelsLike, TempMin, TempMax) 
                VALUES (?, ?, ?, ?, ?)
            END
            """, data['location'], data['temperature'], data['feels_like'], data['temp_min'], data['temp_max'],
               data['location'], data['location'], data['temperature'], data['feels_like'], data['temp_min'], data['temp_max'])
        conn.commit()
        logging.info('SQL table updated successfully')
        print("Data loaded into SQL table successfully.")  # Print confirmation

    except pyodbc.DatabaseError as db_err:
        logging.error(f'Database error occurred: {db_err}')
        print("Database error occurred.")
    except Exception as e:
        logging.error(f'Error updating SQL table: {str(e)}')
        print("Error updating SQL table.")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    # Example usage: Simulating data to load into SQL
    example_data = {
        'location': 'Stockholm',
        'temperature': 15.0,
        'feels_like': 12.0,
        'temp_min': 10.0,
        'temp_max': 20.0
    }
    update_sql_table(example_data)
