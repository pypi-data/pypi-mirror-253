from abc import ABC,abstractmethod
class NOTEREADERCONFIG(ABC):

    @abstractmethod
    def load_config(self):
        self._value =True
        return self._format

    @abstractmethod
    def set_expected_note_format(self,format=None):
        self._format = format


