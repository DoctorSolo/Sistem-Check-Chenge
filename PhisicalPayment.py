from Chenge import Chenge
from DataSetMoneyConfig import arrMoneys


class PhisicalPayment:
    DL_ = Chenge.chenge        # DL is a play money, valores is a list
    
    def __init__(self, money: list, PRICE: float):
        self.money = money      # client payment
        self.PRICE = PRICE      # Price product

    
    def payment(self) -> None:
        if self.checkChenge(self.convertMoney(self.money)):
            c = Chenge(self.DL_)
        else:
            print("Erro")
    
    
    def convertMoney(self, money: list) -> dict:
        libr = arrMoneys
        for i in range(len(money)):
            for k in list(arrMoneys.keys()):
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
        
              
        # if the total is less than price, return false
        if money_t < self.PRICE:
            return False
        
        # if the total sum is equal to the price
        elif money_t == self.PRICE:
            # for k in list(self.DL_.keys()):
            #     self.DL_[k] += money[k]
            return True
        
        # Check if there is chenge
        elif chenge_t < (money_t - self.PRICE):
            return False
        
        
        
        
        # give chenge and receive the money
        cont_money_c = 0
        for k in list(self.DL_.keys()):
            self.DL_[k] += money[k]
        
        for k in list(self.DL_.keys()):
            if k > self.PRICE:
                continue
            else:
                for i in range(money[k]):
                    if (cont_money_c + (money[k] * i)) > (money_t - self.PRICE):
                        continue
                    else:
                        self.DL_[k] -= 1
                        cont_money_c += (money[k] * i)
                    
                    if cont_money_c == self.PRICE:
                        return True