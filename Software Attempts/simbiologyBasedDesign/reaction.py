from baseClass import BaseClass

class Reaction(BaseClass):
    def __init__(self):
        super().__init__("Reaction")
        self.reaction = ""
        self.reactants = []
        self.products = []
        self.stoichiometry = []
        self.reactionRate = ""
        self.kineticLaw = ""
        self.active = True
        self.reversible = True
