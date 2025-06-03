matriz1 = []


linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))

#Preencher a matriz. (Nessa opção o usuário deverá definir o tamanho da matriz e a popular.
if linhas <= 0 or colunas <= 0:
    print('\nNúmero inválido.')
else:
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input(f'Digite o o valor para linha {i} e coluna {j}: ')))
        matriz1.append(linha)

    print(f"""\nMenu principal: 
{'-'*80}
1 -  Exibir a matriz formatada na tela\n2 -  Mostrar a soma de todos os elementos da matriz\n3 -  Mostrar o maior e o menor elemento da matriz e suas respectivas posições
4 -  Procurar a posição de um número a sua escolha\n5 -  Exibir a matriz transposta\n6 -  Multiplicar a matriz por um fator escalar\n7 -  Multiplicação entre duas matrizes
{'-'*80}""")
    escolha = int(input('Digite a opção desejada: '))
    print()

    if escolha <= 0 or escolha > 7: 
        print('Nenhuma opção encontrada!')
        
        
    #Exibir a matriz formatada na tela (desing de matriz, linha x coluna).
    if escolha == 1:
        for i in range(linhas):
            for j in range(colunas):
                print(f'{matriz1[i][j]:7}', end= '')
            print()


    #Calcular e mostrar a soma de todos os elementos da matriz;
    if escolha == 2:
        soma = 0
        for i in range(linhas):
            for j in range(colunas):
                soma += matriz1[i][j]
        print(f'A soma de todos os elementos da matriz é: {soma:.2f}')


    #Calcular e mostrar o maior e o menor elemento da matriz, e também suas respectivas posições.
    if escolha == 3:
        maior_valor = 0
        menor_valor = matriz1[0][0]
        posicao_maior = (0, 0)
        posicao_menor = (0, 0)
        for i in range(linhas):
            for j in range(colunas):
                if matriz1[i][j] > maior_valor:
                    maior_valor = matriz1[i][j]
                    posicao_maior = (i, j)
                if matriz1[i][j] < menor_valor:
                    menor_valor = matriz1[i][j]
                    posicao_menor = (i, j)

        print(f'O maior valor é: {maior_valor} e a posção é: {posicao_maior}')
        print(f'O menor valor é: {menor_valor} e a posição é: {posicao_menor}')


    #Procurar por um elemento na Matriz. Se encontrar, retornar a posição do mesmo. Caso exista mais de um elemento igual, mostrar as posições de todos.
    if escolha == 4:
        posicao_valor_encontrada = (0, 0)
        elemento_procurado = int(input('Digite o número que você queira encontrar na matriz: '))
        for i in range(linhas):
            for j in range(colunas):
                if matriz1[i][j] == elemento_procurado:
                    posicao_valor_encontrada = (i, j)
                    print(f'A posição dele é: {posicao_valor_encontrada}')


    #Calcular e exibir a matriz transposta (Trocar linhas por colunas). Para a transposição da matriz, crie uma nova matriz e reorganize os elementos.
    if escolha == 5:
        matriz_nova = []
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                linha.append(matriz1[j][i])
            matriz_nova.append(linha)

        print('Matriz transposta: ')
        for i in range(linhas):
            for j in range(colunas):
                print(f'{matriz_nova[i][j]:7}', end = '')
            print()


    #Multiplicar a matriz por um fator escalar. - Multiplique todos os elementos da matriz por esse escalar e mostrar a matriz depois.   
    if escolha == 6:
        escalar = float(input('Digite o fator escalar desejado para multiplicar a matriz: '))
        for i in range(linhas):
            for j in range(colunas):
                escalada = matriz1[i][j] * escalar
                print(f'{escalada:7}', end = '')
            print()


    #Multiplicação entre duas matrizes. Caso o usuário escolha esse opção, 
    # ele deverá popular a segunda matriz e o programa realizar a multiplicação entre a primeira e a segunda matriz. Verificar se é possível realizar a operação.
    matriz_nova = []
    if escolha == 7:
        linhas_nova = int(input('Digite o número de linhas da nova matriz: '))
        colunas_nova = int(input('Digite o número de colunas da nova matriz: '))
        print()
        if linhas_nova <= 0 or colunas_nova <= 0:
            print('Número para matriz inválido!')
        else:
            #AQUI É A CONDIÇÃO DA MULTIPLICAÇÃO DE MATRIZ
            if colunas != linhas_nova:
                print('Multiplicação inválida, o número de linhas da matriz nova precisa ser equivalente ao número de colunas da primeira matriz!')
            else:
                #AQUI VAI PEDIR OS VALORES DA MATRIZ NOVA
                for i in range(linhas_nova):
                    linha = []
                    for j in range(colunas_nova):
                        linha.append(float(input(f'Informe o valor para linha {i} e a coluna {j}: ')))
                    matriz_nova.append(linha)
                print()
                
                #AQUI JA CALCULA A MULTIPLICAÇÃO DA MATRIZ NOVA COM A PRIMEIRA E JA MOSTRA O RESULTADO
                print('O resultado da matriz multiplicada é:')
                for i in range(linhas):
                    for j in range(colunas_nova):
                        produto = 0
                        for k in range(colunas):
                            produto += matriz1[i][k] * matriz_nova[k][j]
                        print(f'{produto:10.2f}', end = '')
                    print()


input('\nPressione Enter para fechar o programa...')
