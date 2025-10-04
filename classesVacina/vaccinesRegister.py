class Vaccine:

    def __init__(self, code, name,  necessary_doses, qntdStock):
        self.code = code
        self.name = name
        self.necessary_doses = necessary_doses
        self.qntdStock = qntdStock
    
    def __str__(self):
        return f"{{Código: {self.code}, Nome: {self.name}, Doses: {self.necessary_doses}, Estoque: {self.qntdStock}}}"