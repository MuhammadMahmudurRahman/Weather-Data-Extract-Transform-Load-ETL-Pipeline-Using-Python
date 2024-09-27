import logging
from extract import fetch_data_from_api
from transfer import transform_data
from load import update_sql_table

# Configure logging
logging.basicConfig(filename='weather_update.log', level=logging.INFO, format='%(asctime)s %(message)s')

def main():
    print("Starting ETL process...")
    logging.info("ETL process started.")

    # Extract data
    print("Extracting data from API...")
    data = fetch_data_from_api()
    if data:
        print("Data extraction completed.")
        logging.info("Data extraction completed.")
    else:
        print("Data extraction failed.")
        logging.error("Data extraction failed.")
        return

    # Transform data
    print("Transforming data...")
    transformed_data = transform_data(data)
    if transformed_data:
        print("Data transformation completed.")
        logging.info("Data transformation completed.")
    else:
        print("Data transformation failed.")
        logging.error("Data transformation failed.")
        return

    # Load data
    print("Loading data into SQL table...")
    update_sql_table(transformed_data)
    logging.info("Data loading completed.")
    print("ETL process completed successfully.")

if __name__ == "__main__":
    main()
