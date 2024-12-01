from abc import ABC, abstractmethod

class ItemCollection(ABC):
    @abstractmethod
    def get_details(self):
        pass
