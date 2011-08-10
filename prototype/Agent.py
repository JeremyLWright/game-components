import random
import logging
from Map import Map, ClosedDoorException, LockedDoorException
from Parser import  Parser
from CommandFactory import CommandFactory

class Inventory(object):
    def __init__(self):
        self.items = []

    def GetItems(self):
        return self.items

    def AddItem(self, item):
        self.items.append(item)

    def DropItem(self, item):
        self.items.pop(self.items.index(item))

class AgentView(object):
    def ReceiveMsg(self, message):
        pass

class PlayerView(object):
    def ReceiveMsg(self, message):
        print message

class NPCView(object):
    def ReceiveMsg(self, message):
        pass


class Agent(object):
    def __init__(self, name, map):
        self.name = name
        self.position = map.GetStartingPosition()
        self.inventory = Inventory()
        self.map = map;
        self.map.register(self)

    def OutputPosition(self):
        self.view.ReceiveMsg(self.map.GetDescription(self))
        self.view.ReceiveMsg( "This room has the following Items:")
        for item in self.map.GetItems(self.position):
            self.view.ReceiveMsg(item)
            
    def Go(self, direction):
        self.map.UpdatePosition(self, direction)
        self.OutputPosition()

    def TakeItem(self, item):
        if(self.map.TakeItem(item, self)):
            self.inventory.AddItem(item)
        else:
            self.view.ReceiveMsg("You cannot take that item.")

    def DropItem(self, item):
        self.inventory.DropItem(item)
        self.position.rooms.DropItem(item, self.position.position)

    def Look(self):
        self.OutputPosition()

    def FrameTick(self, frame):
        pass

    def ListInventory(self):
        for item in self.inventory.items:
            self.view.ReceiveMsg(item)
  

class CommandException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Player(Agent):
    def __init__(self, name, map):
        Agent.__init__(self,name, map)
        self.parser = Parser(self)
        self.view = PlayerView()

    def ParseTokens(self, tokens):
        verb = tokens[0].upper()
        if(verb in "EXIT"):
            return exit()
        elif(verb in  "LOOK"):
            return self.Look()
        elif(verb in "INVENTORY"):
            return self.ListInventory()
        elif(verb in "DEBUG_WHERE"):
            return self.map.DEBUG_WHERE(self)
        elif(verb in ("HELP",)):
            helpText = """Available Commands:
exit, look, inventory, walk, go, take, drop, open door"""
            self.view.ReceiveMsg(helpText)
            return
        noun = tokens[1].title()
        if(verb in ("WALK", "GO")):
            return self.Go(noun)  
        elif(verb == "TAKE"):
            return self.TakeItem(noun)
        elif(verb == "DROP"):
            return self.DropItem(noun)
        elif(verb == "OPEN"):
            self.map.OpenDoor(self, tokens[2].upper())
        else:
            raise CommandException("Tokens are unparsable: "+repr(tokens))

    def FrameTick(self, frame):
        try:
            self.ParseTokens(self.parser.GetLine(frame))
        except(CommandException, KeyError, IndexError):
            self.view.ReceiveMsg( "I did not understand.")
        except(ClosedDoorException):
            self.view.ReceiveMsg( "You must open the door.")

class NPC(Agent):
    def __init__(self, name, map):
        Agent.__init__(self, name, map)
        self.view = NPCView()

    def FrameTick(self, frame):
        directions = ("NORTH", "SOUTH", "EAST", "WEST",)
        direction = random.choice(directions)
        logging.debug("Moving "+self.name+" "+direction)
        try:
            self.Go(direction)
        except(ClosedDoorException):
            self.map.OpenDoor(self, direction)
            self.Go(direction)





