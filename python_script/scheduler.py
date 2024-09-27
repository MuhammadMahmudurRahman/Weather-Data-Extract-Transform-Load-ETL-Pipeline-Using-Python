import subprocess
import logging

# Configure logging
logging.basicConfig(
    filename='scheduler_test.log',  # Log file name
    level=logging.INFO,             # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

def create_task():
    task_name = "PromptUserTask"
    bat_file_path = r"C:\Rumon\DS23EC\8. Python\Kunskapskontroll 2\Muhammad_Kunskapskontroll_2\open_task_scheduler.bat"

    # Command to create a task in Task Scheduler
    command = [
        "schtasks",
        "/create",
        "/tn", task_name,
        "/tr", f'"{bat_file_path}"',  # Run the .bat file
        "/sc", "once",                 # Set to run once
        "/st", "00:00",                # Placeholder for start time (can be changed later)
        "/f"                           # Force if the task already exists
    ]

    # Print command for debugging
    logging.info("Command to create task: %s", " ".join(command))

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Task '%s' created successfully. You can now set the actual time in Task Scheduler.", task_name)
            print("Task created successfully. Please set the actual time in Task Scheduler.")
        else:
            logging.error("Failed to create task: %s", result.stderr)
            print("Failed to create task:", result.stderr)
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    create_task()
