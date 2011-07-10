class Parser():
    def __init__(self):
        self.verbs = ("walk","take","lick","touch","look",)
        self.directions = ("north", "south", "east", "west",)

    def GetLine(self, agent):
        line = raw_input()
        items = line.split()
        verb = items[0]
        noun = items[1]
        if(verb == "walk"):
            if(noun == "north"):
                GoNorthCommand(agent)
            elif(noun == "south"):
                GoSouthCommand(agent)
            elif(noun == "east"):
                GoEastCommand(agent)
            elif(noun == "west"):
                GoWestCommand(agent)
            else:
                print "Invalid Direction"


