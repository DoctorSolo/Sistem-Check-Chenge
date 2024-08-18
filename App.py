from Product import Product
from PhisicalPayment import PhisicalPayment
from DataSetMoneyConfig import DataSetMoneyConfig

chenge = DataSetMoneyConfig().getArr()

client0 = Product()
client1 = Product()

client0.showProduct()

pc0 = client0.choiseP("Limpeza","Alcool 70")
pc0PM = [50.00]


pc1 = client1.choiseP("Comida","Queijo queijo")

PhisicalPayment(chenge, pc0PM, pc0)
