from models import *
from datetime import date
from funcoes import *
import customtkinter as ctk

#mostrar tabela
def show_table(position):
    #Exibção da tabela principal
    try:
        cont = 1 
        new_frame = ctk.CTkFrame(position, width=600, height=600, fg_color='#F3F4F6', border_width=2, border_color='#E5E7EB').place(x=200)
        scroll_table = ctk.CTkScrollableFrame(new_frame, width=550, height=400, fg_color='#F3F4F6')
        scroll_table.place(x=230,y=50)
        
        labelGastos = ctk.CTkLabel(position, justify='center', width=600, text="Confira seus gastos aqui", font=ctk.CTkFont(size=20, weight="bold"), fg_color='#F3F4F6', text_color='#1E3A8A').place(x=200,y=10)


        cursor.execute(f"""SELECT nome, valor, categoria, data FROM gastos WHERE data LIKE '%/{actual_month()}/%'""")
        query = cursor.fetchall()
        for dados in query:
            valorA, valorB, valorC,valorD = dados
            item_frame = ctk.CTkFrame(scroll_table, fg_color='#F3F4F6')
            item_frame.pack(fill='x', pady=2)
            
            new_label = ctk.CTkLabel(item_frame, wraplength=450, text=f'{cont}. {valorA}: R${valorB:.2f} | {valorC} | {valorD}', font=ctk.CTkFont(size=14, weight="bold"), fg_color='#F3F4F6', text_color='black', justify ='left')
            new_label.pack(side='left', padx=(0, 10))

            btn_remove = ctk.CTkButton(item_frame, command=lambda idc = cont:remove_gasto(position, idc), width=120, text="Excluir",text_color='#0C447C', fg_color=('#E6F1FB'), hover_color='#3B82F6', border_color='#B5D4F4', border_width=2).pack(side='right', padx=10)
        
            cont += 1
            

        btn_add = ctk.CTkButton(position, command=lambda:addGasto(position), width=50,height=50, text="+",text_color='#E6F1FB',font=('Arial',34), fg_color=('#0C447C'), hover_color='#3B82F6', border_color='#B5D4F4', border_width=2, corner_radius=10).place(x=720, y=425)

        
        btn_fixo = ctk.CTkButton(position, command=lambda:gasto_fixo(position), width=140, text="Criar Gasto Fixo",text_color='#0C447C', fg_color=('#E6F1FB'), hover_color='#3B82F6', border_color='#B5D4F4', border_width=2).place(x=205, y=500)

        btn_remove_fixo = ctk.CTkButton(position, command=lambda:remove_gasto_fixo(position), width=140, text="Remover Gasto Fixo",text_color='#0C447C', fg_color=('#E6F1FB'), hover_color='#3B82F6', border_color='#B5D4F4', border_width=2).place(x=355, y=500)

        btn_categ = ctk.CTkButton(position, command=lambda:add_categoria(position), width=140, text="Adicionar Categoria",text_color='#0C447C',fg_color=('#E6F1FB'), hover_color='#3B82F6', border_color='#B5D4F4', border_width=2).place(x=505, y=500)
        
        btn_remove_categ = ctk.CTkButton(position, command=lambda:remove_categoria(position), width=140, text="Remover Categoria",text_color='#0C447C', fg_color=('#E6F1FB'), hover_color='#3B82F6', border_color='#B5D4F4', border_width=2).place(x=655, y=500)
                

    except NameError as e:
        new_label = ctk.CTkLabel(new_frame, text=f'Ops! Não foi possível carregar os dados em nosso sistema\n Por favor, tente novamente!\n{e}', font=ctk.CTkFont(size=12), fg_color='#F3F4F6', text_color='black').place(x=240,y=300)
    finally:   
        pass     
    

