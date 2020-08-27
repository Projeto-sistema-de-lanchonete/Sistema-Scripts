import tkinter as gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
import time


def MainEditUsuario():
      
 
  def PesquisarUsuario():
     connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
     mycursorEdit = connection.cursor()

     iduserEdit = str(Id_entry.get())

     sqlEdit = "select * from usuarios where id = {};".format(iduserEdit)
     print(sqlEdit)
     mycursorEdit.execute(sqlEdit)
     print(mycursorEdit)

     for i in mycursorEdit:
       print(i)

     Usuario_entry.insert(0,i[1])
     Cpf_entry.insert(0,i[2])
     Senha_entry.insert(0,i[3]) 

# Funçao para Alterar o cadastro de usuário 
  def UpdateUsuario():
    connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
    mycursor = connection.cursor()

    # abrituindo os valores dos entry a uma variável-----------------
    user = str(Usuario_entry.get())
    cpf = str(Cpf_entry.get())
    senha = str(Senha_entry.get())
    ide = str(Id_entry.get())

    # Script de Update
    sqlupdate = "UPDATE usuarios SET  nome='{}', cpf={}, senha={} where id ={}".format(user, cpf, senha,ide)
    print(sqlupdate)
    mycursor.execute(sqlupdate)

    
# Zera os campos
    Usuario_entry.delete(0,END)
    Cpf_entry.delete(0,END)
    Senha_entry.delete(0,END)

    time.sleep(2)
    messagebox.showinfo(title="Info",message="Usuário alterado com sucesso!")
    # Texto_label["text"] = "Usuário cadastrado com sucesso!"
# Fecha a conexão do banco de dados
    mycursor.close()
    connection.commit()
    connection.close()


    

  # ----------------------------------------------------------------------
  signin_window = Toplevel()
  signin_window.title("Lanchonete | Editar Usuário")
  signin_window.resizable(False,False)  
  signin_window.iconbitmap("imagens/ico.lanchonete.ico")
  signin_window.configure(bg="#DCDCDC")
  
  #=================notebook========================
  mynot  = ttk.Notebook(signin_window)
  mynot.pack(pady=10)

  # ------------Frames----------------------------------
  frame1 = gui.Frame(mynot,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
  frame1.place(relwidth=0.80,relheight=0.3,relx=0.1,rely=0.2)
  mynot.add(frame1, text="Editar usuário")


  #---------labels-----------------------------
  # Label(signin_window,text="Cadastrar",font="Ariel").grid(row=0,column=0,sticky=W,pady=10)

  esp_label = Label(frame1,text="", bg="#C0C0C0")
  esp_label.grid(row=0,column=0)

  Usuario_label = Label(frame1,text="Cod.:", bg="#C0C0C0", font="Britannic 10 bold")
  Usuario_label.grid(row=1,column=0, pady=5, padx=10) #pady e padx é o espaço ao redor

  Usuario_label = Label(frame1,text="Usuário:", bg="#C0C0C0", font="Britannic 10 bold")
  Usuario_label.grid(row=2,column=0, pady=5, padx=10) #pady e padx é o espaço ao redor

  Cpf_label = Label(frame1,text="CPF:", bg="#C0C0C0", font="Britannic 10 bold")
  Cpf_label.grid(row=3,column=0, pady=5, padx=10)

  Senha_label = Label(frame1,text="Senha:", bg="#C0C0C0", font="Britannic 10 bold")
  Senha_label.grid(row=4,column=0, pady=5, padx=10)

  Texto_label = Label(frame1,text="", fg="green", bg="#C0C0C0", font="Britannic 10 bold")
  Texto_label.grid(row=5,column=0,rowspan=20,columnspan=4,padx=20,pady=15,sticky=W+E)

 

  #---------entrys-----------------------------
  Id_entry = Entry(frame1, width=10, bd=4)
  Id_entry.grid(row=1,column=1,ipady=3,sticky=W+E)

  Usuario_entry = Entry(frame1, width=35, bd=4)
  Usuario_entry.grid(row=2,column=1,ipady=3)

  Cpf_entry = Entry(frame1, width=35, bd=4)
  Cpf_entry.grid(row=3,column=1,ipady=3)

  Senha_entry = Entry(frame1, width=35, bd=4)
  Senha_entry.grid(row=4,column=1,ipady=3)


  #---------buttons-----------------------------
  excluiruser = Button(frame1,text="Pesquisar",bg="#C0C0C0", padx=20, pady=2, borderwidth=5,command=PesquisarUsuario,width=15)
  excluiruser.grid(row=1,column=2,rowspan=2,columnspan=4,padx=20,pady=(0,20),sticky=W+E)
  
  salvar_add = Button(frame1,text="Salvar",bg="#C0C0C0", padx=20, pady=2, borderwidth=5,command=UpdateUsuario)
  salvar_add.grid(row=5,column=1,rowspan=2,padx=20, pady=20,sticky=W+E)


 
 

  signin_window.mainloop()
  