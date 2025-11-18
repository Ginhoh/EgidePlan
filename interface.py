import customtkinter as ctk
from funcoes import *
import data
def gastos():
    labelGastos = ctk.CTkLabel(frameCentral,justify='center', width=600, text="Aqui é a área de gastos", font=ctk.CTkFont(size=20, weight="bold"), fg_color='transparent', text_color='black').place(x=200,y=10)


def dashboard():
    labelDashboard = ctk.CTkLabel(frameCentral,justify='center', width=600, text="Aqui é a área do Dashboard", font=ctk.CTkFont(size=20, weight="bold"), fg_color='transparent', text_color='black').place(x=200,y=10)


window = ctk.CTk(fg_color="#aefac5")

window.geometry("800x600")
window.title("EgidePlan")
window.resizable(False, False)
window.iconbitmap("teste.py") #Coloca o ícone da aplicação

framelateral = ctk.CTkFrame(window,  width=200, height=600, fg_color='#aefac5').place(x=0,y=0)
linha = ctk.CTkFrame(window, width=200, height=600, fg_color='black').place(x=200,y=0)
frameCentral = ctk.CTkFrame(window, width=600, height=600, fg_color='transparent').place(x=200,y=0)

logo = ctk.CTkLabel(framelateral, text="EgidePlan", font=ctk.CTkFont(size=20, weight="bold"), fg_color='#aefac5', text_color='black').place(x=50,y=20)

btnDashboard = ctk.CTkButton(framelateral, width=200, command=dashboard, text="Dashboard", fg_color=('transparent'),text_color='black', border_color='black', border_width=2).place(x=0,y=200)
btnGastos = ctk.CTkButton(framelateral, command=gastos, text="Gastos",  width=200, fg_color=('transparent'),text_color='black', border_color='black', border_width=2).place(x=0,y=250)

    
window.mainloop()