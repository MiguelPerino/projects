class Pacients:

    def __init__(self, code, name, age):
        self.code = code
        self.name = name
        self.age = age

    
    def __str__(self):
        return f"Código: {self.code}, Nome: {self.name}, Idade: {self.age}"
    
    
        