import customtkinter as ctk
from PIL import Image
import random

sentences = [
     "O que pode ser medido, pode ser melhorado. O primeiro passo para a liberdade financeira é a clareza dos seus números.",
     "Pequenos vazamentos afundam grandes navios. Use o Edge Plan para identificar aqueles pequenos gastos que somam muito no final do mês.",
     "Orçamento não é sobre limitar gastos, é sobre garantir que seu dinheiro vá para onde é mais importante para você.",
     "A organização financeira de hoje é a tranquilidade do seu 'eu' de amanhã.",
     "Não trabalhe pelo dinheiro, faça o dinheiro trabalhar para você. Comece entendendo para onde ele está indo."
]
def home(frame):
     new_frame = ctk.CTkFrame(frame, width=600, height=600, fg_color='#F3F4F6').place(x=200) 
     
     img = ctk.CTkImage(light_image=Image.open('./assents/logo.ico'), size=(100,100))

     labelimg = ctk.CTkLabel(new_frame, text=None, image=img,fg_color='#F3F4F6', width=600, justify='center').place(x=200)
     welcome = ctk.CTkLabel(new_frame, text='Bem vindo(a) ao EgidePlan', width=600, justify='center',font= ('arial',20,'bold'), fg_color='#F3F4F6', text_color='#1E3A8A').place(x=200,y=100)
     first = ctk.CTkLabel(new_frame, text='Primeira vez aqui? Veja como é fácil!',fg_color='#F3F4F6', width=600, justify='center', font=('arial', 16, 'bold'), text_color='#1E3A8A').place(x=200, y=150)
     gastos = ctk.CTkLabel(new_frame, text='1. Adicione seus gastos clicando no botão "Gastos" no menu lateral.',fg_color='#F3F4F6', width=550, anchor='w', font=('arial', 14, 'bold'), wraplength=600, text_color='#3B82F6').place(x=250, y=200)
     dashboard = ctk.CTkLabel(new_frame, text='2. Acompanhe seus gastos e estatísticas no Dashboard.',fg_color='#F3F4F6', width=550, anchor='w', font=('arial', 14, 'bold'), wraplength=600, text_color='#3B82F6').place(x=250, y=250)

     msg = ctk.CTkLabel(new_frame, text=random.choice(sentences),fg_color='#F3F4F6', width=600, justify='center', font=('arial', 16, 'bold'), wraplength=600, text_color='#3B82F6').place(x=200, y=500)