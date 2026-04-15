import customtkinter as ctk
from funcoes import *
from models import *

#Função que abre uma nova janela para exibir tabela anterior
            
def show_history(frame):
    new_frame = ctk.CTkFrame(frame, width=600, height=600, fg_color='#F3F4F6', border_width=0)
    new_frame.place(x=200)
    title = ctk.CTkLabel(new_frame, text='Histórico de Gastos', font=ctk.CTkFont(size=20, weight="bold"), fg_color='#F3F4F6', text_color='#1E3A8A')
    title.place(x=200, y=20)

    ctg_select = ctk.CTkOptionMenu(new_frame,command=lambda choice: last_tb(choice, new_frame), width=100,fg_color="#F3F4F6", dropdown_fg_color='#F3F4F6', dropdown_text_color='black', text_color='#3d3d3d', button_color='#F3F4F6', button_hover_color='#575757',
            values= months_())
    ctg_select.set("Selecione o mês")
    ctg_select.place(x=450,y=50)
    

def last_tb(choice, position):
    new_scroll = ctk.CTkScrollableFrame(position, width=550, height=300, fg_color='#F3F4F6')
    new_scroll.place(x=30,y=100)        
    cont = 1
    cursor.execute(f"""SELECT nome, valor, categoria, data FROM gastos
                    WHERE data LIKE '%/{choice_month(choice)}/%'""")
    query = cursor.fetchall()
    for dados in query:
        valorA, valorB, valorC, valorD = dados
        new_label = ctk.CTkLabel(new_scroll, text=f'{cont}. {valorA}: R${valorB:.2f} ({valorC}) {valorD}', font=ctk.CTkFont(size=14, weight="bold"), fg_color='#F3F4F6', text_color='#1E3A8A', width=350, anchor='w')
        new_label.pack(fill='x', pady=5)
        cont += 1

    #bloco1=ctk.CTkFrame(position, width=200, height=100, fg_color="#F3F4F6", border_width=2, border_color="#E5E7EB", bg_color='transparent').place(x=230,y=450)
    label_total = ctk.CTkLabel(position, text=f'TOTAL\nR${gastos_total(choice_month(choice)):,.2f}', font=('Arial',24), text_color='#1E3A8A',width=194, height=94, fg_color='#F3F4F6').place(x=32,y=432)

    label_maior = ctk.CTkLabel(position, text=f'Categoria com maior gasto: {categoria_maior(choice_month(choice))}', font=('Arial',16),width=400,anchor='w', text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=432)

    label_menor = ctk.CTkLabel(position, text=f'Categoria com menor gasto: {categoria_menor(choice_month(choice))}', font=('Arial',16),width=400,anchor='w', text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=462)


    label_essencial = ctk.CTkLabel(position, text=f'Essencial: R${gastos_por_categoria(choice_month(choice), 'Essencial'):,.2f}', font=('Arial',12,'bold'), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=490)

    label_alimentacao = ctk.CTkLabel(position, text=f'Alimentação: R${gastos_por_categoria(choice_month(choice), 'Alimetação'):,.2f}', font=('Arial',12,'bold'), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=440,y=490)

    label_lazer = ctk.CTkLabel(position, text=f'Lazer: R${gastos_por_categoria(choice_month(choice), 'Lazer'):,.2f}', font=('Arial',12,'bold'), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=520)
    label_investimentos = ctk.CTkLabel(position, text=f'Investimentos: R${gastos_por_categoria(choice_month(choice), 'Investimentos'):,.2f}', font=('Arial',12,'bold'), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=440,y=520)

    label_transporte = ctk.CTkLabel(position, text=f'Transporte: R${gastos_por_categoria(choice_month(choice), 'Transporte'):,.2f}', font=('Arial',12,'bold'), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=550)
    
    label_autocuidado = ctk.CTkLabel(position, text=f'Auto-Cuidado: R${gastos_por_categoria(choice_month(choice), 'Auto Cuidado'):,.2f}', font=('Arial',12,'bold'), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=440,y=550)