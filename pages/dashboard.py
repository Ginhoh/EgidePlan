import customtkinter as ctk
from funcoes import *
from models import *
#Dashboard



def exibir_dashboard(position): 

    new_frame = ctk.CTkFrame(position, width=600, height=600, fg_color='#F3F4F6', border_width=2, border_color='#E5E7EB').place(x=200)
    title = ctk.CTkLabel(new_frame,width=600, text='DASHBOARD',font=('Arial', 20, 'bold'),text_color='#1E3A8A', justify='center', fg_color='#F3F4F6').place(x=200,y=5)

    

    bloco1=ctk.CTkFrame(position, width=200, height=100, fg_color="#F3F4F6", border_width=2, border_color="#E5E7EB", bg_color='transparent').place(x=230,y=60)
    label_total = ctk.CTkLabel(bloco1, text=f'TOTAL\nR${gastos_total(actual_month()):,.2f}', font=('Arial',24), text_color='#1E3A8A',width=194, height=94, fg_color='#F3F4F6').place(x=232,y=62)

    bloco2=ctk.CTkFrame(position, width=200, height=100, fg_color="#F3F4F6", border_width=2, border_color="#E5E7EB", bg_color='transparent').place(x=570,y=60)
    label_media = ctk.CTkLabel(bloco2, text=f'MÉDIA\nR${gastos_media(actual_month()):.2f}', font=('Arial',24), text_color='#1E3A8A',width=194, height=94, fg_color='#F3F4F6').place(x=572,y=62)


    label_maior = ctk.CTkLabel(position, text=f'Categoria com maior gasto: {categoria_maior(actual_month())}', font=('Arial',20),width=400,anchor='w', text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=230)

    label_menor = ctk.CTkLabel(position, text=f'Categoria com menor gasto: {categoria_menor(actual_month())}', font=('Arial',20),width=400,anchor='w', text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=260)

    label_comparacao = ctk.CTkLabel(position, text=comparacao(), font=('Arial',20), text_color='#1E3A8A', width=400,anchor='w', fg_color='#F3F4F6').place(x=240,y=290)

    subtitle = ctk.CTkLabel(position,width=600, text='Gastos por Categoria',font=('Arial', 16, 'bold'),text_color='#1E3A8A', justify='center', fg_color='#F3F4F6').place(x=200,y=320)

    label_essencial = ctk.CTkLabel(position, text=f'Essencial: R${gastos_por_categoria(actual_month(), 'Essencial'):,.2f}', font=('Arial',14), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=360)

    label_alimentacao = ctk.CTkLabel(position, text=f'Alimentação: R${gastos_por_categoria(actual_month(), 'Alimetação'):,.2f}', font=('Arial',14), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=390)

    label_lazer = ctk.CTkLabel(position, text=f'Lazer: R${gastos_por_categoria(actual_month(), 'Lazer'):,.2f}', font=('Arial',14), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=420)
    label_investimentos = ctk.CTkLabel(position, text=f'Investimentos: R${gastos_por_categoria(actual_month(), 'Investimentos'):,.2f}', font=('Arial',14), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=450)

    label_transporte = ctk.CTkLabel(position, text=f'Transporte: R${gastos_por_categoria(actual_month(), 'Transporte'):,.2f}', font=('Arial',14), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=480)
    
    label_autocuidado = ctk.CTkLabel(position, text=f'Auto-Cuidado: R${gastos_por_categoria(actual_month(), 'Auto Cuidado'):,.2f}', font=('Arial',14), text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=510)
    


#Gastos totais, média, categoria com maior gasto, categoria com menor gasto, comparação com mês anterior
def gastos_total(month):
    cursor.execute(f"""SELECT SUM(valor) FROM gastos WHERE data LIKE '%/{month}/%'
""")
    total = cursor.fetchall()
    if total[0][0] == None:
        return 0.0
    else:
        return total[0][0]


def gastos_media(month):
    cursor.execute(f"""SELECT AVG(valor) FROM gastos WHERE data LIKE '%/{month}/%'""")
    media = cursor.fetchall()
    if media[0][0] == None:
        return 0.0
    else:
        return media[0][0]


def categoria_maior(month):
    cursor.execute(f"""SELECT categoria, SUM(valor) FROM gastos WHERE data LIKE '%/{month}/%' 
               GROUP BY categoria """)
    dados = cursor.fetchall()
    select = ''
    maior = 0
    for valor in dados:
        categ, sumvalor = valor
        if sumvalor>maior:
            maior = sumvalor
            select = categ
    return select
    


def categoria_menor(month):
    cursor.execute(f"""SELECT categoria, SUM(valor) FROM gastos WHERE data LIKE '%/{month}/%' 
               GROUP BY categoria """)
    dados = cursor.fetchall()
    select = ''
    menor = dados[0][1]
    for valor in dados:
        categ, sumvalor = valor
        if sumvalor<float(menor):
            menor = sumvalor
            select = categ

    return select

def comparacao():
    mes_atual = float(gastos_total(actual_month()))
    mes_passado = float(gastos_total(past_month()))
    if mes_atual > mes_passado:
        return f'R${mes_atual - mes_passado:,.2f} superior ao mês passado'
    elif mes_atual < mes_passado:
        return f'R${mes_passado - mes_atual:,.2f} inferior ao mês passado'
    else:
        return f'Mesma quantia acumulada refetente ao mês passado'

def gastos_por_categoria(month, categoria):
   cursor.execute(f"SELECT SUM(valor) FROM gastos WHERE data LIKE '%/{month}/%' AND categoria = '{categoria}'")
   dados = cursor.fetchall()
   return 0 if dados[0][0] == None else dados[0][0]


