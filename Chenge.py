from DataSetMoneyConfig import DataSetMoneyConfig

class Chenge:
    chenge = DataSetMoneyConfig().arrMoneys
    
    def __init__(self, chenge: dict) -> None:
        self.chenge = chenge
        print(self.chenge)