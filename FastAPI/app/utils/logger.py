# app/utils/logger.py
import logging

# Configure the logging format and level
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Logger instance used throughout the app
logger = logging.getLogger(__name__)
