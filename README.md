# Weather_Data_ETL_Pipeline

## A Python-based ETL pipeline that extracts, transforms, and loads weather data, with automated scheduling and monitoring.

• main.py: Orchestrates the ETL process, ensuring the proper sequence and centralized management.

• extract.py: Extracts data.

• transfer.py: Transforms data.

• load.py: Loads data into the SQL table.

• test.py: Contains tests for the ETL process.

• scheduler.py: Schedules the execution of main.py and weather_update.py.

• scheduler_test.log: Monitors the scheduler.

• weather_update.log: Monitors the ETL process.

• weather_update.py: Runs independently for specific tasks, possibly related to weather data updates.

• open_task_scheduler.bat: Manages scheduled tasks.
