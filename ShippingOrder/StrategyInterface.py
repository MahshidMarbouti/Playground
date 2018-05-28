import abc

class strategy_interface(abc.ABC):
        def __init__(self):
            pass
        @abc.abstractmethod
        def calculate(self):
        
