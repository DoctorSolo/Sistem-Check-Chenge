from Product import Product
from PhisicalPayment import PhisicalPayment
from Chenge import Chenge

client0 = Product()
client1 = Product()

client0.showProduct()

pc0 = client0.choiseP("Limpeza","Alcool 70")
pc0PM = [20.00]
PhisicalPayment(Chenge.chenge, pc0PM, pc0).payment()

pc1 = client1.choiseP("Comida","Queijo queijo")

