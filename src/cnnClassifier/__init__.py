import os
import sys
import logging
from datetime import datetime

LOG_STR = '%(asctime)s | %(levelname)-8s | [%(name)s] - %(filename)s:%(module)s:%(lineno)d : "%(message)s"'
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
os.makedirs(LOG_DIR, exist_ok=True)
log_filepath = os.path.join(LOG_DIR, LOG_FILE)


logging.basicConfig(level=logging.DEBUG,
                    format=LOG_STR,
                    datefmt='%d-%h-%y %H:%m',
                    handlers=[logging.FileHandler(log_filepath),
                              logging.StreamHandler(sys.stdout)])

logger = logging.getLogger('cnnClassiferLogger')


def error_mssg_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    err_file = exc_tb.tb_frame.f_code.co_filename
    error_tb = exc_tb.tb_frame.f_code.__qualname__
    err_line_no = exc_tb.tb_frame.f_lineno
    err_info = str(error)
    error_mssg = f'Error occured in script,line no. - {err_file}:{err_line_no}.\n"{err_info}"\nTraceback:{error_tb}'
    return error_mssg


class CustomExceptionHandling(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_mssg_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
