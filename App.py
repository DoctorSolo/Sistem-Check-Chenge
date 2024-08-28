from Product import Product
from PhisicalPayment import PhisicalPayment
from DigitalPayment import DigitalPayment
from DigitalMoney import DigitalMoney

client0 = Product()
client1 = Product()

loja = Product()

client0.showProduct()

pc0 = client0.choiseP("Limpeza","Alcool 70")
pc0PM = [20.00]
PhisicalPayment(pc0PM, pc0).payment()

pc1 = client1.choiseP("Comida","Queijo queijo")
pc1PM = [10.00,20.00, 20.00]
PhisicalPayment(pc1PM, pc1).payment()

digitalCliente = loja.choiseP("Limpeza", "Pano Panda")
print(DigitalPayment(60, digitalCliente).payment())