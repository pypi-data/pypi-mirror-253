import logging
import os
import datetime
from pathlib import Path

def create_logger(name) -> logging.Logger:
    logs_path = os.getenv("LOGS_PATH", "./logs")
    logs_folder = Path(logs_path)
    os.makedirs(logs_path, exist_ok=True)
    full_path = logs_folder / f"{datetime.date.today()}_dev_log.log"

    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(full_path, "a", "utf-8")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "(%(name)s) %(asctime)s [%(levelname)s] : (%(message)s)"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
