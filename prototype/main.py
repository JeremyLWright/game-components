import sys
sys.path.insert(0,'.')

import Agent
import ICommand

a = Agent.Agent("Jeremy")
go = ICommand.GoNorthCommand(a)
go.Execute()
go = ICommand.GoSouthCommand(a)
go.Execute()
