from PageTools import PageTools
from StorageClass import DataStorage
from LoggerCalls import LoggerCalls

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

lc = LoggerCalls()
PT = PageTools(lc)
PT.driver.get(DataStorage.string_dict['lama3_url'])
entry_button = PT.wait_and_search(By.XPATH , DataStorage.string_dict['exerience_lama_button'])
entry_button.click()
time.sleep(1)
window_handles = PT.driver.window_handles
new_window_handle = window_handles[-1]
# Switch the new tab
PT.driver.switch_to.window(new_window_handle)
time.sleep(1)
text_area = PT.wait_and_search(By.XPATH, DataStorage.string_dict['text_area'])
text_area.send_keys('tell me something pretty')
time.sleep(1)
text_area.send_keys(Keys.ENTER)