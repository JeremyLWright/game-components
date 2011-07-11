import json
import logging

class Map():
    def __init__(self):
        dat = open("map.json")
        self.rooms = json.load(dat)

    def GetStartingPosition(self):
        return "Meadow"

    def GetDescription(self, room):
        logging.debug("Fetching Description for: "+str(room))        
        return self.rooms[room]["Description"]

    def GetNorthPosition(self, currentPosition):
        if(self.rooms[currentPosition]["North"]["Destination"] == None):
            print "You cannot go that way."
            return currentPosition
        elif(self.rooms[currentPosition]["North"]["Door"] == True):
            print "You have to open the door."
            return currentPosition
        else:
            return self.rooms[currentPosition]["North"]["Destination"]
    
    def GetSouthPosition(self, currentPosition):
        if(self.rooms[currentPosition]["South"]["Destination"] == None):
            print "You cannot go that way."
            return currentPosition
        elif(self.rooms[currentPosition]["South"]["Door"] == True):
            print "You have to open the door."
            return currentPosition
        else:
            return self.rooms[currentPosition]["South"]["Destination"]

    def GetEastPosition(self, currentPosition):
        if(self.rooms[currentPosition]["East"]["Destination"] == None):
            print "You cannot go that way."
            return currentPosition
        elif(self.rooms[currentPosition]["East"]["Door"] == True):
            print "You have to open the door."
            return currentPosition
        else:
            return self.rooms[currentPosition]["East"]["Destination"]

    def GetItems(self, currentPosition):
        return self.rooms[currentPosition]["Items"]
    
    def GetWestPosition(self, currentPosition):
        if(self.rooms[currentPosition]["West"]["Destination"] == None):
            print "You cannot go that way."
            return currentPosition
        elif(self.rooms[currentPosition]["West"]["Door"] == True):
            print "You have to open the door."
            return currentPosition
        else:
            return self.rooms[currentPosition]["West"]["Destination"]

    def TakeItem(self, item, currentPosition):
        items = self.GetItems(currentPosition)
        if item in items:
            self.rooms[currentPosition]["Items"].pop(self.rooms[currentPosition]["Items"].index(item))
            return True
        return False
            
    def DropItem(self, item, currentPosition):
        self.rooms[currentPosition]["Items"].append(item)
        



