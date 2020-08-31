import tkinter as gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
import pymysql
import time
import datetime

def MainClientes():
      # Pega o maior valor da coluna cod_produtos para colocar na entry Cod
      connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
      mycursor = connection.cursor()
      sqlid = "SELECT MAX(cod_cliente) FROM clientes"
      mycursor.execute(sqlid)
      for i in mycursor:
            print(i)
      if  i[0] ==  None :
            i = 0 
      ultimocod = i

      def CadastrarCliente():
            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()
            
            Codigo_entry["state"] = "normal"
            data = DataNasc_entry.get()
           
            sqlcliente ="INSERT INTO clientes (cod_cliente, nome_cliente, datanasc_cliente , cpf_cliente, rg_cliente, end_cliente, nunend_cliente, bairro_cliente, cep_cliente, cidade_cliente, uf_cliente, fone_cliente, celular_cliente, email_cliente) VALUES ('{}','{}',STR_TO_DATE('{}','%Y-%m-%d'),'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Codigo_entry.get(),Nome_entry.get(),data,CPF_entry.get(),RG_entry.get(),End_entry.get(),EndNun_entry.get(),Bairro_entry.get(),Cep_entry.get(),Cidade_entry.get(),UF_entry.get(),Fone_entry.get(),Cel_entry.get(),Email_entry.get())
            mycursor.execute(sqlcliente)

            mycursor.close()
            connection.commit()
            connection.close()

            Codigo_entry.delete(0,END)

            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()
            sqlid = "SELECT MAX(cod_cliente) FROM clientes"
            mycursor.execute(sqlid)
            for i in mycursor:
                  print(i)
            ultimocod = i

            Codigo_entry.insert(0,ultimocod[0]+1)
            Codigo_entry["state"] = "disabled"

            Codigo_entry.delete(0,END)
            Nome_entry.delete(0,END)
            DataNasc_entry.delete(0,END)
            CPF_entry.delete(0,END)
            RG_entry.delete(0,END)
            End_entry.delete(0,END)
            EndNun_entry.delete(0,END)
            Bairro_entry.delete(0,END)
            Cep_entry.delete(0,END)
            Cidade_entry.delete(0,END)
            UF_entry.delete(0,END)
            Fone_entry.delete(0,END)
            Cel_entry.delete(0,END)
            Email_entry.delete(0,END)

      def  PesquisarCliente():
            
            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()

            sqlpesquisarcliente = "SELECT cod_cliente, nome_cliente, DATE_FORMAT(datanasc_cliente, '%d/%m/%Y'), cpf_cliente, rg_cliente, end_cliente, nunend_cliente, bairro_cliente, cep_cliente, cidade_cliente, uf_cliente, fone_cliente, celular_cliente, email_cliente FROM  clientes WHERE cod_cliente = {}".format(Pesquisar_entry.get())
            mycursor.execute(sqlpesquisarcliente)

            for cliente in mycursor:
                  print(cliente)

         
            Codigo_entry["state"] = "normal"
            Codigo_entry.delete(0,END)
            Codigo_entry.insert(0,cliente[0])
            Codigo_entry["state"] = "disabled"
            Nome_entry.insert(0,cliente[1])
            str(cliente[2])
            DataNasc_entry.insert(0,cliente[2])
            CPF_entry.insert(0,cliente[3])
            RG_entry.insert(0,cliente[4])
            End_entry.insert(0,cliente[5])
            EndNun_entry.insert(0,cliente[6])
            Bairro_entry.insert(0,cliente[7])
            Cep_entry.insert(0,cliente[8])
            Cidade_entry.insert(0,cliente[9])
            UF_entry.insert(0,cliente[10])
            Fone_entry.insert(0,cliente[11])
            Cel_entry.insert(0,cliente[12])
            Email_entry.insert(0,cliente[13])






      # ------------Opening Window----------------------------------
      window = gui.Tk()
      window.title("Lanchonete | Cadatro de Cliente")
      window.iconbitmap("imagens/ico.lanchonete.ico")
      window.configure(bg="#DCDCDC")
      window.protocol("WM_DELETE_WINDOW")
      window.resizable(False,False) 
      window.geometry("950x500") # WxH


      # ------------Frames----------------------------------
      clientes = gui.Frame(window,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
      clientes.place(relwidth=0.80,relheight=0.73,relx=0.1,rely=0.15)

      # ------------Widgets----------------------------------
      #labels
      lblanchonetename = Label(window, text="Sistema Lanchonete", bg="#DCDCDC", fg="#363636", bd=0.01, font="Broadway 35 bold")
      lblanchonetename.place(x=175,y=0)

      Pesquisar_Label = gui.Label(clientes,text="Pesquisar:", bg="#C0C0C0", font="Britannic 10 bold")
      Pesquisar_Label.grid(sticky=W,padx=8)

      Pesquisar_entry = gui.Entry(clientes, width =15)
      Pesquisar_entry.grid(row=0,column=1,sticky=W)

      Btn_Pesquisar = gui.Button(clientes,text="Pesquisar",command=PesquisarCliente)
      Btn_Pesquisar.grid(row=0,column=2)

      Codigo_Label = gui.Label(clientes,text="Codigo:", bg="#C0C0C0", font="Britannic 10 bold")
      Codigo_Label.grid(row=1,sticky=W,padx=8)


      Codigo_entry = gui.Entry(clientes, width = 10)
      Codigo_entry.grid(row=1,column=1,sticky=W)
      Codigo_entry.insert(0,ultimocod[0]+1)
      Codigo_entry["state"] = "disabled"

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


      Btn_Salvar = gui.Button(clientes,text="Salvar",width = 15,command=CadastrarCliente)
      Btn_Salvar.grid(row=15)

      Btn_Editar = gui.Button(clientes,text="Editar",width = 15)
      Btn_Editar.grid(row=15,column=1,sticky=E)

      Btn_Sair = gui.Button(clientes,text="Sair",width = 15)
      Btn_Sair.grid(row=15,column=2,sticky=E)



      # ------------Loop End----------------------------------

      window.mainloop()




     