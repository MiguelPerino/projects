from classes.Lanchonete import Lanchonete
from classes.client import Client
from classes.product import Product
from classes.sales import Sales

restaurant_name = Lanchonete(input('Digite o nome do restaurante: '))

while True:
    try:
        quantity = int(input('Digite a quantidade de clientes que deseja cadastrar: '))
        if quantity > 0:
            break
        else:
            print('Coloque uma quantidade válida, seu jumento.')

    except ValueError:
        print(f'Entrada incompatível, tente novamente...')

clients = []
for i in range(quantity):
    client = Client(input(f'Nome do {i+1}° cliente: '))
    products = []
    j = 1

    catalog = {}
    while True:
        
        product_name = input(f'Produto {j} (ou digite "sair" para não adicionar mais pedidos): ')
        if product_name.lower() == "sair":
            break 
        
        # if product_name in catalog:
        #     #se o nome ja tiver cadastrado nao pede valor
        #     catalog[product_name] = product

        try:
            product_price = float(input('Digite o preço do produto: '))

        except ValueError:
            print('Entrada incompatível, tente novamente...')
            continue

        product = Product(product_name, product_price)       
        products.append(product)
        j += 1
    
    date = input('Informe a data(dd/mm/aaaa): ')
    sale = Sales(client, date, products)
    restaurant_name.add_sale(sale)


restaurant_name.displaySales()
