class Lanchonete:
    def __init__(self, name):
        self.name = name
        self.sales = []
    
    def add_sale(self, sale):
        self.sales.append(sale)

    def displaySales(self):
        for i, s in enumerate(self.sales, start=1):
            print(f'\nVenda {i}: \n{s}')        