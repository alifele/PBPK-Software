from baseClass import BaseClass


class AbstractElement(BaseClass):
    def __init__(self, type):
        super().__init__(type)
        self.value = 0
        self.units = ""
        self.constantValue = False
        self.constant = False
        self.boundaryCondition = False