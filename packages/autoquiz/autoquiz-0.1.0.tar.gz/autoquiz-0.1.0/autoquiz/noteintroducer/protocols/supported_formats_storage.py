from abc import ABC,abstractmethod
class SUPPORTEDFORMATSSTORAGE(ABC):
    @abstractmethod
    def get_all(self,storage=None) -> list:
        pass

    @abstractmethod 
    def get_by_name(self,name:str=None) -> dict:
        pass

