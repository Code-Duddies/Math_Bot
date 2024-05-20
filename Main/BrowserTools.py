#Extrenal imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException


# STL imports
import time

# Custom imports
from Main.AbstractTool import AbstractTool


#Base browser tools
class BrowserTools(AbstractTool):
    
    def __init__(self, passedLogger):
        super().__init__()
        self.logger = passedLogger
        self.logger.info_call('BrowserTools object created')
        self.driver = self.establish_driver()
        self.job_urls = []
        
    def __del__(self):
        self.logger.info_call('Browser Tools object deleted')
        
    def establish_driver(self):
        '''Creates a driver instance'''
        try:
            self.logger.info_call('EstablishDriver called')
            
            driver = webdriver.Firefox(options = self.driver_options())
            driver.set_page_load_timeout(120)  # Set a 120-second timeout for page loads
            #driver.maximize_window()
            
            return driver
        
        except WebDriverException as ex:
            errorReport = f"Error in BrowserTools.EstablishDriver: {ex}"
            self.logger.error_call(errorReport)
            
    def driver_options(self):
        '''Creates an options object and adds arguments to it'''
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        #options.add_argument("--headless")  # Run in headless mode
        
        return options
    
    def tab_test(self, passed_handle):
        try:
            time.sleep(.2)
            # Get a list of all window handles
            window_handles = self.driver.window_handles
            
            # Tests for multiple open tabs
            if len(window_handles) > 1:
                # Get the window handle of the new tab
                new_window_handle = window_handles[-1]

                # Close the new tab
                self.driver.switch_to.window(new_window_handle)
                time.sleep(.5)
                self.driver.close()
                
                # Return to orginal tab
                self.driver.switch_to.window(passed_handle)
                time.sleep(.2)
                
                return False
                
            else:
                return True
                
        except ValueError as ve:
            errorReport = f'Error in linkedinbrowsertools.tab_test: {ve}'
            self.logger.error_call(errorReport)
    
    def get_driver(self):
        '''Returns a reference to the instance webdriver'''
        return self.driver
    
    def kill_driver(self):
        '''Quits driver'''
        self.driver.quit()
        
    def get_logger(self):
        '''Returns a reference to instance loggercalls object'''
        return self.logger