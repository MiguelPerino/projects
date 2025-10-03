from a import Fila


def showMenu():
    print('1 - Adicionar pessoas convencionais')
    print('2 - Adicionar pessoas na fila preferêncial')
    print('3 - Atender pessoas')
    print('4 - Quantidade pessoas fila')
    print('5 - mostrar fila')
    print('6 - Sair')

def entrarFila(fila):
    name = input('Digite o nome do cliente: ')
    fila.enqueue(name)
    print(f'{name} entou na fila!')

def atenderPessoa(fila):
    if not fila.isEmpty():
        print(f'A pessoa atendida: {fila.dequeue()}')
    else:
        print('A lista está vazia!')
def qntdPessoasFila(fila):
    print(f'Há {fila.size()}')

def showFila(fila):
    print(fila)

if __name__ == '__main__':
    fila_conv = Fila()
    fila_pref = Fila()
    while True:
        showMenu()
        option = int(input('Digite uma opção: '))

        match option:
            case 1:
                entrarFila(fila_conv)
            case 2:
                entrarFila(fila_pref)    
            case 2:
                atenderPessoa(fila_conv)
            case 3:
                qntdPessoasFila(fila_conv)
            case 4:
                showFila(fila_conv)
            case 5:
                print('Encerrando')
                break
