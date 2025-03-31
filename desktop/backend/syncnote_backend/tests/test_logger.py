# tests/test_logger.py
from src.utils.logger import setup_logger

def test_logger_creation():
    logger = setup_logger("TestLogger")
    assert logger is not None
    logger.info("Test log message")
    logger.error("Test error message")
