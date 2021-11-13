class DirectoryMissing(Exception):
    def __init__(self, message):
        self.message = message


class FileMissing(Exception):
    def __init__(self, message):
        self.message = message
