from openpyxl import workbook, load_workbook
import customtkinter as ctk

#retornar mês atual
def actual_month():
    from datetime import date
    mes = date.today().month
    if mes == 1: return 'Janeiro'
    elif mes == 2: return 'Fevereiro'
    elif mes == 3: return 'Março'
    elif mes == 4: return 'Abril'
    elif mes == 5: return 'Maio'
    elif mes == 6: return 'Junho'
    elif mes == 7: return 'Julho'
    elif mes == 8: return 'Agosto'
    elif mes == 9: return 'Setembro'
    elif mes == 10: return 'Outubro'
    elif mes == 11: return 'Novembro'
    elif mes == 12: return 'Dezembro'


#criar_abas():
def verify_sheet(table, nameAba):
    if nameAba not in table.sheetnames:
        table.create_sheet(nameAba)

        table[nameAba]['A1'].value = 'Descrição'
        table[nameAba]['B1'].value = 'Valor'
        table[nameAba]['C1'].value = 'Tipo de gasto'
        table[nameAba]['D1'].value = 'Data'
    if 'Sheet' in table.sheetnames:
        table.remove(table['Sheet'])
    if 'Plan1' in table.sheetnames:
        table.remove(table['Plan1'])

#verificar se é a primeira aba
def first(tabela):
    cont = 0
    for aba in tabela.sheetnames:
        cont += 1
    if cont == 1:
        return True
    else:
        return False  
    


