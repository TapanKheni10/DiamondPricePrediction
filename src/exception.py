import sys
import logger_

def error_message_details(error, error_details:sys):
    ## all the information about the error/exception is stored in the 
    ## exc_tb through exc_info() (like in which file, no. of line)
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured it python script name [{0}], line number [{1}], error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    return error_message
    
class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logger_.logging.info("Divide by zero error.")
#         raise CustomException(e, sys)