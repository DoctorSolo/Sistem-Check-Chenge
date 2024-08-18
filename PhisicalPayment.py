from DataSetMoneyConfig import DataSetMoneyConfig

class PhisicalPayment:
    chenge = DataSetMoneyConfig.getArr()
    
    def __init__(self, value: list, money: list, PRICE: float):
        self.DL_ = value[::-1] # DL is a play money, valores is a list
        
        self.money = money      # client payment
        self.PRICE = PRICE      # Price product

    
    # check chege
    def checkChenge(self, money: list) -> bool:
        money_t = sum(money) # sum all money
        
        # if the total is less than price, return false
        if money_t < self.PRICE:
            return False
        
        # if the total sum is equal to the price
        elif money_t == self.PRICE:
            for i in range(len(self.DL_)):
                self.DL_[i] += money[i]
        
        # Check if there is chenge
        else:
            for i in range(len(self.DL_)):
                cont = 0
                if self.DL_[i] < (money[i] - self.PRICE):
                    cont += 1
                
                if cont > 3:
                    return False
        
        
        # give chenge and receive the money
        for i in range(len(self.DL_)):
            if self.DL_[i] == 0:
                continue
            else:
                self.chenge[i] += self.DL_[i]
                self.DL_[i] -= 1
            
            if sum(self.chenge) == (money_t - self.PRICE):
                self.DL_[i:] += self.money[i:]
                return True