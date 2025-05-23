# networksecurity/exception/exception.py

import sys
from networksecurity.logging.logger import logger

class NetworkSecurityException(Exception):
    """
    Custom exception class for network security-related errors.
    Captures error message, line number, and filename.
    """
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
        self.error_message = error_message

    def __str__(self):
        return (
            f"Error occurred in python script [{self.filename}] "
            f"at line number [{self.lineno}]: {self.error_message}"
        )
