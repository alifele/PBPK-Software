from baseClass import BaseClass

class Model(BaseClass):
    def __init__(self):
        super().__init__("Model")
        self.Compartments = []
        self.Species = []
        self.Parameters = []
        self.Rules = []
        self.Events = []
        self.Observables = []
        self.Reactions = []










if __name__ == "__main__":
    model = Model()
    print(model.type)


