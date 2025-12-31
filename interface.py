import customtkinter as ctk
from funcoes import *
from dashboard import *
from gastos import *
from home import *

ctk.set_appearance_mode('light')
window = ctk.CTk()

window.geometry("800x600")
window.title("EgidePlan - Controle de Gastos")
window.resizable(False, False)
window.iconbitmap("assents/logo.ico") #Coloca o ícone da aplicação


frameCentral = ctk.CTkFrame(window, width=600, height=600, fg_color='#F3F4F6',border_color='#E5E7EB', border_width=2).place(x=200,y=0)
framelateral = ctk.CTkFrame(window,  width=200, height=600, fg_color="#1E3A8A",border_color='#E5E7EB', border_width=1).place(x=0,y=0)


logo = ctk.CTkLabel(framelateral, text="EgidePlan", font=ctk.CTkFont(size=20, weight="bold"), fg_color="#1E3A8A", text_color='#F8FAFC').place(x=50,y=20)


btn_home = ctk.CTkButton(framelateral, width=200, command=lambda:home(frameCentral), text="Home", fg_color=('#F3F4F6'),text_color='#1E3A8A', border_color='#E5E7EB', border_width=1, hover_color='#3B82F6').place(x=0,y=170)
btnDashboard = ctk.CTkButton(framelateral, width=200, command=lambda:exibir_dashboard(frameCentral), text="Dashboard", fg_color=('#F3F4F6'),text_color='#1E3A8A', border_color='#E5E7EB', border_width=1, hover_color='#3B82F6').place(x=0,y=200)
btnGastos = ctk.CTkButton(framelateral, command=lambda:exibir_tabela(frameCentral), text="Gastos",  width=200, fg_color=('#F3F4F6'),text_color='#1E3A8A', border_color='#E5E7EB', border_width=1, hover_color='#3B82F6').place(x=0,y=230)

home(frameCentral)
window.mainloop()