#Adicionar gasto
def addGasto(motherWindow):
    #função para enviar os dados para a tabela
    def submitGasto():
        try:
            valor = valorEntry.get().replace(',','.')
            today = date.today().strftime('%d/%m/%Y')
            cursor.execute("""INSERT INTO gastos (nome, valor, categoria, data) VALUES (?, ?, ?, ?)""", (descricaoEntry.get(), float(valor), ctg_select.get(), today))
            db.commit()
            labelInfo = ctk.CTkLabel(AddWindow, text="Gasto adicionado com sucesso!", width=400, justify='center', font=ctk.CTkFont(size=16, weight="bold")).place(y=350)

        except ValueError or IndexError or KeyError:
            print('Houve um erro no envio das informações. Revise o que foi pedido e tente novamente.')
        finally:
            show_table(motherWindow)
            
            AddWindow.destroy()
    
    def submit_gasto_fixo(id):
            cursor.execute("""SELECT nome, valor, categoria FROM fixos WHERE id = ?""", (id,))
            query = cursor.fetchone()
            valorA, valorB, valorC = query

            descricaoEntry.delete(0, 'end')
            valorEntry.delete(0, 'end')

            descricaoEntry.insert(0, valorA)
            valorEntry.insert(0, valorB)
            ctg_select.set(valorC)
            
        
    try:
        AddWindow = ctk.CTkToplevel(motherWindow, fg_color='#F3F4F6')
        AddWindow.geometry("600x400")
        AddWindow.title("Adicionar Gasto")
        AddWindow.resizable(False, False)
        AddWindow.iconbitmap("assents/logo.ico") #Coloca o ícone da aplicação
        AddWindow.transient(motherWindow) # vincula a janela filha à janela mãe
        AddWindow.grab_set()# impede interação com a janela mãe
        AddWindow.lift()# traz a janela para frente

        labelInfo = ctk.CTkLabel(AddWindow, text="Preencha as informações do gasto abaixo:",width=400, justify='center', font=ctk.CTkFont(size=16, weight="bold"), text_color='#1E3A8A').place(x=0,y=20)

        descricao_label = ctk.CTkLabel(AddWindow, text="Nome:", font=ctk.CTkFont(size=12, weight="bold"), fg_color='#F3F4F6', text_color='black').place(x=55,y=60)
        descricaoEntry = ctk.CTkEntry(AddWindow, width=300, placeholder_text="Ex: Almoço",fg_color="#E5E7EB", text_color='#3d3d3d')
        descricaoEntry.place(x=50,y=80)
        
        valor_label = ctk.CTkLabel(AddWindow, text="Valor R$:", font=ctk.CTkFont(size=12, weight="bold"), fg_color='#F3F4F6', text_color='black').place(x=55,y=120)
        valorEntry = ctk.CTkEntry(AddWindow, width=300, placeholder_text="Ex: 50,00",fg_color="#E5E7EB", text_color='#3d3d3d')
        valorEntry.place(x=50,y=140)
        

        cursor.execute("""SELECT nome FROM categoria""")
        dados = cursor.fetchall()

        ctg_select = ctk.CTkOptionMenu(AddWindow, width=300, fg_color="#E5E7EB", dropdown_fg_color='#E5E7EB', dropdown_text_color='black', text_color='#3d3d3d', button_color='#E5E7EB', button_hover_color='#575757',
            values=[dado[0] for dado in dados])
        ctg_select.set("Selecione a categoria")
        ctg_select.place(x=50,y=200)
        
        fixos_label = ctk.CTkLabel(AddWindow, text="Gastos Fixos:",width=150, justify='center', font=ctk.CTkFont(size=14, weight="bold"), fg_color='#F3F4F6', text_color='#1E3A8A').place(x=400,y=50)
        fixos_scroll = ctk.CTkScrollableFrame(AddWindow, width=150, height=250, fg_color='#F3F4F6', border_color='#F3F4F6', border_width=1)
        fixos_scroll.place(x=400,y=70)

            #Criar opções para gastos fixos
        cursor.execute("""SELECT id, nome categoria FROM fixos """)
        query = cursor.fetchall()

        for dados in query:
            valorA, valorB = dados
            btn_fixo = ctk.CTkButton(fixos_scroll, width=150, text=f"{valorB}",text_color='#0C447C',command=lambda id=valorA: submit_gasto_fixo(id), fg_color=('#E6F1FB'), hover_color='#3B82F6', border_color='#B5D4F4', border_width=2)
            btn_fixo.pack(pady=5)
          
 
    except ValueError or IndexError or KeyError:
        print('Houve um erro no envio das informações. Revise o que foi pedido e tente novamente.')


    finally:
        btnSubmit = ctk.CTkButton(AddWindow, command=submitGasto, width=300, text="Enviar Gasto",text_color='#F3F4F6', fg_color=('#1E3A8A'), hover_color='#3B82F6', border_color='black', border_width=2).place(x=50,y=300)


