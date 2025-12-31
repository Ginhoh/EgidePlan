#VERSÃO APENAS PARA TERMINAL


from openpyxl import load_workbook
from datetime import date
from funcoes import *
from time import sleep

tabela = load_workbook('total_de_gastos.xlsx')
main_page = tabela[actual_month()]


verify_sheet(tabela, actual_month())


while True:
    escolha = int(input('''Escolha uma opção: 
    [1] Ver total de gastos
    [2] Adicionar gastos
                        
    -> '''))
    if escolha == 1 or escolha == 2 or escolha == 3:
        break
    print('Comando não reconhecido, insira um comando válido')

if escolha == 1:
    valores = 0 
    for linha in range(2, main_page.max_row+1):
        sleep(0.5)
        valorA = main_page[f'A{linha}'].value
        valorB = main_page[f'B{linha}'].value
        valorC = main_page[f'C{linha}'].value
        valorD = main_page[f'D{linha}'].value
        print(f'{valorA}: R${valorB} ({valorC}) {valorD}')
        num = float(valorB)
        valores += num
    print(f'\n\n\nValor gasto total: R${valores:.2f}')
    

if escolha == 2:
    try:
        lastCell = main_page.max_row + 1

        descricao = input('Título do Gasto: ')
        main_page[f'A{lastCell}'].value = descricao
        real = input('Valor (Utilize . para as casas decimais.): R$')
        main_page[f'B{lastCell}'].value = real
        criterio = input('Grau de importância: ')
        main_page[f'C{lastCell}'].value = criterio
        today = date.today().strftime('%d/%m/%Y')
        main_page[f'D{lastCell}'].value = today
    except ValueError or IndexError or KeyError:
        print('Houve um erro no envio das informações. Revise o que foi pedido e tente novamente.')
    finally:
        print('Item adicionado com sucesso!')


if escolha == 3:
    print(tabela.sheetnames)


tabela.save('total_de_gastos.xlsx')
