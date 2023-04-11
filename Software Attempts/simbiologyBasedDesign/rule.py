from baseClass import BaseClass

class Rule(BaseClass):
    def __init__(self):
        super().__init__("Rule")
        self.rule = ""
        self.ruleType = ""
        self.active = ""