#Remover gasto
def remove_gasto(motherWindow, idc):
    # dialogWindow = ctk.CTkInputDialog(motherWindow,text='Digite qual gasto deseja remover: ', button_fg_color='#1E3A8A', button_hover_color='#3B82F6')
    # dialogWindow.geometry("400x200")
    # dialogWindow.title("Remover Gasto")
    # dialogWindow.iconbitmap("assents/logo.ico") #Coloca o ícone da aplicação
    # value_to_remove = dialogWindow.get_input()

    # if value_to_remove is None:
    #     return
    # value_to_remove = value_to_remove.strip()
    # if value_to_remove == '':
    #     return
    # else:
        cont = 1
        cursor.execute(f"""SELECT nome, valor, categoria, data FROM gastos WHERE data LIKE '%{actual_month()}%'""")
        query = cursor.fetchall()
        for dados in query:
            valorA, valorB, valorC,valorD = dados
             

            if cont == idc:
                cursor.execute("""DELETE FROM gastos WHERE nome = ? AND valor = ? AND categoria = ? AND data = ?""", (valorA, valorB, valorC, valorD))
                db.commit()
            cont += 1
        show_table(motherWindow)


def gasto_fixo(motherWindow):
    def add_fixo():
        try:
            if descricaoEntry.get() == '' or valorEntry.get() == '' or ctg_select.get() == 'Selecione a categoria':

                labelInfo = ctk.CTkLabel(AddWindow, text="Por favor, preencha todas as informações para criar um gasto fixo.", width=400, justify='center', font=ctk.CTkFont(size=16, weight="bold"), text_color='red').place(x=0,y=350)
            else:
                cursor.execute("""INSERT INTO fixos (nome, valor, categoria) VALUES (?, ?, ?)""", (descricaoEntry.get(), float(valorEntry.get().replace(',','.')), ctg_select.get()))
                db.commit()
                labelInfo = ctk.CTkLabel(AddWindow, text="Gasto fixo criado com sucesso!", width=400, justify='center', font=ctk.CTkFont(size=16, weight="bold")).place(x=0,y=350)

        except ValueError or IndexError or KeyError:
            print('Houve um erro no envio das informações. Revise o que foi pedido e tente novamente.')


        finally:
            AddWindow.destroy()
    try:
        AddWindow = ctk.CTkToplevel(motherWindow, fg_color='#F3F4F6')
        AddWindow.geometry("400x400")
        AddWindow.title("Criar Gasto Fixo")
        AddWindow.resizable(False, False)
        AddWindow.iconbitmap("assents/logo.ico") #Coloca o ícone da aplicação
        AddWindow.transient(motherWindow) # vincula a janela filha à janela mãe
        AddWindow.grab_set()# impede interação com a janela mãe
        AddWindow.lift()# traz a janela para frente

        labelInfo = ctk.CTkLabel(AddWindow, text="Preencha as informações do gasto abaixo:",width=400, justify='center', font=ctk.CTkFont(size=16, weight="bold"), text_color='#1E3A8A').place(x=0,y=20)

        descricaoEntry = ctk.CTkEntry(AddWindow, width=300, placeholder_text="Título do Gasto (Max: 20 caracteres)",fg_color="#E5E7EB", text_color='#3d3d3d')
        descricaoEntry.place(x=50,y=80)
        

        valorEntry = ctk.CTkEntry(AddWindow, width=300, placeholder_text="Valor R$:)",fg_color="#E5E7EB", text_color='#3d3d3d')
        valorEntry.place(x=50,y=140)
        

        cursor.execute("""SELECT nome FROM categoria""")
        dados = cursor.fetchall()
        
        ctg_select = ctk.CTkOptionMenu(AddWindow, width=300, fg_color="#E5E7EB", dropdown_fg_color='#E5E7EB', dropdown_text_color='black', text_color='#3d3d3d', button_color='#E5E7EB', button_hover_color='#575757',
            values=[dado[0] for dado in dados])
        ctg_select.set("Selecione a categoria")
        ctg_select.place(x=50,y=200)

    except ValueError or IndexError or KeyError:
        print('Houve um erro no envio das informações. Revise o que foi pedido e tente novamente.')


    finally:

        btnSubmit = ctk.CTkButton(AddWindow, width=150, text="Criar Gasto",text_color='#F3F4F6',command=lambda: add_fixo(), fg_color=('#1E3A8A'), hover_color='#3B82F6', border_color='black', border_width=2).place(x=125,y=300)

