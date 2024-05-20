from PageTools import PageTools
from StorageClass import DataStorage
from LoggerCalls import LoggerCalls

lc = LoggerCalls()
PT = PageTools(lc)
PT.driver.get(DataStorage.string_dict['lama3_url'])