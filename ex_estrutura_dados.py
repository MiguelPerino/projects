from unidecode import unidecode

def cumprimentar(nome):
    print(f'Olá, {nome}! Seja bem vindo!')

def dobro(num):
    resultado = num * 2
    return resultado

def media_notas():
    contador = 1
    notas = []
    
    while True:
        try:
            nota = float(input(f'Informe a {contador}° nota (ou digite 0 para finalizar): '))
            contador += 1

            if nota == 0:
                break

            if nota < 0 or nota > 10:
                print('sexo2')
                continue
            notas.append(nota)

        except ValueError:
            print('sexo')
        
    if notas:
        soma = 0
        for i in range(len(notas)):
            soma += notas[i]

        return soma / len(notas)
    else: 
        return 0

def contar_vogais(string):
    cont = 0
    vogais = ['a','e','i','o','u']

    for i in range(len(string)):
        if string[i] in vogais:
            cont += 1
    return cont

def substituir_negativos(lista: list):
    nova_lista = []
    nova_lista.append(substituir_negativos)

    for valor in substituir_negativos:
        if valor < 0:
            valor = 0
        nova_lista.append(valor)
    return nova_lista


nomes = cumprimentar('euclides')
num_dobrado = dobro(int(input('Informe um número para ser dobrado: ')))
media_total = media_notas()
qntd_vogais = contar_vogais(unidecode('programação'))
print(f'Número dobrado: {num_dobrado}')
print(f'Média total: {media_total}')
print(f'Quantidade de vogais: {qntd_vogais}')
