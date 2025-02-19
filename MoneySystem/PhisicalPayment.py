from Chenge import Chenge
from Data.DataSetMoneyConfig import arrMoneys


class PhisicalPayment:
    DL_ = Chenge.chenge        # DL is a play money, valores is a list
    returnChenge = arrMoneys.copy()
    
    def __init__(self, money: list, PRICE: float):
        self.money = money      # client payment
        self.PRICE = PRICE      # Price product

    
    def payment(self) -> None:
        if self.checkChenge(self.convertMoney(self.money)):
            c = Chenge(self.DL_)
        else:
            print("Erro")
    
    
    def convertMoney(self, money: list) -> dict:
        libr = arrMoneys.copy()
        for i in range(len(money)):
            for k in list(libr.keys()):
                if k == money[i]:
                    libr[k] += 1
        
        return libr
    
    
    # check chege
    def checkChenge(self, money: dict) -> bool:
        
        money_t = 0
        for k in list(money.keys()):
            money_t += k * money[k] # sum all money
  
        chenge_t = 0
        for k in list(self.DL_.keys()):
            chenge_t += k * self.DL_[k]
        
        chenge = float(money_t - self.PRICE)
        
        if (money_t >= self.PRICE) and (chenge_t >= chenge):
            for k in list(money.keys()):
                self.DL_[k] += money[k]
            
            chenge_t_money = 0
            for k in list(money.keys()):
                for i in range(money[k]):
                    if ((chenge_t_money + k) <= chenge) and (money[k] > 0):
                        self.DL_[k] -= 1
                        self.returnChenge[k] += 1
                        chenge_t_money += k
            
            return True
        return False