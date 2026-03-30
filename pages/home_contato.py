import customtkinter as ctk
from PIL import Image
import random
from webbrowser import open


#frases aleatórias
sentences = [
     "O que pode ser medido, pode ser melhorado. O primeiro passo para a liberdade financeira é a clareza dos seus números.",
     "Pequenos vazamentos afundam grandes navios. Use o Edge Plan para identificar aqueles pequenos gastos que somam muito no final do mês.",
     "Orçamento não é sobre limitar gastos, é sobre garantir que seu dinheiro vá para onde é mais importante para você.",
     "A organização financeira de hoje é a tranquilidade do seu 'eu' de amanhã.",
     "Não trabalhe pelo dinheiro, faça o dinheiro trabalhar para você. Comece entendendo para onde ele está indo."
]
#home frame
def home(frame):
     new_frame = ctk.CTkFrame(frame, width=600, height=600, fg_color='#F3F4F6').place(x=200) 
     
     img = ctk.CTkImage(light_image=Image.open('./assents/logo.ico'), size=(100,100))

     labelimg = ctk.CTkLabel(new_frame, text=None, image=img,fg_color='#F3F4F6', width=600, justify='center').place(x=200)
     welcome = ctk.CTkLabel(new_frame, text='Bem vindo(a) ao EgidePlan', width=600, justify='center',font= ('arial',20,'bold'), fg_color='#F3F4F6', text_color='#1E3A8A').place(x=200,y=100)
     first = ctk.CTkLabel(new_frame, text='Primeira vez aqui? Veja como é fácil!',fg_color='#F3F4F6', width=600, justify='center', font=('arial', 16, 'bold'), text_color='#1E3A8A').place(x=200, y=150)
     gastos = ctk.CTkLabel(new_frame, text='1. Adicione seus gastos clicando no botão "Gastos" no menu lateral.',fg_color='#F3F4F6', width=550, anchor='w', font=('arial', 14, 'bold'), wraplength=600, text_color='#3B82F6').place(x=250, y=200)
     dashboard = ctk.CTkLabel(new_frame, text='2. Acompanhe seus gastos e estatísticas no Dashboard.',fg_color='#F3F4F6', width=550, anchor='w', font=('arial', 14, 'bold'), wraplength=600, text_color='#3B82F6').place(x=250, y=250)

     msg = ctk.CTkLabel(new_frame, text=random.choice(sentences),fg_color='#F3F4F6', width=600, justify='center', font=('arial', 16, 'bold'), wraplength=600, text_color='#3B82F6').place(x=200, y=500)

#contact frame
def contact(frame):
     new_frame = ctk.CTkFrame(frame, width=600, height=600, fg_color='#F3F4F6').place(x=200) 

     msg_title = ctk.CTkLabel(new_frame, text='Gostou do EgidePlan?',fg_color='#F3F4F6', width=600, justify='center', font=('arial', 22, 'bold'),text_color='#1E3A8A').place(x=200, y=20)

     msg_return = ctk.CTkLabel(new_frame, text='Desenvolvo soluções personalizadas que facilitam sua vida pessoal e profissional. \n\n\n\n\nEntre em contato comigo para discutir como posso ajudar você a alcançar seus objetivos com tecnologia sob medida!',fg_color='#F3F4F6', width=600, justify='center', font=('arial', 16, 'bold'), wraplength=500, text_color='#3B82F6').place(x=200, y=70)

     btn_linkedin = ctk.CTkButton(new_frame, text='Visite meu LinkedIn', command=lambda: open('https://www.linkedin.com/in/igorjeronimo/'), fg_color='#0A66C2', width=250, text_color='#FFFFFF', border_color='#1E3A8A', border_width=1, hover_color='#004182').place(x=500, y=300, anchor='n')

     btn_github = ctk.CTkButton(new_frame, text='Confira meus projetos no GitHub', command=lambda: open('https://github.com/Ginhoh'), fg_color='#181717', width=250, text_color='#FFFFFF', border_color='#1E3A8A', border_width=1, hover_color='#0F0F0F').place(x=500, y=350, anchor='n')

     btn_email = ctk.CTkButton(new_frame, text='Entre em contato por Email', command=lambda: open('mailto:igorjeronimo2007@gmail.com'), fg_color='#D44638', width=250, text_color='#FFFFFF', border_color='#8B2B22', border_width=1, hover_color='#B2312A').place(x=500, y=400, anchor='n')

     btn_portfolio = ctk.CTkButton(new_frame, text='Acesse meu portfolio', command=lambda: open('https://ginhoh.github.io/igorjeronimo/'), fg_color='#111827', width=250, text_color='#FFFFFF', border_color='#1E3A8A', border_width=1, hover_color="#0C1832").place(x=500, y=450, anchor='n')

     thanks = ctk.CTkLabel(new_frame, text='Obrigado por usar o EgidePlan!',fg_color='#F3F4F6', width=600, justify='center', font=('arial', 16, 'bold'), text_color='#1E3A8A').place(x=200, y=550)