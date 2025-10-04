class Sales:
    def __init__(self, client, date, products, ):
        self.client = client
        self.date = date
        self.products = products
        self.total = sum(p.price for p in products)
    
    def __str__(self):
        products_name = ', '.join(p.name for p in self.products)
        
        return f'Venda de {self.client} em {self.date} - Products: {products_name} | Total: {self.total:.2f}'
        
