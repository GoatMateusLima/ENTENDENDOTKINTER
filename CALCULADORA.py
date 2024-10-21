#importa a biblioteca

from tkinter import *
from tkinter import ttk
import os

#cores atribuidas a variaveis
co1='#000'
co2='#fff'
co3='#38576b'
co4='#1C1C1C'
co5='#FF8C00'
co6='#8B0000'

#janela e nome da janela
janela = Tk()
janela.title('Calculadora')

#imagem do app
caminho_img = os.path.join('img', 'favicon.ico')
janela.iconbitmap(caminho_img)

#tamanho e cor
janela.geometry('250x323')
janela.resizable(width= False, height= False )
janela.config(bg=(co1))

#Criando frames da tela
frame_tela = Frame(janela, width=250, height=70, bg=(co3))
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=250, height=278)
frame_corpo.grid(row=1, column=0)


#Variavel todos valores

todos_valores = ''

#Criando Label
valor_texto = StringVar()

#armazenar valores

def entrada_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    #passando valor para a tela

    valor_texto.set(todos_valores)

#funcao para calcular valores

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

#funcao limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


app_label = Label(frame_tela, textvariable= valor_texto, width=24, height=5, padx=5, relief=FLAT, anchor="e", justify=RIGHT, font=('Helvetica 13 bold'), bg=co3, fg=co2)
app_label.place(x=0, y=0)

#criando Botoes

b1= Button(frame_corpo, command = limpar_tela, text='C', width=13, height=2, bg=(co6), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0 , y=0)
b2= Button(frame_corpo, command= lambda: entrada_valores('%'), text='%', width=6, height=2, bg=(co5), fg=(co2),  font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=120 , y=0)
b3= Button(frame_corpo, command= lambda: entrada_valores('/'),text='/', width=6, height=2, bg=(co5), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=185 , y=0)

b4= Button(frame_corpo, command= lambda: entrada_valores('7'),text='7', width=5, height=2, bg=(co4), fg=(co2),  font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5= Button(frame_corpo, command= lambda: entrada_valores('8'),text='8', width=5, height=2, bg=(co4), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6= Button(frame_corpo, command= lambda: entrada_valores('9'),text='9', width=6, height=2, bg=(co4), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118 , y=52)
b7= Button(frame_corpo, command= lambda: entrada_valores('*'),text='*', width=6, height=2, bg=(co5), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=185 , y=52)

b8= Button(frame_corpo, command= lambda: entrada_valores('4'),text='4', width=5, height=2, bg=(co4), fg=(co2),  font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=102)
b9= Button(frame_corpo, command= lambda: entrada_valores('5'),text='5', width=5, height=2, bg=(co4), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=102)
b10= Button(frame_corpo,command= lambda: entrada_valores('6'), text='6', width=6, height=2, bg=(co4), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118 , y=102)
b11= Button(frame_corpo, command= lambda: entrada_valores('-'),text='-', width=6, height=2, bg=(co5), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=185 , y=102)

b12= Button(frame_corpo, command= lambda: entrada_valores('1'),text='1', width=5, height=2, bg=(co4), fg=(co2),  font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=152)
b13= Button(frame_corpo, command= lambda: entrada_valores('2'),text='2', width=5, height=2, bg=(co4), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=152)
b14= Button(frame_corpo, command= lambda: entrada_valores('3'),text='3', width=6, height=2, bg=(co4), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118 , y=152)
b15= Button(frame_corpo, command= lambda: entrada_valores('+'),text='+', width=6, height=2, bg=(co5), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=185 , y=152)

b16= Button(frame_corpo, command= lambda: entrada_valores('0'),text='0', width=13, height=2, bg=(co4), fg=(co2),  font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=202)
b17= Button(frame_corpo, command= lambda: entrada_valores('.'),text='.', width=6, height=2, bg=(co4), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=202)
b18= Button(frame_corpo, command= calcular,text='=', width=6, height=2, bg=(co5), fg=(co2), font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=185 , y=202)


#deixa a janela em loop
janela.mainloop()