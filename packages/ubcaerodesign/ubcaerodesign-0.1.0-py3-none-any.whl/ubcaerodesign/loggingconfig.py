# Configure logging
import os
import sys
import logging
from datetime import datetime
from pathlib import Path

def init_logging(self):
    """Sets up file directory for writing logs and data."""
    now = datetime.now()
    timestamp = now.strftime("%Y_%m_%d_%H.%M.%S")

    logging_folder = (
        Path(__file__).resolve().parent / self.config.logging["directory"].lower()
    )

    self.data_folder = logging_folder / f"{timestamp}"
    log_file = self.data_folder / "log.txt"

    # Check if the directories exist and if they don't, make them
    if not os.path.exists(self.data_folder):
        os.makedirs(self.data_folder)
    with open(log_file, "x", encoding="utf-8") as f:
        pass

    # Configure logging
    logging.basicConfig(
        level=logging._nameToLevel[self.config.logging["level"].upper()],
        format="%(asctime)s:%(msecs)03d [%(filename)s - %(levelname)s] \t\t %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout),
        ],
    )

    logging.info("Logging configured successfully.")
