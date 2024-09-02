

class FileException(Exception):
    def __init__(self, extension):
        self.extension = extension
    
    def __str__(self):
        return f"[System] The {self.extension} extension is not available."

class BoardException(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return f"[System] {self.msg}"