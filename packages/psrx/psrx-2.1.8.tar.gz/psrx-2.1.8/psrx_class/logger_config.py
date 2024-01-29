# logger_config.py
from psrx_class import devices
import logging
from datetime import datetime

def setup_logging():
    # Get the current date and time in the desired format
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%d-%m-%yT%H-%M')

    # Set the log file path using the formatted datetime
    log_file_path = rf'C:\{devices.package_name}\logs\{formatted_datetime}.log'

    # Configure logging
    logging.basicConfig(
        filename=log_file_path,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
