from abstractElement import AbstractElement


class Compartment(AbstractElement):
    def __init__(self):
        super().__init__("compartment")
        self.species = []
        self.compartments = []
        self.capacity = 0
        self.capacityUnit = ""
        self.owner = None