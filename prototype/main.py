import sys
sys.path.insert(0,'.')
import logging
logging.basicConfig(level=logging.DEBUG)
import Agent
import ICommand
import Parser
import Map
from CommandFactory import CommandFactory

gameMap = Map.Map()
j = Agent.Player("Jeremy", gameMap)
f = CommandFactory(j)
i = 0
while(True):
    j.FrameTick(i)
    i = i + 1

