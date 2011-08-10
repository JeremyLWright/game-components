import ICommand

class Parser():
    def __init__(self):
        pass
    def __init__(self, owner):
        self.owner = owner

    def GetLine(self, frame):
        line = raw_input("(%s:%d) ?> "%(self.owner.name, frame))
        items = line.split()
        return items
