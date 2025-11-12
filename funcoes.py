from openpyxl import workbook, load_workbook

#criar_abas():
def excluir_dados_completos(nomeTabela, nomePg):
    tabela = nomeTabela
    pagina = nomePg
    for linha in pagina.iter_rows(values_only=True):
        pagina.delete_rows(linha)

        
def mes_atual():
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


def verificarAba(tabela, nomeAba):
    if nomeAba in tabela.sheetnames:
        return True
    else:
        tabela.create_sheet(nomeAba)
print(mes_atual())
