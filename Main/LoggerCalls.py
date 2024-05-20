from LoggerTools import LoggerTools as LT

class LoggerCalls(LT):
    
    def __init__(self):
        super().__init__()
        self.logger.info('LoggerCalls object created')
        
    def __del__(self):
        self.logger.info('LoggerCalls object deleted')
        
    def info_call(self, passedString):
        self.logger.info(passedString)
            
    def error_call(self, passedString):
        self.logger.error(passedString)
        
    def debug_call(self, passedString):
        self.logger.debug(passedString)