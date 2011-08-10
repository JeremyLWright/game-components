import sys
sys.path.insert(0,'.')
import logging
#logging.basicConfig(level=logging.DEBUG)
import Agent
import ICommand
import Parser
import Map

gameMap = Map.Map()
Agent.Player("Jeremy", gameMap)
Agent.Player("Lindsey", gameMap)
for npc in range(10):
    Agent.NPC("Grue"+str(npc), gameMap)

currentFrame = 0
while(True):
    gameMap.FrameTick(currentFrame)
    currentFrame = currentFrame + 1
    

