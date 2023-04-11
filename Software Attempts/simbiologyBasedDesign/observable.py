from baseClass import BaseClass


class Observable(BaseClass):
    def __init__(self):
        super().__init__("Observable")
        self.expression = ""
        self.units = ""
        self.active = ""