def remove_gasto_fixo(motherWindow):
        def delete_fixo(value_to_remove):
            if value_to_remove is None:
                return
            value_to_remove = value_to_remove.strip()
            if value_to_remove == '':
                return
            else:
                cont = 1
                cursor.execute(f"""SELECT  nome, valor, categoria FROM fixos""")
                query = cursor.fetchall()
                for dados in query:
                    valorA, valorB, valorC = dados
                    

                    if cont == int(value_to_remove):
                        cursor.execute("""DELETE FROM fixos WHERE nome = ? AND valor = ? AND categoria = ?""", (valorA, valorB, valorC))
                        db.commit()
                    cont += 1
            show_table(motherWindow)
            windowrf.destroy()

        windowrf = ctk.CTkToplevel(motherWindow, fg_color='#F3F4F6')
        windowrf.geometry("400x400")
        windowrf.title("Criar Gasto Fixo")
        windowrf.resizable(False, False)
        windowrf.iconbitmap("assents/logo.ico") #Coloca o ícone da aplicação
        windowrf.transient(motherWindow) # vincula a janela filha à janela mãe
        windowrf.grab_set()# impede interação com a janela mãe
        windowrf.lift()# traz a janela para frente

        delete_input = ctk.CTkLabel(windowrf, text='Digite o número do gasto fixo que deseja remover:', font=ctk.CTkFont(size=14, weight="bold"), fg_color='#F3F4F6', text_color='#1E3A8A').place(x=20,y=280)
        delete_entry = ctk.CTkEntry(windowrf, width=360, placeholder_text="Ex: 1",fg_color="#E5E7EB", text_color='#3d3d3d')
        delete_entry.place(x=20,y=320)
        btn_delete = ctk.CTkButton(windowrf, command=lambda: delete_fixo(delete_entry.get()), width=360, text="Remover Gasto Fixo", fg_color=('#1E3A8A'), text_color='#F3F4F6', hover_color='#3B82F6', border_color='black', border_width=2).place(x=20,y=350)

        gf_scroll = ctk.CTkScrollableFrame(windowrf, width=380, height=270, fg_color='#F3F4F6', border_color='#F3F4F6', border_width=1)
        gf_scroll.pack()

        cursor.execute(f"""SELECT nome, valor, categoria FROM fixos""")
        query = cursor.fetchall()
        cont = 1
        for dados in query:
            valorA, valorB, valorC = dados
            new_label = ctk.CTkLabel(gf_scroll, text=f'{cont}. {valorA}: R${valorB:.2f} ({valorC})', font=ctk.CTkFont(size=14, weight="bold"), fg_color='#F3F4F6', text_color='#1E3A8A', width=460, anchor='w',)
            new_label.pack(fill='x', pady=5)
            cont += 1

