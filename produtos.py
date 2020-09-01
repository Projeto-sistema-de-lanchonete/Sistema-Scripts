import tkinter as gui
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import mysql.connector
import pymysql
import time

def MainProdutos():
        # Pega o maior valor da coluna cod_produtos para colocar na entry Cod
    connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
    mycursor = connection.cursor()
    sqlid = "SELECT MAX(cod_produto) FROM produtos"
    mycursor.execute(sqlid)
    for i in mycursor:
        print(i)
    teste = i

    def VisualisarProddutos():
         treeviewproduto.delete(*treeviewproduto.get_children()) #limpa a lista
         connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
         mycursor = connection.cursor()   
         sqlid = "select * from produtos;"# sql para pegar os produto
         mycursor.execute(sqlid)
               
         for viwer in mycursor:
          treeviewproduto.insert("","end",values=(viwer))
     
    def CadastrarProdutos():
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
        mycursor = connection.cursor()


        # abrituindo os valores dos entry a uma variável-----------------
        ean = int(entryean.get())
        nome = str(entrynome.get())


        # verificando se o produto ja existem----------------------
        sqlselect = "select * from produtos where ean_produto like {};".format(ean)
        mycursor.execute(sqlselect)
        valido = mycursor.fetchall() # busca todas as linhas de um resultado de consulta. Ele retorna todas as linhas como uma lista de tuplas. Uma lista vazia é retornada se não houver nenhum registro para buscar.

        if len(valido) > 0:
                messagebox.showwarning("Warning","Produto já cadastrado!")  

        else:   # inserindo os dados no banco -----------------------------------
                sqlinsert = "INSERT INTO  produtos (ean_produto, nome_produto, categoria_produto, descricão_produto, pre_venda_produto, pre_custo_produto, estoque) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(ean, nome, comboboxcat.get(), entrydescrição.get("1.0",END), entryprevenda.get(), entryprecusto.get(), entryestoque.get())
                mycursor.execute(sqlinsert)

               
                entrycod["state"] ="normal"
                entrycod.delete(0,END)
                entrycod.insert(0,teste[0]+2)
                entrycod["state"] ="disabled"
                entryean.delete(0,END)
                entrynome.delete(0,END)
                comboboxcat.set("Selecione")
                entrydescrição.delete("1.0",END)
                entryprecusto.delete(0,END)
                entryprevenda.delete(0,END)
                entryestoque.delete(0,END)

                time.sleep(2)
                messagebox.showinfo(title="Info",message="Produto cadastrado com sucesso!")
                
                

        mycursor.close()
        connection.commit()
        connection.close()
                
        # elif nome in i:
                # messagebox.showwarning("Warning","Produto já cadastrado!\n\nEsse nome já pertence a um produto existente.")

    def ExcluirProdutos():
            connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()

            codProd = str(cod_entry.get()) 

            sqldelete = "delete from produtos where cod_produto = {};".format(codProd)
            mycursor.execute(sqldelete)
           # print(sqldelete)
            mycursor.close()
            connection.commit()
            connection.close()

            cod_entry.delete(0, END)

            time.sleep(2)
            messagebox.showinfo("Info","Produto excluido.")

     

    def EditarProdutos():
        def UpdateProdutos():
        
            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()


            entrycod["state"] ="normal"
            cod = entrycod.get()
            entrycod["state"] ="disabled"    
            ean = entryean.get()
            nome = entrynome.get()
           
            prevenda = entryprevenda.get()
            precusto = entryprecusto.get()
            estoque = entryestoque.get()
            

             # Script de Update
            sqlupdate = "UPDATE produtos SET  ean_produto = {},nome_produto ='{}', categoria_produto='{}', descricão_produto ='{}', pre_venda_produto = {}, pre_custo_produto = {}, estoque = {} where cod_produto ={}".format(ean,nome, comboboxcat.get(),entrydescrição.get("1.0",END),prevenda,precusto,estoque,cod)
            print(sqlupdate)
            mycursor.execute(sqlupdate)

            mycursor.close()
            connection.commit()
            connection.close()          


        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
        mycursor = connection.cursor()

        codProd = str(cod_entry.get()) 

        sqlPesquisar = "SELECT * FROM produtos where cod_produto= {}".format(codProd)
        mycursor.execute(sqlPesquisar)

        for produto in mycursor:
          print(produto)

        window = gui.Tk()
        window.title("Lanchonete | Editar Produtos")
        window.iconbitmap("imagens/ico.lanchonete.ico")
        window.geometry("770x300") # WxH
        window.resizable(False,False)
        window.configure(bg="#DCDCDC")

        #=================notebook========================
        # mynot  = ttk.Notebook(window, width= 710, height=450) # criando notebook
        # mynot.pack(pady=65)

        # ------------Frames----------------------------------
       
        #=================labels e entrys========================
        # lblanchonetename = Label(window, text="Sistema Lanchonete", bg="#DCDCDC", fg="#363636", bd=0.01, font="Broadway 35 bold")
        # lblanchonetename.place(x=100, y=0)
        #codigo
        labelcod = gui.Label(window,text="Cód. Produto:",  font="Britannic 10 bold")
        labelcod.grid(row=0,column=0,sticky=W) # sticky -> para ficar um pouco mais para o oeste

        
        entrycod = gui.Entry(window, width=35, bd=4)# state="disabled")
        entrycod.grid(row=0, column=1,padx=5,pady=3,ipady=3) # ipady -> para altura do entry | padxe pady -> espaço ao redor
    
        #EAN
        labelean = gui.Label(window,text="EAN/GTIN:",font="Britannic 10 bold")
        labelean.grid(row=1,column=0,sticky=W)

        entryean = gui.Entry(window, width=35, bd=4)
        entryean.grid(row=1, column=1,padx=5,pady=3,ipady=3)
        #nome
        labelnome = gui.Label(window,text="Nome:",font="Britannic 10 bold")
        labelnome.grid(row=2,column=0,sticky=W)

        entrynome = gui.Entry(window, width=35, bd=4)
        entrynome.grid(row=2, column=1,padx=5,pady=3,ipady=3)
        #categoria
        labelcat = gui.Label(window,text="Categoria:",font="Britannic 10 bold")
        labelcat.grid(row=3,column=0,sticky=W)

        comboboxcat = ttk.Combobox(window, width=33, values="Lanches Salgados Doces Bebidas", state="readonly") # adicionando um Combobox
        #comboboxcat.set("Selecione") # o combobox inicia vazio se não for selecionado uma opção para ele iniciar | para fazer isso usa-se o .set
        comboboxcat.grid(row=3, column=1,padx=5,pady=3,ipady=3)
        #preço de venda
        labelprevenda = gui.Label(window,text="Preço de venda:", font="Britannic 10 bold")
        labelprevenda.grid(row=0,column=2,sticky=W)

        entryprevenda = gui.Entry(window, width=35, bd=4)
        entryprevenda.grid(row=0, column=3,padx=5,pady=3,ipady=3)
        #preço de custo
        labelprecusto = gui.Label(window,text="Preço de custo:", font="Britannic 10 bold")
        labelprecusto.grid(row=1,column=2,sticky=W)

        entryprecusto = gui.Entry(window, width=35, bd=4)
        entryprecusto.grid(row=1, column=3,padx=5,pady=3,ipady=3)
        #estoque
        labelestoque = gui.Label(window,text="Estoque atual:", font="Britannic 10 bold")
        labelestoque.grid(row=2,column=2,sticky=W)

        entryestoque = gui.Entry(window, width=35, bd=4)
        entryestoque.grid(row=2, column=3,padx=5,pady=3,ipady=3)
        #descrição
        labeldescrição = gui.Label(window,text="Descrição:", font="Britannic 10 bold")
        labeldescrição.grid(row=4,column=0,sticky=W)

        entrydescrição = gui.Text(window, width=28, height=5, bd=4)
        entrydescrição.grid(row=4, column=1,padx=5,pady=3,ipady=3)

        btSalvar = gui.Button(window,text="Salvar", fg="green", bg="#C0C0C0", padx=20, pady=2, borderwidth=5, command=UpdateProdutos)
        btSalvar.grid(row=6, column=4,pady=8)

        # entrycod.insert(0,produto[0])
        entrycod.insert(0, "Automático")
        entrycod["state"] ="disabled" # desativar o entry
        entryean.insert(0,produto[1])
        entrynome.insert(0,produto[2])
        comboboxcat.set(produto[3])
        entrydescrição.insert(END,produto[4],'')
        entryprevenda.insert(0,produto[5])
        entryprecusto.insert(0,produto[6])
        entryestoque.insert(0,produto[7])
    







    # ------------Opening Window----------------------------------
    window = gui.Tk()
    window.title("Lanchonete | Produtos")
    window.iconbitmap("imagens/ico.lanchonete.ico")
    window.geometry("750x500") # WxH
    window.resizable(False,False)
    window.configure(bg="#DCDCDC")

    #=================notebook========================
    mynot  = ttk.Notebook(window, width= 710, height=450) # criando notebook
    mynot.pack(pady=65)

    # ------------Frames----------------------------------
    frame1 = gui.Frame(mynot,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
    frame1.place(relwidth=0.80,relheight=0.73,relx=0.1,rely=0.15)
    mynot.add(frame1, text="Cadastrar produtos") # adicionando frame no notebook

    frame2 = gui.Frame(mynot,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
    frame2.place(relwidth=0.80,relheight=0.73,relx=0.1,rely=0.15)
    mynot.add(frame2, text="Visualisar produtos")

    frame3 = gui.Frame(mynot,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
    frame3.place(relwidth=0.80,relheight=0.73,relx=0.1,rely=0.15)
    mynot.add(frame3, text="Excluir/Editar produtos")

    #=================labels e entrys========================
    lblanchonetename = Label(window, text="Sistema Lanchonete", bg="#DCDCDC", fg="#363636", bd=0.01, font="Broadway 35 bold")
    lblanchonetename.place(x=100, y=0)
    #codigo
    labelcod = gui.Label(frame1,text="Cód. Produto:", bg="#C0C0C0", font="Britannic 10 bold")
    labelcod.grid(row=0,column=0,sticky=W) # sticky -> para ficar um pouco mais para o oeste

    entrycod = gui.Entry(frame1, width=35, bd=4)# state="disabled"
    entrycod.grid(row=0, column=1,padx=5,pady=3,ipady=3) # ipady -> para altura do entry | padxe pady -> espaço ao redor
    # entrycod.insert(0,teste[0]+1)
    entrycod.insert(0, "Automático") # inserindo valor no entry
    entrycod["state"] ="disabled" # desativar o entry
    #EAN
    labelean = gui.Label(frame1,text="EAN/GTIN:", bg="#C0C0C0", font="Britannic 10 bold")
    labelean.grid(row=1,column=0,sticky=W)

    entryean = gui.Entry(frame1, width=35, bd=4)
    entryean.grid(row=1, column=1,padx=5,pady=3,ipady=3)
    #nome
    labelnome = gui.Label(frame1,text="Nome:", bg="#C0C0C0", font="Britannic 10 bold")
    labelnome.grid(row=2,column=0,sticky=W)

    entrynome = gui.Entry(frame1, width=35, bd=4)
    entrynome.grid(row=2, column=1,padx=5,pady=3,ipady=3)
    #categoria
    labelcat = gui.Label(frame1,text="Categoria:", bg="#C0C0C0", font="Britannic 10 bold")
    labelcat.grid(row=3,column=0,sticky=W)

    comboboxcat = ttk.Combobox(frame1, width=33, values="Lanches Salgados Doces Bebidas", state="readonly") # adicionando um Combobox
    comboboxcat.set("Selecione") # o combobox inicia vazio se não for selecionado uma opção para ele iniciar | para fazer isso usa-se o .set
    comboboxcat.grid(row=3, column=1,padx=5,pady=3,ipady=3)
    #preço de venda
    labelprevenda = gui.Label(frame1,text="Preço de venda:", bg="#C0C0C0", font="Britannic 10 bold")
    labelprevenda.grid(row=0,column=2,sticky=W)

    entryprevenda = gui.Entry(frame1, width=35, bd=4)
    entryprevenda.grid(row=0, column=3,padx=5,pady=3,ipady=3)
    #preço de custo
    labelprecusto = gui.Label(frame1,text="Preço de custo:", bg="#C0C0C0", font="Britannic 10 bold")
    labelprecusto.grid(row=1,column=2,sticky=W)

    entryprecusto = gui.Entry(frame1, width=35, bd=4)
    entryprecusto.grid(row=1, column=3,padx=5,pady=3,ipady=3)
    #estoque
    labelestoque = gui.Label(frame1,text="Estoque atual:", bg="#C0C0C0", font="Britannic 10 bold")
    labelestoque.grid(row=2,column=2,sticky=W)

    entryestoque = gui.Entry(frame1, width=35, bd=4)
    entryestoque.grid(row=2, column=3,padx=5,pady=3,ipady=3)
    #descrição
    labeldescrição = gui.Label(frame1,text="Descrição:", bg="#C0C0C0", font="Britannic 10 bold")
    labeldescrição.grid(row=4,column=0,sticky=W)

    entrydescrição = gui.Text(frame1, width=28, height=5, bd=4)
    entrydescrição.grid(row=4, column=1,padx=5,pady=3,ipady=3)

    codexcluir = Label(frame3,text="Cod. do produto:", bg="#C0C0C0", font="Britannic 10 bold")
    codexcluir.grid(row=2,column=0, pady=20, padx=10)
    
    cod_entry = Entry(frame3, width=35, bd=4)
    cod_entry.grid(row=2,column=1,ipady=3)

    #=================botões==================================
    btcliente = gui.Button(frame1,text="Sair", fg="red", bg="#C0C0C0", width= 10, padx=20, pady=2, borderwidth=5)
    btcliente.place(x=10,y=300)

    btfuncionario = gui.Button(frame1,text="Cadastrar", fg="green", bg="#C0C0C0", width= 10, padx=20, pady=2, borderwidth=5, command=CadastrarProdutos)
    btfuncionario.place(x=145,y=300)

    btfuncionarioo = gui.Button(frame2,text="Visualizar", fg="green", bg="#C0C0C0", width= 10, padx=20, pady=2, borderwidth=5, command=VisualisarProddutos)
    btfuncionarioo.place(x=90,y=300)

    excluirprod = Button(frame3,text="Excluir",bg="#C0C0C0", width= 10, padx=20, pady=2, borderwidth=5,command=ExcluirProdutos)
    excluirprod.grid(row=3,column=0,rowspan=2,columnspan=4,padx=20,pady=(0,20))
    
    editarprod = Button(frame3,text="Editar", bg="#C0C0C0", width= 10, padx=22, pady=2, borderwidth=5,command=EditarProdutos)
    editarprod.grid(row=5,column=0,rowspan=2,columnspan=4)

    #=================treeview==================================
    treeviewproduto = ttk.Treeview(frame2,columns=('id','ean','nome','cat','desc', 'precovenda','precusto', 'estq'),show='headings')
    treeviewproduto.column('id',minwidth=0,width=65)
    treeviewproduto.column('ean',minwidth=0,width=70)
    treeviewproduto.column('nome',minwidth=0,width=75)
    treeviewproduto.column('cat',minwidth=0,width=65)
    treeviewproduto.column('precovenda',minwidth=0,width=60)
    treeviewproduto.column('precusto',minwidth=0,width=60)
    treeviewproduto.column('estq',minwidth=0,width=60)
    treeviewproduto.column('desc',minwidth=0,width=200)

    treeviewproduto.heading('id',text="Cód. Prod ")
    treeviewproduto.heading('ean',text="EAN/GTIN ")
    treeviewproduto.heading('nome',text="Nome ")
    treeviewproduto.heading('cat',text="Categ. ")
    treeviewproduto.heading('precovenda',text="Pr. Venda ")
    treeviewproduto.heading('precusto',text="Pr. Custo ")
    treeviewproduto.heading('estq',text="Estoque ")
    treeviewproduto.heading('desc',text="Descriçao ")
    treeviewproduto.pack()

    # ------------Loop End----------------------------------
    window.mainloop()
