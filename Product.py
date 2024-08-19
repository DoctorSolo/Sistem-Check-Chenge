class Product:
    dictProduct = {
        "Limpeza": {"Alcool 70"     : 20.00, 
                    "Agua Sanitaria": 30.00,
                    "Pano Panda"    : 50.00},
        
        "Comida": {"Pão"            : 0.50,
                   "Queijo queijo"  : 50.00,
                   "Peixe Pirata"   : 30.50,
                   "Frango"         : 35.00}
    }
    
    
    def __init__(self) -> None:
        pass
    
    
    def showProduct(self):
        print(self.dictProduct)
    
    
    def choiseP(self, category, product):
        print(self.dictProduct[category][product])
        return self.dictProduct[category][product]
    