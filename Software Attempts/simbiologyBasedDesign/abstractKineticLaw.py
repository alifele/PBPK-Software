from baseClass import BaseClass

class AbstractKineticLaw(BaseClass):
    def __init__(self):
        super().__init__("AbstractKineticLaw")
        self.expression = ""
        self.parameterVariables = []
        self.speciesVariables = []

