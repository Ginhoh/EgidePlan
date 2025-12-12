from openpyxl import load_workbook
from datetime import date
from funcoes import *
import customtkinter as ctk



tabela = load_workbook('total_de_gastos.xlsx')
verificarAba(tabela, mes_atual())
main_page = tabela[mes_atual()]


def exibir_tabela(position):
    try:
        valores = 0
        cont = 1 
        px = 50
       # scrollabel_frame = ctk.CTkScrollableFrame(position, orientation='vertical').place(x=200)

        new_frame = ctk.CTkFrame(position, width=600, height=600, fg_color='#F3F4F6', border_width=2, border_color='#E5E7EB').place(x=200)
       # table_frame = ctk.CTkScrollableFrame(new_frame, fg_color='#F3F4F6')
        #table_frame.place(x=20, y=60)
        labelGastos = ctk.CTkLabel(new_frame, justify='center', width=600, text="Confira seus gastos aqui", font=ctk.CTkFont(size=20, weight="bold"), fg_color='#F3F4F6', text_color='#1E3A8A').place(x=200,y=10)
        for linha in range(2, main_page.max_row+1):
            valorA = main_page[f'A{linha}'].value
            valorB = float(main_page[f'B{linha}'].value)
            valorC = main_page[f'C{linha}'].value
            valorD = main_page[f'D{linha}'].value
            new_label = ctk.CTkLabel(new_frame, text=f'{cont}. {valorA}: R${valorB:.2f} ({valorC}) {valorD}', font=ctk.CTkFont(size=14, weight="bold"), fg_color='#F3F4F6', text_color='#1E3A8A', width=460, anchor='w').place(x=240,y=px)
            num = float(valorB)
            valores += num
            cont += 1
            px += 30
            btnAdd = ctk.CTkButton(position,command=lambda:addGasto(position), width=150, text="Adicionar Gasto", fg_color=('#3B82F6'),text_color='black', border_color='black', border_width=2).place(x=325,y=500)
            btnRemove = ctk.CTkButton(position,command=lambda:removeGasto(position), width=150, text="Remover Gasto", fg_color=('#3B82F6'),text_color='black', border_color='black', border_width=2).place(x=525,y=500)
    except:
        new_label = ctk.CTkLabel(new_frame, text=f'Ops! Não foi possível carregar os dados em nosso sistema\n Por favor, tente novamente!', font=ctk.CTkFont(size=12), fg_color='#F3F4F6', text_color='black').place(x=240,y=px)
    finally:   
        pass
        
    


def addGasto(motherWindow):
    def submitGasto():
        try:
            lastCell = main_page.max_row + 1
            main_page[f'A{lastCell}'].value = descricaoEntry.get()

            main_page[f'B{lastCell}'].value = valorEntry.get()

            main_page[f'C{lastCell}'].value =  ctg_select.get()

            today = date.today().strftime('%d/%m/%Y')

            main_page[f'D{lastCell}'].value = today
            labelInfo = ctk.CTkLabel(AddWindow, text="Gasto adicionado com sucesso!", width=400, justify='center', font=ctk.CTkFont(size=16, weight="bold")).place(y=350)

        except ValueError or IndexError or KeyError:
            print('Houve um erro no envio das informações. Revise o que foi pedido e tente novamente.')
        finally:
            exibir_tabela(motherWindow)
            tabela.save('total_de_gastos.xlsx')
            AddWindow.destroy()
            
        
    try:
        AddWindow = ctk.CTkToplevel(motherWindow, fg_color='#F3F4F6')
        AddWindow.geometry("400x400")
        AddWindow.title("Adicionar Gasto")
        AddWindow.resizable(False, False)
        AddWindow.iconbitmap("assents/logo.ico") #Coloca o ícone da aplicação
        AddWindow.transient(motherWindow) # vincula a janela filha à janela mãe
        AddWindow.grab_set()# impede interação com a janela mãe
        AddWindow.lift()# traz a janela para frente

        labelInfo = ctk.CTkLabel(AddWindow, text="Preencha as informações do gasto abaixo:",width=400, justify='center', font=ctk.CTkFont(size=16, weight="bold"), text_color='#1E3A8A').place(x=0,y=20)

        descricaoEntry = ctk.CTkEntry(AddWindow, width=300, placeholder_text="Título do Gasto",fg_color="#3d3d3d", text_color='#E5E7EB')
        descricaoEntry.place(x=50,y=80)
        

        valorEntry = ctk.CTkEntry(AddWindow, width=300, placeholder_text="Valor (Utilize . para as casas decimais.)",fg_color="#3d3d3d", text_color='#E5E7EB')
        valorEntry.place(x=50,y=140)
        

        #criterioEntry = ctk.CTkEntry(AddWindow, width=300, placeholder_text="Grau de importância")
        ctg_select = ctk.CTkOptionMenu(AddWindow, width=300,fg_color="#3d3d3d", dropdown_fg_color='#E5E7EB', dropdown_text_color='black', text_color='#E5E7EB', button_color='#3d3d3d', button_hover_color='#575757',
            values=["Essencial", "Lazer", "Investimentos", "Transporte", "Auto Cuidado"])
        ctg_select.set("Selecione a categoria")
        ctg_select.place(x=50,y=200)
        

 
    except ValueError or IndexError or KeyError:
        print('Houve um erro no envio das informações. Revise o que foi pedido e tente novamente.')


    finally:
        btnSubmit = ctk.CTkButton(AddWindow, command=submitGasto, width=150, text="Enviar",text_color='#F3F4F6', fg_color=('#1E3A8A'), hover_color='#3B82F6', border_color='black', border_width=2).place(x=125,y=300)

        
def removeGasto(motherWindow):
    dialogWindow = ctk.CTkInputDialog(motherWindow,text='Digite qual gasto deseja remover: ', button_fg_color='#1E3A8A', button_hover_color='#3B82F6')
    dialogWindow.geometry("400x200")
    dialogWindow.title("Remover Gasto")
    dialogWindow.iconbitmap("assents/logo.ico") #Coloca o ícone da aplicação
    value_to_remove = dialogWindow.get_input()
    if value_to_remove is None:
        return
    value_to_remove = value_to_remove.strip()
    if value_to_remove == '':
        return
    if value_to_remove != '':
        main_page.delete_rows(int(value_to_remove)+1)
        tabela.save('total_de_gastos.xlsx')
        exibir_tabela(motherWindow)
     
#main_page.max_column #Ver o máximo de colunas
#main_page.max_row #Ver o máximo de linhas

#main_page['A1'].value é possível exibir e alterar o valor de uma célulam