import ICommand

class Parser():
    def __init__(self):
        pass
    def __init__(self, owner):
        self.owner = owner

    def GetLine(self):
        line = raw_input("(%s) ?> "%(self.owner.name))
        items = line.split()
        return items
