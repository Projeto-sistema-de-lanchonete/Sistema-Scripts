import tkinter as gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql







def MainUsuario():
  def CadastrarUsuario():
  
    connection = pymysql.connect(
      host="localhost",
      user="root",
      password="",
      database="db"
     )
    mycursor = connection.cursor()
    sql = "INSERT INTO usuarios (name, cpf,senha) VALUES (%s, %s,%s)"
    val = (Usuario_entry.get(), Cpf_entry.get(),Senha_entry.get())
    mycursor.execute(sql, val)

    connection.commit()
    Usuario_entry.delete(0,END)
    Cpf_entry.delete(0,END)
    Senha_entry.delete(0,END)
    messagebox.showinfo(title="Aviso",message="Usuario Cadastrado com sucesso")



    


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

  Usuario_entry = Entry(signin_window, font="Ariel,10")
  Usuario_entry.grid(row=0,column=1)
  Cpf_entry = Entry(signin_window, font="Ariel,10")
  Cpf_entry.grid(row=1,column=1)
  Senha_entry = Entry(signin_window, font="Ariel,10")
  Senha_entry.grid(row=2,column=1,pady=(0,20))

  

  user_add = Button(signin_window,text="Cadastrar",font="Ariel,17",command=CadastrarUsuario)
  user_add.grid(row=1,column=2,rowspan=2,padx=20,pady=(0,20))

  view_exist = Button(signin_window,text="Visualizar Cadastros")
  view_exist.grid(row=4,column=0,rowspan=2,columnspan=4,padx=20,pady=(0,20),sticky=W+E)

  signin_window.mainloop()
