#Colocar tabelas referentes ao mês
#DashBoard estatístico
from openpyxl import load_workbook
from datetime import date
from funcoes import *
from time import sleep

tabela = load_workbook('total_de_gastos.xlsx')
main_page = tabela['Sheet']

verificarAba(tabela, mes_atual())


#main_page.delete_rows(10)# - Serve para apagar linhas
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
        print(f'{valorA}: R${valorB} ({valorC})')
        num = float(valorB)
        valores += num
    print(f'\n\n\nValor gasto total: R${valores:.2f}')
    
   # valores += float(lista[cont])
   # print(f'Total de gastos: R${valores:.2f}')

if escolha == 2:
    try:
        ultima_celula = main_page.max_row + 1
        descricao = input('Título do Gasto: ')
        main_page[f'A{ultima_celula}'].value = descricao
        real = input('Valor (Utilize . para as casas decimais.): R$')
        main_page[f'B{ultima_celula}'].value = real
        criterio = input('Grau de importância: ')
        main_page[f'C{ultima_celula}'].value = criterio
        data = date.today().strftime('%d/%m/%Y')
        main_page[f'D{ultima_celula}'].value = data
    except ValueError or IndexError or KeyError:
        print('Houve um erro no envio das informações. Revise o que foi pedido e tente novamente.')
    finally:
        print('Item adicionado com sucesso!')
    #Se salvar com um nome diferente, ele cria um arquivo

if escolha == 3:
    print(tabela.sheetnames)


tabela.save('total_de_gastos.xlsx')
main_page.max_column #Ver o máximo de colunas
main_page.max_row #Ver o máximo de linhas

#main_page['A1'].value é possível exibir e alterar o valor de uma célulam