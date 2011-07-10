import ICommand

class Parser():
    def __init__(self):
        self.verbs = ("walk","take","lick","touch","look",)
        self.directions = ("north", "south", "east", "west",)

    def GetLine(self, agent):
        line = raw_input("?> ")
        items = line.split()
        verb = items[0]
        if(verb == "exit"):
            return ICommand.ExitCommand()
        noun = items[1]
        if(verb == "walk"):
            if(noun == "north"):
                return ICommand.GoNorthCommand(agent)
            elif(noun == "south"):
                return ICommand.GoSouthCommand(agent)
            elif(noun == "east"):
                return ICommand.GoEastCommand(agent)
            elif(noun == "west"):
                return ICommand.GoWestCommand(agent)
            else:
                print "Invalid Direction"


