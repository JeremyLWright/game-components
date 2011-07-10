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

class Inventory():
    def __init__(self):
        self.items = []

    def GetItems(self):
        return self.items

    def AddItem(self, item):
        self.items.append(item)

    def DropItem(self, item):
        self.items.pop(self.items.index(item))


class Agent():
    def __init__(self, name):
        self.name = name
        self.position = Position()
        self.inventory = Inventory()

    def OutputPosition(self, position):
        print position.rooms.GetDescription(position.position)
        print "This room has the following Items:"
        for item in self.position.rooms.GetItems(self.position.position):
            print item
            
    def Go(self, direction):
        self.position.UpdatePosition(direction)
        self.OutputPosition(self.position)

    def TakeItem(self, item):
        roomItems = self.position.rooms.GetItems(self.position.position)
        if item in roomItems:
            self.inventory.AddItem(item)
        else:
            print "You cannot take that item."

    def Look(self):
        self.OutputPosition(self.position)

    def ListInventory(self):
        for item in self.inventory.items:
            print item
  



