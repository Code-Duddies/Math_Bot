# External modules
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# STL imports
import time

# Custom modules
from Main.BrowserTools import BrowserTools


class PageTools(BrowserTools):
    def __init__(self, passedLogger):
        super().__init__(passedLogger)
        self.logger.info_call('Page Tools object created')
        
    def __del__(self):
        self.logger.info_call('Page Tools object deleted')
        
    def button_clicker(self, passed_by, passed_string):
        self.wait_and_search(passed_by, passed_string).click()
        
    def  text_inputter(self, passed_by, passed_string, passed_info, hit_return=False):
        element = self.wait_and_search(passed_by, passed_string)
        for _ in range(30):
            element.send_keys(Keys.DELETE)
        time.sleep(.5)
        element.send_keys(passed_info)
        if hit_return:
            time.sleep(.25)
            element.send_keys(Keys.RETURN)
            
    def wait_and_search(self, passedBy, passedString, is_single=True):
        """"Waits up to 2 minutes for an element to appear and returns a reference of the element.
            Use only if element's existance is confirmed!!!"""
        try:
            if is_single:
                returnVar = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((passedBy, passedString)))
                return returnVar
            else:
                returnVar = WebDriverWait(self.driver, 120).until(EC.presence_of_all_elements_located((passedBy, passedString)))
                return returnVar
        
        except NoSuchElementException as ve:
            errorReport = f'Error in wait and search {ve}'
            self.logger.error_call(errorReport)
        except TimeoutException as te:
            errorReport = f'Timeout Error in wait and search: {te}'
            self.logger.error_call(errorReport)
            
    def test_for_element(self, passedBy, passedString):
        """Test whether an element exists on the current webpage"""
        try:
            time.sleep(2.5)
            possible_element = self.driver.find_elements(passedBy, passedString)
            
            return possible_element
            
        except NoSuchElementException as ne:
            errorReport = f'Error in browsertools.test_for_element: {ne}'
            self.logger.error_call(errorReport)
            
    def soup_parser(self, passed_source, passed_type):
        '''Uses BeautifulSoup to parse the page source'''
        try:
            return_soup = BeautifulSoup(passed_source, passed_type)
            return return_soup
        
        except ValueError as ve:
            errorReport  = f"Couldn't Parse Page Source: {ve}"
            self.logger.error_call(errorReport)
    
    def soup_search(self, passed_soup, passed_by, passed_search_string):
        '''Uses a BeautifulSoup object to search for a child element by a specific class'''
        
        try:
            return_soup = passed_soup.find(passed_by, class_= passed_search_string)
            return return_soup
        
        except ValueError as ve:
            errorReport =  f'Soup unable to find element: {ve}'
            self.logger.error_call(errorReport)
            
    