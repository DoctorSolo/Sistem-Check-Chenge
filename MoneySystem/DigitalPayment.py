from MoneySystem.DigitalMoney import DigitalMoney

class DigitalPayment:
    def __init__(self, pay: float, PRICE: float) -> None:
        self.pay = pay
        self.PRICE = PRICE
        self.chenge = 0.0
    
    def payment(self):
        if self.checkChenge():
            return self.chenge
        else:
            print("ERRO")
            return self.pay
    
    
    def checkChenge(self):
        
        if self.pay >= self.PRICE:
            self.chenge = (self.pay - self.PRICE)
            DigitalMoney(self.pay - self.chenge)
            return True
        
        return False
            