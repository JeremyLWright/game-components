class Position():
    def __init__(self):
        self.pos = (0,0,)

    def UpdatePosition(self, direction):
        print "Updating position."
        print "Moving %s"%(direction)
        if(direction == "north"):
            self.pos = (self.pos[0], self.pos[1]+1,)
        elif(direction == "south"):
            self.pos = (self.pos[0], self.pos[1]-1,)
        elif(direction == "east"):
            self.pos = (self.pos[0]+1, self.pos[1],)
        elif(direction == "west"):
            self.pos = (self.pos[0]-1, self.pos[1],)
        else:
            print "Invalid Position"

class Agent():
    def __init__(self, name):
        self.name = name
        self.position = Position()

    def Go(self, direction):
        self.position.UpdatePosition(direction)
        print self.name+"'s Updated position: "+str((self.position.pos))


