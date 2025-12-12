import customtkinter as ctk
from PIL import Image
import random

frases = [
     "O que pode ser medido, pode ser melhorado. O primeiro passo para a liberdade financeira é a clareza dos seus números.",
     "Pequenos vazamentos afundam grandes navios. Use o Edge Plan para identificar aqueles pequenos gastos que somam muito no final do mês.",
     "Orçamento não é sobre limitar gastos, é sobre garantir que seu dinheiro vá para onde é mais importante para você.",
     "A organização financeira de hoje é a tranquilidade do seu 'eu' de amanhã.",
     "Não trabalhe pelo dinheiro, faça o dinheiro trabalhar para você. Comece entendendo para onde ele está indo."
]
def home(frame):
     new_frame = ctk.CTkFrame(frame, width=600, height=600, fg_color='#F3F4F6', border_width=2, border_color='#E5E7EB').place(x=200) 
     
     img = ctk.CTkImage(light_image=Image.open('./assents/logo.ico'), size=(100,100))

     labelimg = ctk.CTkLabel(new_frame, text=None, image=img,fg_color='#F3F4F6', width=600, justify='center').place(x=200)
     welcome = ctk.CTkLabel(new_frame, text='Bem vindo(a) ao EgidePlan')

     msg = ctk.CTkLabel(new_frame, text=random.choice(frases),fg_color='#F3F4F6', width=600,height=200, justify='center', font=('arial', 16, 'bold'), text_color='#3B82F6').place(x=200, y=400)