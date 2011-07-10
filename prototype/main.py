import sys
sys.path.insert(0,'.')
import logging
logging.basicConfig(level=logging.DEBUG)
import Agent
import ICommand
import Parser
from CommandFactory import CommandFactory

j = Agent.Agent("Jeremy")
p = Parser.Parser()
f = CommandFactory(j)
while(True):
    tokens = p.GetLine()
    command = f.GetCommand(tokens)
    command.Execute()

