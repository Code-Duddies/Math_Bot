#STL import
import logging

#Custom import
from AbstractTool import AbstractTool

#Base Logger tools
class LoggerTools(AbstractTool):

    def __init__(self):
        super().__init__()
        self.logger = self.establish_logger()
        self.logger.info('Logger Tools object created.')
        
    def __del__(self):
        self.logger.info('Logger Tools object deleted')
        
    def establish_logger(self):
        ''' Establishes a logger and passes a handler to the logger '''
        # Create a logger
        logger = logging.getLogger('Logger')
        logger.setLevel(logging.DEBUG)

        # Add the handler to the logger
        logger.addHandler(self.logger_handler())
        
        return logger
    
    def logger_handler(self):
        ''' Establishes a handler and sets format conditions '''
        # Create a console handler
        handler = logging.StreamHandler()

        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        return handler
    
    def get_logger(self):
        return self.logger