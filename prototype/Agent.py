from Map import Map

class Position():
    def __init__(self):
        self.rooms = Map()
        self.position = self.rooms.GetStartingPosition()
        

    def UpdatePosition(self, direction):
        if(direction == "north"):
            self.position = self.rooms.GetNorthPosition(self.position)
        elif(direction == "south"):
            self.position = self.rooms.GetSouthPosition(self.position)
        elif(direction == "east"):
            self.position = self.rooms.GetEastPosition(self.position)
        elif(direction == "west"):
            self.position = self.rooms.GetWestPosition(self.position)
        else:
            print "Invalid Position"

class Agent():
    def __init__(self, name):
        self.name = name
        self.position = Position()

    def Go(self, direction):
        self.position.UpdatePosition(direction)
        print self.position.rooms.rooms[self.position.position]

    def Look(self):
        print self.position.rooms.rooms[self.position.position]



