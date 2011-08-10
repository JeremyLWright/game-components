import json
import logging

class LockedDoorException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class ClosedDoorException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
    

class Map():
    def __init__(self):
        dat = open("map.json")
        self.rooms = json.load(dat)
        self.agents = {}

    def register(self, agent):
        self.agents[agent] = self.GetStartingPosition()

    def FrameTick(self, frame):
        for agent in self.agents:
            agent.FrameTick(frame)

    def GetStartingPosition(self):
        return "Meadow"

    def OpenDoor(self, agent, direction):
        agentsPosition = self.agents[agent]
        if(self.rooms[agentsPosition][direction]["Door"] == True):
            self.rooms[agentsPosition][direction]["Door"] = False
        elif(self.rooms[agentsPosition][direction]["Door"] == False):
            raise ClosedDoorException("You must open the door.")
        else:
            agent.view.ReceiveMsg("There is no Door")

    def DEBUG_WHERE(self, agent):
        for aagent in self.agents:
            agent.view.ReceiveMsg(str(aagent.name+": "+self.agents[aagent]))

    def GetDescription(self, agent):
        logging.debug("Fetching Description for: "+str(agent))        
        position = self.agents[agent]
        for npc in self.agents.keys():
            if npc == agent:
                pass
            elif self.agents[npc] == position:
                agent.view.ReceiveMsg("There is another player, "+npc.name)

        return self.rooms[position]["Description"]

    def UpdatePosition(self, agent, direction):
        agentsPosition = self.agents[agent]
        if(self.rooms[agentsPosition][direction]["Destination"] == None):
            agent.view.ReceiveMsg("You cannot go that way.")
            return agentsPosition
        elif(self.rooms[agentsPosition][direction]["Door"] == True):
            agent.view.ReceiveMsg("You have to open the door")
            return agentsPosition
        else:
            self.agents[agent] = self.rooms[agentsPosition][direction]["Destination"]
            return self.agents[agent]

    def GetItems(self, currentPosition):
        return self.rooms[currentPosition]["Items"]
    
    def TakeItem(self, item, agent):
        agentsPosition = self.agents[agent]
        items = self.GetItems(agentsPosition)
        if item in items:
            self.rooms[agentsPosition]["Items"].pop(self.rooms[agentsPosition]["Items"].index(item))
            return True
        return False
            
    def DropItem(self, item, currentPosition):
        self.rooms[currentPosition]["Items"].append(item)
        



