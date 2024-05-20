from abc import ABC, abstractmethod

#Abstract parent of all tool classes
class AbstractTool(ABC):
    
    @abstractmethod
    def __init__(self, passedLogger=None):
        pass
    
    @abstractmethod
    def __del__(self):
        pass
    
    
#Abstract parsing/sorting tools for each site
class AbstractSortingTools(ABC):
    
    @abstractmethod
    def sort_jobs_urls(self):
        pass
    
    @abstractmethod
    def apply_menu_root(self):
        pass