import sys
from utils.logger import logger  # ✅ this is now safe to import

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error in file: {file_name}, line: {line_number}, message: {str(error)}"

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(error_message, error_detail)
        super().__init__(self.error_message)
        logger.error(self.error_message)  # ✅ safe logger usage
