import logging
import sys
from datetime import datetime
import os

# Create logs directory if not present
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name
LOG_FILE = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Logger setup
logger = logging.getLogger("credit-risk-api")
logger.setLevel(logging.DEBUG)

# File Handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)

# Stream Handler (for console)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(module)s - %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
