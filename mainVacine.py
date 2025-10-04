from classesVacina.vaccinesRegister import Vaccine
from classesVacina.pacientsRegister import Pacients
from classesVacina.aplicationsRegister import Applications


def showMenu():
        print('1 - Cadastrar vacina no estoque')
        print('2 - Cadastrar paciente')
        print('3 - Registrar aplicação de vacina')
        print('4 - Listar vacinas')
        print('5 - Listar pacientes')
        print('6 - Listar aplicações')
        print('7 - Mostrar pacientes com vacinação incompleta')
        print('8 - Mostrar vacinas com estoque baixo')
        print('0 - Sair')

vaccines = []
def registerVaccine():
    while True:
        try:
            code = int(input('Informe o código da vacina: '))
            name = input('Nome da vacina: ')
            doses = int(input('Quantidade de doses necessárias: '))
            stock = int(input(f'Quantidade de estoque: '))

            print(f'\n\033[0;32mVacina cadastrada com sucesso\033[0m!')
            print()

            vaccine = Vaccine(code, name, doses, stock)
            vaccines.append(vaccine)
            break
        except ValueError:
            print(f'\nErro: apenas números inteiros\n')
            continue

pacients = []
def registerPacient():
    while True:
        try:
            code = int(input('Digite o código do paciente: '))
            name = input('Digite o nome do paciente: ')
            age = int(input('Digite a idade: '))

            print(f'\n\033[0;32mPaciente cadastrado com sucesso\033[0m!')
            print()
            pacient = Pacients(code, name, age)
            pacients.append(pacient)
            break
        except ValueError:
            print('\nErro: apenas números inteiros.\n')
            continue

applications = []
def registerApplications(list_pacients, list_vaccines):
    while True:
        try:
            pacient_code = int(input('Informe o código do usuário: '))
            vaccine_code = int(input('Informe o código da vacina: '))
            applied_dose = int(input('Informe a dose aplicada: '))
            break
        except ValueError:
            print('Erro: apenas números inteiros.')
            continue
    
    pacient_found = None
    for p in list_pacients:
        if p.code == pacient_code:
            pacient_found = p
            break
    if not pacient_found:
        print(f'Paciente com o código "{pacient_code}", não encontrado.')

    vaccine_found = None
    for v in list_vaccines:
        if v.code == vaccine_code:
            vaccine_found = v
            break
    if not vaccine_found:
        print(f'A vacina com o código {vaccine_code} não foi encontrada')
        return
    if vaccine_found.qntdStock <= 0:
        print(f'O estoque da vacina de {vaccine_found.name} está vazia')
        add_more_stock = input('\nDeseja adicionar mais estoque (s/n)? ').lower()
        if add_more_stock == 's' or add_more_stock == 'sim':
            while True:
                try:
                    vaccine_found.qntdStock = int(input('Informe a quantidade de estoque: '))
                    break
                except ValueError:
                    print('Valor inválido para estoque.')
                    continue
        else:
            print('\nVoltando ao Menu principal')
            return 

    vaccine_found.qntdStock -= 1
    
    aplication = Applications(pacient_code, vaccine_code, applied_dose)
    applications.append(aplication)
    print(f'\n\033[0;32mAplicação registrada com sucesso!\033[0m')

def showLowerStock(list_vaccines):
    if vaccines:
        print('Lista das vacinas com estoque baixo: ')
        for v in list_vaccines:
            if v.qntdStock < 5:
                print(v)
        input('Pressione Enter para voltar ao Menu Principal')
    else:
        print('Não há nenhuma vacina cadastrada')

def incomplete_vaccines(list_applications, list_vaccines, list_pacients):
    if not list_applications:
        print('\nNenhuma aplicação foi feita, todos os pacientes estão com vacinação incompleta\n')
        return

    print('\nPacientes com vacinação incompleta:\n')
    found = False
    for p in list_pacients:
        for v in list_vaccines:
            doses_taken = sum(1 for a in list_applications if a.pacient == p.code and a.vaccine == v.code)

            if doses_taken < v.necessary_doses:
                print(f'Paciente: {p.name}, Código: {p.code} - Vacina: {v.name}, Doses tomadas: {doses_taken}/{v.necessary_doses}')
                found = True
    
    if not found:
        print('\nTodos os pacientes já tomaram todas as doses.\n')

    # doses_por_paciente = {}
    # for app in list_applications:
    #     chave = (app.pacient, app.vaccine)  # (paciente, vacina)
    #     doses_por_paciente[chave] = doses_por_paciente.get(chave, 0) + 1
    
    # print('\nPacientes com vacinação incompleta:\n')
    # for p in list_pacients:
    #     for v in list_vaccines:
    #         doses_tomadas = doses_por_paciente.get((p.code, v.code), 0)
    #         if doses_tomadas < v.necessary_doses:
    #             print(f'Paciente: {p.name}, Código: {p.code} - Vacina: {v.name}, Doses tomadas: {doses_tomadas}/{v.necessary_doses}')



if __name__ == '__main__':
    while True:
        showMenu()
        try:
            option = int(input('Digite a opção: '))
            if option < 0 or option > 8:
                print('\nNenhuma opção corresponde ao número digitado.\n')
                continue
        except  ValueError:
            print(f'\nEntrada incompatível, tente novamente...\n')
            continue

        match option:
            case 1:
                registerVaccine()
            case 2:
                registerPacient()
            case 3:
                registerApplications(pacients, vaccines)
            case 4:
                if vaccines:
                    print('\nLista de todas as vacinas:')
                    for v in vaccines:
                        print(v)
                    input('\nPressione Enter para voltar ao Menu Principal')
                else:
                    print('\n\033[1;31mNenhuma vacina foi cadastrada ainda\033[0m.\n')

            case 5:
                if pacients:
                    print('\nLista de todos os pacientes:')
                    for p in pacients:
                        print(p)
                    input('\nPressione Enter para voltar ao Menu Principal')
                else:
                    print('\n\033[1;31mNenhum paciente foi cadastrado ainda\033[0m.\n')

            case 6:
                if applications:
                    print('Listar aplicações:')
                    for a in applications:
                        print(a)
                    input('\nPressione Enter para voltar ao Menu Principal')
                else:
                    print('\n\033[1;31mNenhuma aplicação foi registrada ainda\033[0m.\n')
            case 7:
                incomplete_vaccines(applications, vaccines, pacients)
            case 8:
                showLowerStock(vaccines)
            case 0:
                print('Encerrando...')
                break