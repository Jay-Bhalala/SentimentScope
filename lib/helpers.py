import os
import logging
from datetime import datetime

def create_directory(path):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_current_timestamp():
    """Returns the current timestamp as a formatted string."""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def setup_logging(log_file):
    """Sets up logging configuration."""
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def log_message(message, level='info'):
    """Logs a message with the specified level."""
    if level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)