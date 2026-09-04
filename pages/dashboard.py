import customtkinter as ctk
from funcoes import *
from models import *
#Dashboard



def exibir_dashboard(position): 

    new_frame = ctk.CTkFrame(position, width=600, height=600, fg_color='#F3F4F6', border_width=None, border_color='#E5E7EB').place(x=200)
    title = ctk.CTkLabel(new_frame,width=600, text='DASHBOARD',font=('Arial', 20, 'bold'),text_color='grey', justify='left', fg_color='#F3F4F6').place(x=200,y=5)

    

    #bloco1=ctk.CTkFrame(position, width=200, height=100, fg_color="#F3F4F6",border_color="#E5E7EB", bg_color='transparent').place(x=230,y=60)
    label_total = ctk.CTkLabel(position, text=f'TOTAL\nR${gastos_total(actual_month()):,.2f}', font=('Impact',24), text_color='#1E3A8A',width=194, height=94, fg_color='#F3F4F6').place(x=232,y=62)

    #bloco2=ctk.CTkFrame(position, width=200, height=100, fg_color="#F3F4F6", border_color="#E5E7EB", bg_color='transparent').place(x=570,y=60)
    label_media = ctk.CTkLabel(position, text=f'MÉDIA\nR${gastos_media(actual_month()):.2f}', font=('Impact',24), text_color='#1E3A8A',width=194, height=94, fg_color='#F3F4F6').place(x=572,y=62)


    label_maior = ctk.CTkLabel(position, text=f'Categoria com maior gasto: {categoria_maior(actual_month())}', font=('Arial',20),width=400,anchor='w', text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=230)

    label_menor = ctk.CTkLabel(position, text=f'Categoria com menor gasto: {categoria_menor(actual_month())}', font=('Arial',20),width=400,anchor='w', text_color='#1E3A8A', fg_color='#F3F4F6').place(x=240,y=260)

    label_comparacao = ctk.CTkLabel(position, text=comparacao(), font=('Arial',20), text_color='#1E3A8A', width=400,anchor='w', fg_color='#F3F4F6').place(x=240,y=290)

    subtitle = ctk.CTkLabel(position,width=600, text='Gastos por Categoria',font=('Arial', 20, 'bold'),text_color='#1E3A8A', justify='center', fg_color='#F3F4F6').place(x=200,y=320)
    
    cursor.execute("""SELECT nome FROM categoria""")
    query = cursor.fetchall()
    size_x = 240
    size_y = 360

    for dados in query:
        nome = dados[0]
        label_categ = ctk.CTkLabel(position, text=f'{nome}: R${gastos_por_categoria(actual_month(), nome)}', font=('Georgia',14), text_color='black', fg_color='#F3F4F6').place(x=size_x,y=size_y)
        size_y += 30
        if size_y >510:
            size_y = 360
            size_x = 460
    


