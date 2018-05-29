class Shipping():
    def __init__(self, strategy):
        self.strategy = strategy
    def calculate(self):
        self.strategy.calculate()
