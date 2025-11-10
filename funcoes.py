from openpyxl import workbook, load_workbook

#criar_abas():
def excluir_dados_completos(nomeTabela, nomePg):
    tabela = nomeTabela
    pagina = nomePg
    for linha in pagina.iter_rows(values_only=True):
        pagina.delete_rows(linha)

        
