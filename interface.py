import customtkinter as ctk
from funcoes import *
from data import *
def gastos():

    exibir_tabela(frameCentral)
    labelGastos = ctk.CTkLabel(frameCentral, justify='center', width=600, text="Aqui é a área de gastos", font=ctk.CTkFont(size=20, weight="bold"), fg_color='#F3F4F6', text_color='#1E3A8A').place(x=200,y=10)
    btnAdd = ctk.CTkButton(frameCentral,command=lambda:addGasto(frameCentral), width=150, text="Adicionar Gasto", fg_color=('#F3F4F6'),text_color='black', border_color='black', border_width=2).place(x=325,y=500)
    btnRemove = ctk.CTkButton(frameCentral, width=150, text="Remover Gasto", fg_color=('#F3F4F6'),text_color='black', border_color='black', border_width=2).place(x=525,y=500)

def dashboard():
 
    labelDashboard = ctk.CTkLabel(frameCentral,justify='center', width=600, text="Aqui é a área do DashBoard", font=ctk.CTkFont(size=20, weight="bold"), fg_color='#457B9D', text_color='#1E3A8A').place(x=200,y=10)
    

window = ctk.CTk()

window.geometry("800x600")
window.title("EgidePlan")
window.resizable(False, False)
window.iconbitmap("assents/logo.ico") #Coloca o ícone da aplicação

linha = ctk.CTkFrame(window, width=200, height=600, fg_color='black').place(x=200,y=0)
frameCentral = ctk.CTkFrame(window, width=600, height=600, fg_color='#F3F4F6',border_color='#E5E7EB', border_width=2).place(x=200,y=0)
framelateral = ctk.CTkFrame(window,  width=200, height=600, fg_color="#1E3A8A",border_color='#E5E7EB', border_width=1).place(x=0,y=0)


logo = ctk.CTkLabel(framelateral, text="EgidePlan", font=ctk.CTkFont(size=20, weight="bold"), fg_color="#1E3A8A", text_color='#F8FAFC').place(x=50,y=20)

btnDashboard = ctk.CTkButton(framelateral, width=200, command=dashboard, text="Dashboard", fg_color=('#F3F4F6'),text_color='#1E3A8A', border_color='#E5E7EB', border_width=1, hover_color='#3B82F6').place(x=0,y=200)
btnGastos = ctk.CTkButton(framelateral, command=gastos, text="Gastos",  width=200, fg_color=('#F3F4F6'),text_color='#1E3A8A', border_color='#E5E7EB', border_width=1, hover_color='#3B82F6').place(x=0,y=250)

    
window.mainloop()