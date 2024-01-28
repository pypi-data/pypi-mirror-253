class RecieveNoteDTO:
    def __init__(self,content:str=None,tags:list=None):
        if (content,tags) is None:
            raise ValueError()
        self._content = content 
        self._tags = tags

    def get_content(self):
        return self._content

    def get_tags(self):
        return self._tags
