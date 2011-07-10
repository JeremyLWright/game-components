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

    def OutputPosition(self, position):
        print position.rooms.GetDescription(position.position)

    def Go(self, direction):
        self.position.UpdatePosition(direction)
        self.OutputPosition(self.position)

    def Look(self):
        self.OutputPosition(self.position)



