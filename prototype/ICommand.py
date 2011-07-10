from sys import exit
class ICommand():
    def Execute(self):
        pass


class GoNorthCommand(ICommand):
    def __init__(self, agent):
        self.agent = agent
    
    def Execute(self):
        self.agent.Go("north")

class GoSouthCommand(ICommand):
    def __init__(self, agent):
        self.agent = agent
    
    def Execute(self):
        self.agent.Go("south")

class GoEastCommand(ICommand):
    def __init__(self, agent):
        self.agent = agent
    
    def Execute(self):
        self.agent.Go("east")

class GoWestCommand(ICommand):
    def __init__(self, agent):
        self.agent = agent
    
    def Execute(self):
        self.agent.Go("west")

class ExitCommand(ICommand):
    def __init__(self):
        pass

    def Execute(self):
        exit()


