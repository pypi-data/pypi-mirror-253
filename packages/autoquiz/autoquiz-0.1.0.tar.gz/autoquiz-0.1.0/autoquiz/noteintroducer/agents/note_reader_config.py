from autoquiz.noteintroducer.protocols.note_reader_config import NOTEREADERCONFIG

class FormatExpected:
    def __init__(self,name:str=None,
                 title:str=None,
                 topic:str=None):
        self._name = name
        self._title = title
        self._topic = topic 

    def get_name(self) -> str:
        return self._name

    def get_title(self) -> str:
        return self._title

    def get_topic(self) -> str:
        return self._topic

class NoteReaderConfig(NOTEREADERCONFIG):
    def __init__(self):
        self._format = None

    def load_config(self):
        return self._format

    def set_expected_note_format(self,format:FormatExpected=None):
        self._format = format


class FormatExpectedBuilder:
    def __init__(self):
        self._name:str = None
        self._title:str = None
        self._topic:str = None

    def set_name(self,name):
        self._name = name 
        return self

    def set_title(self,title):
        self._title = title
        return self

    def set_topic(self,topic):
        self._topic = topic
        return self

    def build(self):
        return FormatExpected(name=self._name,
                              title=self._title,
                              topic=self._topic)
