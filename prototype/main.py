import sys
sys.path.insert(0,'.')

import Agent
import ICommand
import Parser

j = Agent.Agent("Jeremy")
p = Parser.Parser()
while(True):
    command = p.GetLine(j)
    command.Execute()

