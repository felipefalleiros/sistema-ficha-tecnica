from models.insumos import Insumos
import service.insumo_service as service
from utils.input import ler_int

def mostra_menu():
    print(
        '''
        1 - Cadastrar insumo
        2 - Editar insumo
        3 - Remover insumo
        4 - Visualizar insumos
        5 - Sair
        '''
    )

while True:
    mostra_menu()

    try:
        escolha = int(input('Selecione uma das opções acima: '))
    except ValueError:
        print('Opção inválida')
        continue

    match escolha:

        case 1:
            try:
                nome = input('Nome: ')
                preco = float(input('Preço: '))
                peso = float(input('Peso em gramas: '))

                insumo = Insumos(nome, preco, peso)
                service.cadastrar_insumo(insumo)

                print('Insumo cadastrado com sucesso!')
            except ValueError as e:
                print(f'Erro: {e}')

        case 2:
            try:
                for insumo in service.listar_insumo():
                    print(insumo)

                insumo_id = ler_int('Digite o id do insumo que deseja editar: ')

                novo_preco_input = input('Preço atualizado (Enter para manter): ')
                novo_peso_input = input('Peso atualizado (Enter para manter): ')

                novo_preco = float(novo_preco_input) if novo_preco_input else None
                novo_peso = float(novo_peso_input) if novo_peso_input else None

                service.atualizar_insumo(insumo_id, novo_preco, novo_peso)

                print(service.buscar_por_id(insumo_id))
                print('Insumo atualizado com sucesso!')
            except ValueError as e:
                print(f'Erro: {e}')

        case 3:
            try:
                for insumo in service.listar_insumo():
                    print(insumo)

                insumo_id = ler_int('Digite o id do insumo que deseja deletar: ')
                service.remover_insumo(insumo_id)

                print('Insumo removido com sucesso!')
            except ValueError as e:
                print(f'Erro: {e}')

        case 4:
            for insumo in service.listar_insumo():
                print(insumo)

        case 5:
            break
