class SimulationParameters:
    def __init__(self, name):
        self.name = name
        self.valuesByNames = {}
    def setParam(self, name, value):
        self.valuesByNames[name] = value
