class Product:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
        
    def getProduct(self):
        return (self.name, self.price)
    
    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def __str__(self):
        return f"Name: {self.name} - Price: R${self.price:.2f}"
        
        