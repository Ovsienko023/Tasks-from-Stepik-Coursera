class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path) as text:
                file_text = text.read()
                return file_text
        except FileNotFoundError:
            return ''
