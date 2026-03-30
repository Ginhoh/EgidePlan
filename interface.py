#Bibliotecas
import customtkinter as ctk
from funcoes import *
from pages.dashboard import *
from pages.gastos import *
from pages.home_contato import *

#Configurações iniciais da janela principal
ctk.set_appearance_mode('light')
window = ctk.CTk()

window.geometry("800x600")
window.title("EgidePlan - Controle de Gastos")
window.resizable(False, False) 
window.iconbitmap("assents/logo.ico") 


central_frame = ctk.CTkFrame(window, width=600, height=600, fg_color='#F3F4F6',border_color='#E5E7EB', border_width=2).place(x=200,y=0)  # área principal onde o conteúdo é exibido

lateral_frame = ctk.CTkFrame(window,  width=200, height=600, fg_color="#1E3A8A",border_color='#E5E7EB', border_width=1).place(x=0,y=0)  # menu lateral


logo = ctk.CTkLabel(lateral_frame, text="EgidePlan", font=ctk.CTkFont(size=20, weight="bold"), fg_color="#1E3A8A", text_color='#F8FAFC').place(x=50,y=20)  # título/logo no menu lateral

btn_home = ctk.CTkButton(lateral_frame, width=200, command=lambda:home(central_frame), text="Home",anchor='w', fg_color=('#F3F4F6'),text_color='#1E3A8A', border_color='#E5E7EB', border_width=1, hover_color='#3B82F6').place(x=0,y=170)  # botão para abrir a tela Home

btn_dashboard = ctk.CTkButton(lateral_frame, width=200, command=lambda:exibir_dashboard(central_frame), text="Dashboard",anchor='w', fg_color=('#F3F4F6'),text_color='#1E3A8A', border_color='#E5E7EB', border_width=1, hover_color='#3B82F6').place(x=0,y=200)  # botão para abrir Dashboard

btn_gastos = ctk.CTkButton(lateral_frame, command=lambda:show_table(central_frame), text="Gastos",anchor='w',  width=200, fg_color=('#F3F4F6'),text_color='#1E3A8A', border_color='#E5E7EB', border_width=1, hover_color='#3B82F6').place(x=0,y=230)  # botão para abrir a lista de gastos

btn_contato = ctk.CTkButton(lateral_frame, command=lambda:contact(central_frame), text="Contato",anchor='w',  width=200, fg_color=('#F3F4F6'),text_color='#1E3A8A', border_color='#E5E7EB', border_width=1, hover_color='#3B82F6').place(x=0,y=260)  # botão para abrir a tela de contato

home(central_frame)  # mostra a tela inicial ao iniciar
window.mainloop()  # inicia o loop de eventos da GUI

