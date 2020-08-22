import tkinter as gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

def MainClientes():

  
    # ------------Opening Window----------------------------------
      window = gui.Tk()
      window.title("Cadatro de Cliente")
      window.iconbitmap("logo.ico")
      window.protocol("WM_DELETE_WINDOW")
      window.resizable(False,False) # WxH
      window.geometry("950x500") # WxH


    # ------------Frames----------------------------------
      clientes = gui.Frame(window,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
      clientes.place(relwidth=0.80,relheight=0.73,relx=0.1,rely=0.15)

    # ------------Widgets----------------------------------
    #labels

      Pesquisar_Label = gui.Label(clientes,text="Pesquisar:", bg="#C0C0C0", font="Britannic 10 bold")
      Pesquisar_Label.grid(sticky=W,padx=8)

      Pesquisar_entry = gui.Entry(clientes, width =15)
      Pesquisar_entry.grid(row=0,column=1,sticky=W)

      Btn_Pesquisar = gui.Button(clientes,text="Pesquisar")
      Btn_Pesquisar.grid(row=0,column=2)
    

      Codigo_Label = gui.Label(clientes,text="Codigo:", bg="#C0C0C0", font="Britannic 10 bold")
      Codigo_Label.grid(row=1,sticky=W,padx=8)

      Codigo_entry = gui.Entry(clientes, width = 10)
      Codigo_entry.grid(row=1,column=1,sticky=W)

      Nome_Label = gui.Label(clientes,text="Nome:", bg="#C0C0C0", font="Britannic 10 bold")
      Nome_Label.grid(row=2,column=0,sticky=W,padx=8)

      Nome_entry = gui.Entry(clientes,width = 50)
      Nome_entry.grid(row=2,column=1,sticky=W)


      DataNasc_Label = gui.Label(clientes,text="Data Nasc.:", bg="#C0C0C0", font="Britannic 10 bold")
      DataNasc_Label.grid(row=2,column=3,sticky=W,padx=8)

      DataNasc_entry = gui.Entry(clientes)
      DataNasc_entry.grid(row=2,column=4,sticky=W)

      CPF_Label = gui.Label(clientes,text="CPF:", bg="#C0C0C0", font="Britannic 10 bold")
      CPF_Label.grid(row=4,column=0,sticky=W,padx=8)

      CPF_entry = gui.Entry(clientes)
      CPF_entry.grid(row=4,column=1,sticky=W)

      RG_Label = gui.Label(clientes,text="RG:", bg="#C0C0C0", font="Britannic 10 bold")
      RG_Label.grid(row=4,column=3,sticky=W,padx=8)

      RG_entry = gui.Entry(clientes)
      RG_entry.grid(row=4,column=4,sticky=W)

      End_Label = gui.Label(clientes,text="Endereço:", bg="#C0C0C0", font="Britannic 10 bold")
      End_Label.grid(row=5,column=0,sticky=W,padx=8)

      End_entry = gui.Entry(clientes,width = 30)
      End_entry.grid(row=5,column=1,sticky=W)

      EndNun_Label = gui.Label(clientes,text="Nº:", bg="#C0C0C0", font="Britannic 10 bold")
      EndNun_Label.grid(row=5,column=3,sticky=W,padx=8)

      EndNun_entry = gui.Entry(clientes,width = 10)
      EndNun_entry.grid(row=5,column=4,sticky=W)


      Bairro_Label = gui.Label(clientes,text="Bairro:", bg="#C0C0C0", font="Britannic 10 bold")
      Bairro_Label.grid(row=7,column=0,sticky=W,padx=8)

      Bairro_entry = gui.Entry(clientes,width = 20)
      Bairro_entry.grid(row=7,column=1,sticky=W)


      Cep_Label = gui.Label(clientes,text="Cep:", bg="#C0C0C0", font="Britannic 10 bold")
      Cep_Label.grid(row=7,column=3,sticky=W,padx=8)

      Cep_entry = gui.Entry(clientes,width = 20)
      Cep_entry.grid(row=7,column=4,sticky=W)

      Cidade_Label = gui.Label(clientes,text="Cidade:", bg="#C0C0C0", font="Britannic 10 bold")
      Cidade_Label.grid(row=9,column=0,sticky=W,padx=8) 

      Cidade_entry = gui.Entry(clientes)
      Cidade_entry.grid(row=9,column=1,sticky=W)

      UF_Label = gui.Label(clientes,text="UF:", bg="#C0C0C0", font="Britannic 10 bold")
      UF_Label.grid(row=9,column=3,sticky=W,padx=8) 

      UF_entry = gui.Entry(clientes,width = 5)
      UF_entry.grid(row=9,column=4,sticky=W)

      Fone_Label = gui.Label(clientes,text="Telefone:", bg="#C0C0C0", font="Britannic 10 bold")
      Fone_Label.grid(row=10,column=0,sticky=W,padx=8)  

      Fone_entry = gui.Entry(clientes)
      Fone_entry.grid(row=10,column=1,sticky=W)   

      Cel_Label = gui.Label(clientes,text="Celular:", bg="#C0C0C0", font="Britannic 10 bold")
      Cel_Label.grid(row=10,column=3,sticky=W,padx=8)    

      Cel_entry = gui.Entry(clientes)
      Cel_entry.grid(row=10,column=4,sticky=W)

      Email_Label = gui.Label(clientes,text="Email:", bg="#C0C0C0", font="Britannic 10 bold")
      Email_Label.grid(row=11,column=0,sticky=W,padx=8) 

      Email_entry = gui.Entry(clientes,width = 40)
      Email_entry.grid(row=11,column=1,sticky=W)

      #botões
   

      Btn_Salvar = gui.Button(clientes,text="Salvar",width = 15)
      Btn_Salvar.grid(row=15)

      Btn_Editar = gui.Button(clientes,text="Editar",width = 15)
      Btn_Editar.grid(row=15,column=1,sticky=E)

      Btn_Sair = gui.Button(clientes,text="Sair",width = 15)
      Btn_Sair.grid(row=15,column=2,sticky=E)



    # ------------Loop End----------------------------------

      window.mainloop()




     