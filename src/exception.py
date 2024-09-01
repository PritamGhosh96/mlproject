import sys
import logging
from src.logger import logging

def error_message_detail(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script: \n \
    Name = [{0}] \n \
    Line Number = [{1}] \n \
    Error Message = [{2}]".format(
            file_name,exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details:sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error= error_message, error_details= error_details)

    def __str__(self) -> str:
        return self.error_message
    
# if __name__ == '__main__':

#     try: 
#         a = 1/0
#     except Exception as e:
#         logging.info(CustomException(e,sys))