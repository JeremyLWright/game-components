import ICommand

class CommandFactory():
    def __init__(self, agent):
        self.agent = agent

    def GetCommand(self, parser_tokens):
        verb = parser_tokens[0]
        if(verb == "exit"):
            return ICommand.ExitCommand()
        elif(verb ==  "look"):
            return ICommand.AgentLookCommand(self.agent)
        elif(verb == "inventory"):
            return ICommand.AgentListInventory(self.agent)
        noun = parser_tokens[1]
        if(verb == "walk"):
            if(noun == "north"):
                return ICommand.GoNorthCommand(self.agent)
            elif(noun == "south"):
                return ICommand.GoSouthCommand(self.agent)
            elif(noun == "east"):
                return ICommand.GoEastCommand(self.agent)
            elif(noun == "west"):
                return ICommand.GoWestCommand(self.agent)
            else:
                print "Invalid Direction"
        elif(verb == "take"):
            return ICommand.AgentTakeCommand(self.agent, noun)
        elif(verb == "drop"):
            return ICommand.AgentDropCommand(self.agent, noun)
        elif(verb == "open"):
            if(noun == "north"):
                if(parser_tokens[2] == "door"):
                    return ICommand.OpenNorthDoorCommand(self.agent)
            elif(noun == "south"):
                if(parser_tokens[2] == "door"):
                    return ICommand.OpenSouthDoorCommand(self.agent)
            elif(noun == "east"):
                if(parser_tokens[2] == "door"):
                    return ICommand.OpenEastDoorCommand(self.agent)
            elif(noun == "west"):
                if(parser_tokens[2] == "door"):
                    return ICommand.OpenWestDoorCommand(self.agent)
            else:
                print "Invalid Direction"



            
        


