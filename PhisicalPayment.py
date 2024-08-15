class PhisicalPayment():
    def __init__(value, money, price):
        self.DL_ = value # DL is a play money, valores is a list
        
        self.money = money
        self.price = price

    
    def checkChenge(self, money, price) -> bool:
        money_t = sum(money)
        if money_t < price:
            return False
        
        elif money_t == price:
            self.DL_ =