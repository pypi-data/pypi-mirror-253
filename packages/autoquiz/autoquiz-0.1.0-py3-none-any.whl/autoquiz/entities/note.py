class Note:
    def __init__(self,content:str=None,tags:list=None):
        if content is None or content.rstrip()=="":
            raise VoidContentNoteException()
        self._content = content
        self._tags = tags

    def get_tags(self):
        return self._tags

    def get_content(self):
        return self._content


class VoidContentNoteException(BaseException):
    pass
