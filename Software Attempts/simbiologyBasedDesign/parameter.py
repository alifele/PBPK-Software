from abstractElement import AbstractElement


class Parameter(AbstractElement):
    def __init__(self):
        super().__init__("Parameter")
        self.valueUnits = ""