def add_categoria(mother_window):
    dialogWindow = ctk.CTkInputDialog(mother_window,text='Digite o nome da nova categoria: ', button_fg_color='#1E3A8A', button_hover_color='#3B82F6')
    dialogWindow.geometry("400x200")
    dialogWindow.title("Adicionar Categoria")
    dialogWindow.iconbitmap("assents/logo.ico") #Coloca o ícone da aplicação
    value_to_remove = dialogWindow.get_input()

    if value_to_remove is None:
        return
    value_to_remove = value_to_remove.strip()
    if value_to_remove == '':
        return
    else:
        cursor.execute(f"""SELECT nome FROM categoria """)
        query = cursor.fetchall()
        try:
            if value_to_remove not in query:
                cursor.execute("""INSERT INTO categoria (nome) VALUES (?)""", (value_to_remove,))
                db.commit()
   
        finally:
            show_table(mother_window)

def remove_categoria(mother_window):
    def delete_fixo(value_to_remove):
            if value_to_remove is None:
                return
            value_to_remove = value_to_remove.strip()
            if value_to_remove == '':
                return
            else:
                cont = 1
                cursor.execute(f"""SELECT nome FROM categoria""")
                query = cursor.fetchall()

                for dados in query:
                    valorA = dados[0]
                    

                    if cont == int(value_to_remove):
                        cursor.execute("""DELETE FROM categoria WHERE nome = ? """, (valorA,))
                        db.commit()

                    cont += 1

            show_table(mother_window)
            windowrf.destroy()

    windowrf = ctk.CTkToplevel(mother_window, fg_color='#F3F4F6')
    windowrf.geometry("400x400")
    windowrf.title("Criar Gasto Fixo")
    windowrf.resizable(False, False)
    windowrf.iconbitmap("assents/logo.ico") #Coloca o ícone da aplicação
    windowrf.transient(mother_window) # vincula a janela filha à janela mãe
    windowrf.grab_set()# impede interação com a janela mãe
    windowrf.lift()# traz a janela para frente

    delete_input = ctk.CTkLabel(windowrf, text='Digite o número do gasto fixo que deseja remover:', font=ctk.CTkFont(size=14, weight="bold"), fg_color='#F3F4F6', text_color='#1E3A8A').place(x=20,y=280)

    delete_entry = ctk.CTkEntry(windowrf, width=360, placeholder_text="Ex: 1",fg_color="#E5E7EB", text_color='#3d3d3d')
    delete_entry.place(x=20,y=320)

    btn_delete = ctk.CTkButton(windowrf, width=360, command= lambda: delete_fixo(delete_entry.get()),text="Remover Gasto Fixo", fg_color=('#1E3A8A'), text_color='#F3F4F6', hover_color='#3B82F6', border_color='black', border_width=2).place(x=20,y=350)

    gf_scroll = ctk.CTkScrollableFrame(windowrf, width=380, height=270, fg_color='#F3F4F6', border_color='#F3F4F6', border_width=1)
    gf_scroll.pack()

    cursor.execute(f"""SELECT nome FROM categoria""")
    query = cursor.fetchall()
    cont = 1
    for dados in query:
        valorA = dados[0]
        new_label = ctk.CTkLabel(gf_scroll, text=f'{cont}. {valorA}', font=ctk.CTkFont(size=14, weight="bold"), fg_color='#F3F4F6', text_color='black', width=460, anchor='w',)
        new_label.pack(fill='x', pady=5)
        cont += 1