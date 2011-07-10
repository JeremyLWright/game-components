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
        if(self.rooms[currentPosition]["North"] == ""):
            print "You cannot go that way."
            return currentPosition
        else:
            return self.rooms[currentPosition]["North"]
    
    def GetSouthPosition(self, currentPosition):
        if(self.rooms[currentPosition]["South"] == ""):
            print "You cannot go that way."
            return currentPosition
        else:
            return self.rooms[currentPosition]["South"]

    def GetEastPosition(self, currentPosition):
        if(self.rooms[currentPosition]["East"] == ""):
            print "You cannot go that way."
            return currentPosition
        else:
            return self.rooms[currentPosition]["East"]

    def GetItems(self, currentPosition):
        return self.rooms[currentPosition]["Items"]
    
    def GetWestPosition(self, currentPosition):
        if(self.rooms[currentPosition]["West"] == ""):
            print "You cannot go that way."
            return currentPosition
        else:
            return self.rooms[currentPosition]["West"]



