from abstractElement import AbstractElement

class Species(AbstractElement):
    def __init__(self):
        super().__init__("Species")
        self.initialAmount = 0
        self.intialAmountUnits = 0