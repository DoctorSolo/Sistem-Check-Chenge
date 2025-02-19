from Data.DataSetMoneyConfig import arrMoneys

class Chenge:
    chenge = arrMoneys.copy()
    
    def __init__(self, chenge: dict) -> None:
        self.chenge = chenge
        print(chenge)