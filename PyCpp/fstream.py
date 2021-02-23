class ofstream:
    def __init__(self, fileName:str) -> None:
        self.file = fileName

    def __lshift__(self, other:str) -> None:
        open(self.file, "w+").write(other)
    
    def close() -> None:
        self.file = None

class ifstream:
    def __init__(self, fileName:str) -> None:
        self.file = fileName
    
def getline(ifstream):
    return open(ifstream.file).readlines()