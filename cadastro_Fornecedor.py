
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image # pip install Pillow
import mysql.connector


def MainFornecedor():
  # ------------Opening Window----------------------------------
  window = Toplevel()
  window.title("Lanchonete | Fornecedor")
  window.iconbitmap("imagens/ico.lanchonete.ico")
  window.configure(bg="#DCDCDC")
  # window.protocol("WM_DELETE_WINDOW")
  window.resizable(False,False) 
  window.geometry("850x500") # WxH
  

  def Ultimocodigo(): # Pega o maior valor da coluna cod_pedido para colocar na entry Cod           

    connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
    mycursor = connection.cursor()
    sqlid = "SELECT MAX(cod_fornecedor) FROM fornecedor"
    mycursor.execute(sqlid)
    for i in mycursor:
      print(i)
    if  i[0] ==  None :
      i = 0 
    ultimocod = i
    Codigo_entry["state"] = "normal"
    Codigo_entry.delete(0,END)  
    Codigo_entry.insert(0,ultimocod[0]+1)
    Codigo_entry["state"] = "disabled"

  
  def BuscarFornecedor():
    connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
    mycursor = connection.cursor()

    sqlBuscarFornecedor = "SELECT * FROM fornecedor WHERE cod_fornecedor = {}".format(PesquisarFornecedor_entry.get())
    mycursor.execute(sqlBuscarFornecedor)

    for data in mycursor:
      cod = data[0]
      razao_social = data[1]
      nome_fantasia = data[2]
      cpf_cnpj = data[3]
      ie = data[4]
      end = data[5]
      num = data[6]
      bairro = data[7]
      cep = data[8]
      cidade = data[9]
      uf = data[10]
      fone = data[11]
      email = data[12]

      Codigo_entry["state"] = "normal"
      Codigo_entry.delete(0,END)
      Codigo_entry.insert(0,cod)
      Codigo_entry["state"] = "disabled"

      razao_entry["state"] = "normal"
      razao_entry.delete(0,END)
      razao_entry.insert(0,razao_social)
      razao_entry["state"] = "disabled"

      Nome_entry["state"] = "normal"
      Nome_entry.delete(0,END)
      Nome_entry.insert(0,nome_fantasia)
      Nome_entry["state"] = "disabled"

      CPF_entry["state"] = "normal"
      CPF_entry.delete(0,END)
      CPF_entry.insert(0,cpf_cnpj)
      CPF_entry["state"] = "disabled"

      ie_entry["state"] = "normal"
      ie_entry.delete(0,END)
      ie_entry.insert(0,ie)
      ie_entry["state"] = "disabled"

      End_entry["state"] = "normal"
      End_entry.delete(0,END)
      End_entry.insert(0,end)
      End_entry["state"] = "disabled"

      EndNun_entry["state"] = "normal"
      EndNun_entry.delete(0,END)
      EndNun_entry.insert(0,num)
      EndNun_entry["state"] = "disabled"

      Bairro_entry["state"] = "normal"
      Bairro_entry.delete(0,END)
      Bairro_entry.insert(0,bairro)
      Bairro_entry["state"] = "disabled"

      Cep_entry["state"] = "normal"
      Cep_entry.delete(0,END)
      Cep_entry.insert(0,cep)
      Cep_entry["state"] = "disabled"

      Cidade_entry["state"] = "normal"
      Cidade_entry.delete(0,END)
      Cidade_entry.insert(0,cidade)
      Cidade_entry["state"] = "disabled"

      UF_entry["state"] = "normal"
      UF_entry.delete(0,END)
      UF_entry.insert(0,uf)
      UF_entry["state"] = "disabled"

      Fone_entry["state"] = "normal"
      Fone_entry.delete(0,END)
      Fone_entry.insert(0,fone)
      Fone_entry["state"] = "disabled"

      Email_entry["state"] = "normal"
      Email_entry.delete(0,END)
      Email_entry.insert(0,email)
      Email_entry["state"] = "disabled"

      
      # razao_entry["state"] = "disabled"
      # Nome_entry["state"] = "disabled"
      # CPF_entry["state"] = "disabled"
      # ie_entry["state"] = "disabled"
      # End_entry["state"] = "disabled"
      # EndNun_entry["state"] = "disabled"
      # Bairro_entry["state"] = "disabled"
      # Cep_entry["state"] = "disabled"
      # Cidade_entry["state"] = "disabled"
      # UF_entry["state"] = "disabled"
      # Fone_entry["state"] = "disabled"
      # Email_entry["state"] = "disabled"

  def InsertFornecedor():
    cod =Codigo_entry.get()
    razao_social = razao_entry.get()
    nome_fantasia = Nome_entry.get()
    cpf_cnpj = CPF_entry.get()
    ie = ie_entry.get()
    end = End_entry.get()
    num = EndNun_entry.get()
    bairro = Bairro_entry.get()
    cep = Cep_entry.get()
    cidade = Cidade_entry.get()
    uf = UF_entry.get()
    fone = Fone_entry.get()
    email = Email_entry.get()


    connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
    mycursor = connection.cursor()

    sqlsalvarfornecedor = "INSERT INTO fornecedor(cod_fornecedor,razao_social,nome_fantasia,cpf_cnpj,ie_fornecedor,end_fornecedor,nunend_fornecedor,bairro_fornecedor,cep_fornecedor,cidade_fornecedor,uf_fornecedor,fone_fornecedor,email_fornecedor) VALUES( '{}',  '{}',  '{}',  '{}',  '{}',  '{}',  '{}',  '{}',  '{}',  '{}',  '{}', '{}', '{}')".format(cod,razao_social,nome_fantasia,cpf_cnpj,ie,end,num,bairro,cep,cidade,uf,fone,email)
    print(sqlsalvarfornecedor)
    mycursor.execute(sqlsalvarfornecedor)  

    mycursor.close()
    connection.commit()
    connection.close()
    

    razao_entry.delete(0,END)
    Nome_entry.delete(0,END)
    CPF_entry.delete(0,END)
    ie_entry.delete(0,END)
    End_entry.delete(0,END)
    EndNun_entry.delete(0,END)
    Bairro_entry.delete(0,END)
    Cep_entry.delete(0,END)
    Cidade_entry.delete(0,END)
    UF_entry.delete(0,END)
    Fone_entry.delete(0,END)
    Email_entry.delete(0,END)
    
    # razao_entry["state"] = "disabled"
    # Nome_entry["state"] = "disabled"
    # CPF_entry["state"] = "disabled"
    # ie_entry["state"] = "disabled"
    # End_entry["state"] = "disabled"
    # EndNun_entry["state"] = "disabled"
    # Bairro_entry["state"] = "disabled"
    # Cep_entry["state"] = "disabled"
    # Cidade_entry["state"] = "disabled"
    # UF_entry["state"] = "disabled"
    # Fone_entry["state"] = "disabled"
    # Email_entry["state"] = "disabled"

    Ultimocodigo()

    messagebox.showinfo(title="Aviso",message="Cadastro atualizado")

  def Editar():
  
    
    razao_entry["state"] = "normal"
    Nome_entry["state"] = "normal"
    CPF_entry["state"] = "normal"
    ie_entry["state"] = "normal"
    End_entry["state"] = "normal"
    EndNun_entry["state"] = "normal"
    Bairro_entry["state"] = "normal"
    Cep_entry["state"] = "normal"
    Cidade_entry["state"] = "normal"
    UF_entry["state"] = "normal"
    Fone_entry["state"] = "normal"
    Email_entry["state"] = "normal"

  def UpdateFornecedor():
    cod =Codigo_entry.get()
    razao_social = razao_entry.get()
    nome_fantasia = Nome_entry.get()
    cpf_cnpj = CPF_entry.get()
    ie = ie_entry.get()
    end = End_entry.get()
    num = EndNun_entry.get()
    bairro = Bairro_entry.get()
    cep = Cep_entry.get()
    cidade = Cidade_entry.get()
    uf = UF_entry.get()
    fone = Fone_entry.get()
    email = Email_entry.get()


    connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
    mycursor = connection.cursor()
    Codigo_entry["state"] = "normal"
    sqlsalvarfornecedor = "UPDATE fornecedor SET  cod_fornecedor = '{}',razao_social = '{}',nome_fantasia = '{}',cpf_cnpj = '{}',ie_fornecedor = '{}',end_fornecedor = '{}',nunend_fornecedor = '{}',bairro_fornecedor = '{}',cep_fornecedor = '{}', cidade_fornecedor = '{}', uf_fornecedor = '{}',fone_fornecedor = '{}',email_fornecedor = '{}' WHERE cod_fornecedor='{}' ".format(cod,razao_social,nome_fantasia,cpf_cnpj,ie,end,num,bairro,cep,cidade,uf,fone,email,Codigo_entry.get())
    print(sqlsalvarfornecedor)
    mycursor.execute(sqlsalvarfornecedor)  

    mycursor.close()
    connection.commit()
    connection.close()
    messagebox.showinfo(title="Aviso",message="Cadastro atualizado")
    Codigo_entry["state"] = "disabled"
    razao_entry["state"] = "disabled"
    Nome_entry["state"] = "disabled"
    CPF_entry["state"] = "disabled"
    ie_entry["state"] = "disabled"
    End_entry["state"] = "disabled"
    EndNun_entry["state"] = "disabled"
    Bairro_entry["state"] = "disabled"
    Cep_entry["state"] = "disabled"
    Cidade_entry["state"] = "disabled"
    UF_entry["state"] = "disabled"
    Fone_entry["state"] = "disabled"
    Email_entry["state"] = "disabled"


  # ------------Widgets----------------------------------
  #labels e entrys
 

  lblanchonetename = Label(window, text="Sistema Lanchonete", bg="#DCDCDC", fg="#363636", bd=0.01, font="Broadway 35 bold")
  lblanchonetename.grid(row=0,column=0,columnspan=10)
  
  Codigo_Label = Label(window,text="Codigo:", bg="#DCDCDC", font="Britannic 10 bold")
  Codigo_Label.grid(row=1,column=0, sticky=W,padx=10)

  Codigo_entry = Entry(window, width =10, bd=4)
  Codigo_entry.grid(row=1,column=1,sticky=W,padx=2,ipady=3, pady=5)
  Ultimocodigo() # Carrega proximo codigo

  PesquisarFornecedor_Label = Label(window,text="Pesquisar Fornecedor:", bg="#DCDCDC", font="Britannic 10 bold")
  PesquisarFornecedor_Label.grid(row=1,column=2, sticky=W,padx=10)

  PesquisarFornecedor_entry = Entry(window, width=8, bd=4)
  PesquisarFornecedor_entry.grid(row=1,column=3,sticky=W,padx=2,ipady=3, pady=5)
  
  Bt_Pesquisar = Button(window,text="Pesquisar", width= 8, bg="#DCDCDC", padx=20, pady=2, borderwidth=4,command=BuscarFornecedor)
  Bt_Pesquisar.place(x=640,y=60)
  # Bt_Pesquisar.grid(row=1,column=5,sticky=W,rowspan=1)


  razao_Label = Label(window,text="Razão social:", bg="#DCDCDC", font="Britannic 10 bold")
  razao_Label.grid(row=2,column=0,sticky=E,padx=10)

  razao_entry = Entry(window, width =45, bd=4)
  razao_entry.grid(row=2,column=1,sticky=W,padx=2,ipady=3)

  Nome_Label = Label(window,text="Nome fantasia:", bg="#DCDCDC", font="Britannic 10 bold")
  Nome_Label.grid(row=2,column=2,sticky=E)

  Nome_entry = Entry(window, width =30, bd=4)
  Nome_entry.grid(row=2,column=3,sticky=W,padx=2,ipady=3)

  CPF_Label = Label(window,text="CPF/CNPJ:", bg="#DCDCDC", font="Britannic 10 bold")
  CPF_Label.grid(row=4,column=0,sticky=W,padx=10)

  CPF_entry = Entry(window, width =30, bd=4)
  CPF_entry.grid(row=4,column=1,sticky=W,padx=2,ipady=3, pady=5)

  ie_Label = Label(window,text="IE:", bg="#DCDCDC", font="Britannic 10 bold")
  ie_Label.grid(row=4,column=2,sticky=E,columnspan=1)

  ie_entry = Entry(window, width =30, bd=4)
  ie_entry.grid(row=4,column=3,sticky=W,padx=2,ipady=3)

  End_Label = Label(window,text="Endereço:", bg="#DCDCDC", font="Britannic 10 bold")
  End_Label.grid(row=6,column=0,sticky=W,padx=10)

  End_entry = Entry(window, width =45, bd=4)
  End_entry.grid(row=6,column=1,sticky=W,padx=2,ipady=3)

  EndNun_Label = Label(window,text="Nº:", bg="#DCDCDC", font="Britannic 10 bold")
  EndNun_Label.grid(row=6,column=2,sticky=E)

  EndNun_entry = Entry(window, width = 10, bd=4)
  EndNun_entry.grid(row=6,column=3,sticky=W,padx=2,ipady=3)


  Bairro_Label = Label(window,text="Bairro:", bg="#DCDCDC", font="Britannic 10 bold")
  Bairro_Label.grid(row=7,column=0,sticky=W,padx=10)

  Bairro_entry = Entry(window, width =30, bd=4)
  Bairro_entry.grid(row=7,column=1,sticky=W,padx=2,ipady=3, pady=5)

  Cep_Label = Label(window,text="Cep:", bg="#DCDCDC", font="Britannic 10 bold")
  Cep_Label.grid(row=7,column=2,sticky=E)

  Cep_entry = Entry(window, width =30, bd=4)
  Cep_entry.grid(row=7,column=3,sticky=W,padx=2,ipady=3)

  Cidade_Label = Label(window,text="Cidade:", bg="#DCDCDC", font="Britannic 10 bold")
  Cidade_Label.grid(row=9,column=0,sticky=W,padx=10) 

  Cidade_entry = Entry(window, width =30, bd=4)
  Cidade_entry.grid(row=9,column=1,sticky=W,padx=2,ipady=3)

  UF_Label = Label(window,text="UF:", bg="#DCDCDC", font="Britannic 10 bold")
  UF_Label.grid(row=9,column=2,sticky=E) 

  UF_entry = Entry(window, width =5, bd=4)
  UF_entry.grid(row=9,column=3,sticky=W,padx=2,ipady=3)

  Fone_Label = Label(window,text="Telefone:", bg="#DCDCDC", font="Britannic 10 bold")
  Fone_Label.grid(row=10,column=0,sticky=W,padx=10)  

  Fone_entry = Entry(window, width =30, bd=4)
  Fone_entry.grid(row=10,column=1,sticky=W,padx=2,ipady=3, pady=5)   

  Email_Label = Label(window,text="Email:", bg="#DCDCDC", font="Britannic 10 bold")
  Email_Label.grid(row=11,column=0,sticky=W,padx=10) 

  Email_entry = Entry(window, width =45, bd=4)
  Email_entry.grid(row=11,column=1,sticky=W,padx=2,ipady=3)


  #botões
  Bt_cadastrar = Button(window,text="Cadastrar", width= 8, bg="#DCDCDC", padx=20, pady=2, borderwidth=4,command=InsertFornecedor)
  Bt_cadastrar.grid(row=12,column=0,sticky=W,padx=10,ipady=2, pady=30)
  
  Bt_editar = Button(window,text="Editar", width= 8, bg="#DCDCDC", padx=20, pady=2, borderwidth=4,command=Editar)
  Bt_editar.grid(row=12,column=1,sticky=W,padx=10,ipady=2, pady=30)

  Bt_editar = Button(window,text="Salvar", width= 8, bg="#DCDCDC", padx=20, pady=2, borderwidth=4,command=UpdateFornecedor)
  Bt_editar.grid(row=12,column=2,sticky=W,padx=10,ipady=2, pady=30)
  
  

  window.mainloop()
