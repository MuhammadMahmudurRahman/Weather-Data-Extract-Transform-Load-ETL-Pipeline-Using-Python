import logging
import time

# Configure logging
logging.basicConfig(
    filename='C:\\Rumon\\DS23EC\\8. Python\\Kunskapskontroll 2\\Muhammad_Kunskapskontroll_2\\weather_update.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Weather update script started")

# Simulate some work with sleep (replace with actual script logic)
time.sleep(5)

# Your weather update code here
logging.info("Weather update script completed")
