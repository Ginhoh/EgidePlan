import customtkinter as ctk
from openpyxl import load_workbook
from funcoes import *

tabela = load_workbook('total_de_gastos.xlsx')
verificarAba(tabela, mes_atual())
main_page = tabela[mes_atual()]



def exibir_dashboard(position):        
    new_frame = ctk.CTkFrame(position, width=600, height=600, fg_color='#F3F4F6', border_width=2, border_color='#E5E7EB').place(x=200)
    title = ctk.CTkLabel(new_frame,width=600, text='DASHBOARD',font=('Arial', 20),text_color='#1E3A8A', justify='center', fg_color='#F3F4F6').place(x=200,y=5)


    bloco1=ctk.CTkFrame(position, width=200, height=100, fg_color="#F3F4F6", border_width=2, border_color="#E5E7EB", corner_radius=20, bg_color='transparent').place(x=230,y=60)
    label_total = ctk.CTkLabel(bloco1, text=f'TOTAL\nR${gastos_total(main_page):.2f}', font=('Arial',24), text_color='#1E3A8A',width=194, height=94, fg_color='#F3F4F6').place(x=232,y=62)

    bloco2=ctk.CTkFrame(position, width=200, height=100, fg_color="#F3F4F6", border_width=2, border_color="#E5E7EB", corner_radius=20, bg_color='transparent').place(x=570,y=60)
    label_total = ctk.CTkLabel(bloco2, text=f'MÉDIA\nR${gastos_media(main_page):.2f}', font=('Arial',24), text_color='#1E3A8A',width=194, height=94, fg_color='#F3F4F6').place(x=572,y=62)

