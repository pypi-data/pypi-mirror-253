from autoquiz.noteintroducer.agents.note_reader_config import FormatExpectedBuilder

class FormatSelector:
    def __init__(self,format_storage=None,
                 note_reader_config=None):
        self._note_reader_config = note_reader_config
        self._load_supported_formats(format_storage=format_storage)

    def get_all_format(self):
        return self._supported_format

    def _load_supported_formats(self,format_storage=None):
        self._supported_format = format_storage.get_all()

    def select_expected_note_format(self,expected:str=None):
        chos_format = FormatExpectedBuilder()
        for form_name,format in self._supported_format.items():
            if form_name==expected:
                chos_format.set_name(form_name)
                chos_format.set_title(format['title'])
                chos_format.set_topic(format['topic'])


        self._note_reader_config.set_expected_note_format(format=chos_format.build())

