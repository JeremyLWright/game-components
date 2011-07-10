import json

class Map():
    def __init__(self):
        dat = open("map.json")
        self.rooms = json.load(dat)

    def GetStartingPosition(self):
        return "Other Room"

    def GetNorthPosition(self, currentPosition):
        if(currentPosition == "Crazy Room"):
            return "Nasty Room"
        if(currentPosition == "Nasty Room"):
            return "Nasty Room"
        if(currentPosition == "Other Room"):
            return "Nasty Room"

    def GetSouthPosition(self, currentPosition):
        if(currentPosition == "Crazy Room"):
            return "Other Room"
        if(currentPosition == "Nasty Room"):
            return "Crazy Room"
        if(currentPosition == "Other Room"):
            return "Nasty Room"

    def GetEastPosition(self, currentPosition):
        if(currentPosition == "Crazy Room"):
            return "Nasty Room"
        if(currentPosition == "Nasty Room"):
            return "Other Room"
        if(currentPosition == "Other Room"):
            return "Crazy Room"
    
    def GetWestPosition(self, currentPosition):
        if(currentPosition == "Crazy Room"):
            return "Other Room"
        if(currentPosition == "Nasty Room"):
            return "Other Room"
        if(currentPosition == "Other Room"):
            return "Crazy Room"



