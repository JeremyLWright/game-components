import ICommand

class Parser():
    def __init__(self):
        pass

    def GetLine(self):
        line = raw_input("?> ")
        items = line.split()
        return items
