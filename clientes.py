import tkinter as gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
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

            sqlcliente ="INSERT INTO clientes (cod_cliente, nome_cliente, datanasc_cliente , cpf_cliente, rg_cliente, end_cliente, nunend_cliente, bairro_cliente, cep_cliente, cidade_cliente, uf_cliente, fone_cliente, celular_cliente, email_cliente) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Codigo_entry.get(),Nome_entry.get(),data,CPF_entry.get(),RG_entry.get(),End_entry.get(),EndNun_entry.get(),Bairro_entry.get(),Cep_entry.get(),Cidade_entry.get(),UF_entry.get(),Fone_entry.get(),Cel_entry.get(),Email_entry.get())
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

            Bt_editar["state"] = "normal"
            Bt_excluir["state"] = "normal" 
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
      window.title("Lanchonete | Clientes")
      window.iconbitmap("imagens/ico.lanchonete.ico")
      window.configure(bg="#DCDCDC")
      # window.protocol("WM_DELETE_WINDOW")
      window.resizable(False,False) 
      window.geometry("750x500") # WxH

      #=================notebook========================
      mynot  = ttk.Notebook(window, width= 710, height=450) # criando notebook
      mynot.pack(pady=65)

      # ------------Frames----------------------------------
      frame1 = gui.Frame(mynot,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
      frame1.place(relwidth=0.99,relheight=0.90,relx=0.01,rely=0.15)
      mynot.add(frame1, text="Cadastrar clientes") # adicionando frame no notebook

      frame2 = gui.Frame(mynot,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
      frame2.place(relwidth=0.99,relheight=0.90,relx=0.01,rely=0.15)
      mynot.add(frame2, text="Visualisar clientes")

      # ------------Widgets----------------------------------
      #labels e entrys
      lblanchonetename = Label(window, text="Sistema Lanchonete", bg="#DCDCDC", fg="#363636", bd=0.01, font="Broadway 35 bold")
      lblanchonetename.place(x=100,y=0)
      

      Pesquisar_Label = gui.Label(frame1,text="Pesquisar:", bg="#C0C0C0", font="Britannic 10 bold")
      Pesquisar_Label.grid(sticky=W)

      Pesquisar_entry = gui.Entry(frame1, width =30, bd=4)
      Pesquisar_entry.grid(row=0,column=1,sticky=W,padx=2,ipady=3)

      Codigo_Label = gui.Label(frame1,text="Codigo:", bg="#C0C0C0", font="Britannic 10 bold")
      Codigo_Label.grid(row=1,sticky=W)

      Codigo_entry = gui.Entry(frame1, width =30, bd=4)
      Codigo_entry.grid(row=1,column=1,sticky=W,padx=2,ipady=3)
      Codigo_entry.insert(0,"Automático")
      Codigo_entry["state"] = "disabled"

      Nome_Label = gui.Label(frame1,text="Nome:", bg="#C0C0C0", font="Britannic 10 bold")
      Nome_Label.grid(row=2,column=0,sticky=W)

      Nome_entry = gui.Entry(frame1, width =20, bd=4)
      Nome_entry.grid(row=2,column=1,sticky=W,padx=2,ipady=3)


      DataNasc_Label = gui.Label(frame1,text="Data Nasc.:", bg="#C0C0C0", font="Britannic 10 bold")
      DataNasc_Label.grid(row=2,column=3,sticky=W)

      DataNasc_entry = gui.Entry(frame1, width =30, bd=4)
      DataNasc_entry.grid(row=2,column=4,sticky=W,padx=2,ipady=3)

      CPF_Label = gui.Label(frame1,text="CPF:", bg="#C0C0C0", font="Britannic 10 bold")
      CPF_Label.grid(row=4,column=0,sticky=W)

      CPF_entry = gui.Entry(frame1, width =30, bd=4)
      CPF_entry.grid(row=4,column=1,sticky=W,padx=2,ipady=3)

      RG_Label = gui.Label(frame1,text="RG:", bg="#C0C0C0", font="Britannic 10 bold")
      RG_Label.grid(row=4,column=3,sticky=W)

      RG_entry = gui.Entry(frame1, width =30, bd=4)
      RG_entry.grid(row=4,column=4,sticky=W,padx=2,ipady=3)

      End_Label = gui.Label(frame1,text="Endereço:", bg="#C0C0C0", font="Britannic 10 bold")
      End_Label.grid(row=5,column=0,sticky=W)

      End_entry = gui.Entry(frame1, width =25, bd=4)
      End_entry.grid(row=5,column=1,sticky=W,padx=2,ipady=3)

      EndNun_Label = gui.Label(frame1,text="Nº:", bg="#C0C0C0", font="Britannic 10 bold")
      EndNun_Label.grid(row=5,column=3,sticky=W)

      EndNun_entry = gui.Entry(frame1, width =30, bd=4)
      EndNun_entry.grid(row=5,column=4,sticky=W,padx=2,ipady=3)


      Bairro_Label = gui.Label(frame1,text="Bairro:", bg="#C0C0C0", font="Britannic 10 bold")
      Bairro_Label.grid(row=7,column=0,sticky=W)

      Bairro_entry = gui.Entry(frame1, width =30, bd=4)
      Bairro_entry.grid(row=7,column=1,sticky=W,padx=2,ipady=3)


      Cep_Label = gui.Label(frame1,text="Cep:", bg="#C0C0C0", font="Britannic 10 bold")
      Cep_Label.grid(row=7,column=3,sticky=W)

      Cep_entry = gui.Entry(frame1, width =30, bd=4)
      Cep_entry.grid(row=7,column=4,sticky=W,padx=2,ipady=3)

      Cidade_Label = gui.Label(frame1,text="Cidade:", bg="#C0C0C0", font="Britannic 10 bold")
      Cidade_Label.grid(row=9,column=0,sticky=W) 

      Cidade_entry = gui.Entry(frame1, width =30, bd=4)
      Cidade_entry.grid(row=9,column=1,sticky=W,padx=2,ipady=3)

      UF_Label = gui.Label(frame1,text="UF:", bg="#C0C0C0", font="Britannic 10 bold")
      UF_Label.grid(row=9,column=3,sticky=W) 

      UF_entry = gui.Entry(frame1, width =30, bd=4)
      UF_entry.grid(row=9,column=4,sticky=W,padx=2,ipady=3)

      Fone_Label = gui.Label(frame1,text="Telefone:", bg="#C0C0C0", font="Britannic 10 bold")
      Fone_Label.grid(row=10,column=0,sticky=W)  

      Fone_entry = gui.Entry(frame1, width =30, bd=4)
      Fone_entry.grid(row=10,column=1,sticky=W,padx=2,ipady=3)   

      Cel_Label = gui.Label(frame1,text="Celular:", bg="#C0C0C0", font="Britannic 10 bold")
      Cel_Label.grid(row=10,column=3,sticky=W)    

      Cel_entry = gui.Entry(frame1, width =30, bd=4)
      Cel_entry.grid(row=10,column=4,sticky=W,padx=2,ipady=3)

      Email_Label = gui.Label(frame1,text="Email:", bg="#C0C0C0", font="Britannic 10 bold")
      Email_Label.grid(row=11,column=0,sticky=W) 

      Email_entry = gui.Entry(frame1, width =30, bd=4)
      Email_entry.grid(row=11,column=1,sticky=W,padx=2,ipady=3)

      #botões
      Btn_Pesquisar = gui.Button(frame1,text="Pesquisar", width= 8, padx=10, bg="#C0C0C0", pady=2, borderwidth=5,command=PesquisarCliente)
      Btn_Pesquisar.grid(row=0,column=2)

      Bt_cadastrar = gui.Button(frame1,text="Cadastrar", width= 10, bg="#C0C0C0", padx=20, pady=2, borderwidth=5,command=CadastrarCliente)
      Bt_cadastrar.place(x=10,y=300)
      
      Bt_editar = gui.Button(frame1,text="Editar", width= 10, bg="#C0C0C0", padx=20, pady=2, borderwidth=5, state = "disabled")
      Bt_editar.place(x=145,y=300)

      Bt_excluir = gui.Button(frame1,text="Excluir",width = 10, bg="#C0C0C0", padx=20, pady=2, borderwidth=5, state = "disabled")
      Bt_excluir.place(x=280,y=300)

      Btn_Pesquisar = gui.Button(frame1,text="Sairr",width = 10, bg="#C0C0C0", padx=20, pady=2, borderwidth=5)
      Btn_Pesquisar.place(x=415,y=300)

      #=================treeview==================================
      treeviewclientes = ttk.Treeview(frame2,columns=('cod','nome','cpf','rg','dt. nasc','ende','nº','bairro', 'cidade','uf','cep','telefone', 'celular','email'),show='headings')
      treeviewclientes.column('cod',minwidth=0,width=65)
      treeviewclientes.column('nome',minwidth=0,width=70)
      treeviewclientes.column('cpf',minwidth=0,width=75)
      treeviewclientes.column('rg',minwidth=0,width=65)
      treeviewclientes.column('dt. nasc',minwidth=0,width=75)
      treeviewclientes.column('ende',minwidth=0,width=200)
      treeviewclientes.column('nº',minwidth=0,width=60)
      treeviewclientes.column('bairro',minwidth=0,width=65)
      treeviewclientes.column('cidade',minwidth=0,width=65)
      treeviewclientes.column('uf',minwidth=0,width=75)
      treeviewclientes.column('cep',minwidth=0,width=65)
      treeviewclientes.column('telefone',minwidth=0,width=60)
      treeviewclientes.column('celular',minwidth=0,width=60)
      treeviewclientes.column('email',minwidth=0,width=60)

      treeviewclientes.heading('cod',text="Cod.")
      treeviewclientes.heading('nome',text="Nome")
      treeviewclientes.heading('cpf',text="CPF")
      treeviewclientes.heading('rg',text="RG")
      treeviewclientes.heading('dt. nasc',text="Dt. Nasc.")
      treeviewclientes.heading('ende',text="Endereço")
      treeviewclientes.heading('nº',text="Nº")
      treeviewclientes.heading('bairro',text="Bairro")
      treeviewclientes.heading('cidade',text="Cidade")
      treeviewclientes.heading('uf',text="UF")
      treeviewclientes.heading('cep',text="CEP")
      treeviewclientes.heading('telefone',text="Tel.")
      treeviewclientes.heading('celular',text="Cel")
      treeviewclientes.heading('email',text="Email")
      treeviewclientes.pack()

      # ------------Loop End----------------------------------

      window.mainloop()




     