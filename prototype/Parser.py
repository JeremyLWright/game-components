import ICommand

class Parser():
    def __init__(self):
        self.verbs = ("walk","take","lick","touch","look",)
        self.directions = ("north", "south", "east", "west",)

    def GetLine(self):
        line = raw_input("?> ")
        items = line.split()
        return items
