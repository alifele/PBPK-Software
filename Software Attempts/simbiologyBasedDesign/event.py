from baseClass import BaseClass

class Even(BaseClass):
    def __init__(self):
        super().__init__("Event")
        self.trigger = None
        self.eventFunction = None
        self.active = False