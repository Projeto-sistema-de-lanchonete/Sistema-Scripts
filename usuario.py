import tkinter as gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image





def MainUsuario():
  signin_window = Toplevel()
  signin_window.title("Lanchonete | Cadastar usuario")
  signin_window.resizable(False,False)  
  signin_window.iconbitmap("imagens/ico.lanchonete.ico")

  # Label(signin_window,text="Cadastrar",font="Ariel").grid(row=0,column=0,sticky=W,pady=10)
  Usuario_label = Label(signin_window,text="Usuario :",font="Ariel,12")
  Usuario_label.grid(row=0,column=0)

  Cpf_label = Label(signin_window,text="CPF :",font="Ariel,12")
  Cpf_label.grid(row=1,column=0)

  Senha_label = Label(signin_window,text="Senha :",font="Ariel,12")
  Senha_label.grid(row=2,column=0,pady=(0,20))

  Usuario_entry = Entry(signin_window, font="Ariel,10").grid(row=0,column=1)
  Cpf_entry = Entry(signin_window, font="Ariel,10").grid(row=1,column=1)
  Senha_entry = Entry(signin_window, font="Ariel,10").grid(row=2,column=1,pady=(0,20))

  user_add = Button(signin_window,text="Cadastrar",font="Ariel,17")
  user_add.grid(row=1,column=2,rowspan=2,padx=20,pady=(0,20))

  view_exist = Button(signin_window,text="Visualizar Cadastros")
  view_exist.grid(row=4,column=0,rowspan=2,columnspan=4,padx=20,pady=(0,20),sticky=W+E)

  signin_window.mainloop()
