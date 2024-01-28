import os 
class NoteReader:
    def __init__(self,config=None):
        self._config = config.load_config()

    def get_config(self):
        return self._config

    def read_note(self,path:str=None) -> str:
        lines:list = None
        with open(path, mode='r') as f:
            lines = f.readlines()
        return lines
        
