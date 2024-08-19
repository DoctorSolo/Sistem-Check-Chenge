class DataSetMoneyConfig:
    
    arrMoneys = {
        100: 0.00,
         50: 0.00,
         20: 0.00,
         10: 0.00,
          5: 0.00,
          2: 0.00,
          1: 0.00,
        0.5: 0.00,
    }
    
    
    def __init__(self) -> None:
        pass
    
    
    def getArr(self) -> list[float]:
        return self.arrMoneys.values