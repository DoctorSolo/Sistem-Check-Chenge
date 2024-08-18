from Product import Product
import PhisicalPayment
from DataSetMoneyConfig import DataSetMoneyConfig

chenge = DataSetMoneyConfig().arrMoneys

client0 = Product()
client1 = Product()

client0.showProduct()

client0.choiseP("Limpeza","Alcool 70")
client1.choiseP("Comida","Queijo queijo")
