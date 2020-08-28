import tkinter as gui
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import mysql.connector

def MainProdutos():

    def CadastrarProdutos():
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
        mycursor = connection.cursor()

        # abrituindo os valores dos entry a uma variável-----------------
        ean = int(entryean.get())
        nome = str(entrynome.get())

        # verificando se o produto ja existem----------------------
        sqlselect = "select * from produtos"
        mycursor.execute(sqlselect)

        for i in mycursor:
                # print(i)
                pass
        if ean in i:
                messagebox.showwarning("Warning","Produto já cadastrado!")
                
        # elif nome in i:
                # messagebox.showwarning("Warning","Produto já cadastrado!\n\nEsse nome já pertence a um produto existente.")

        # inserindo os dados no banco -----------------------------------
        else:
            sqlinsert = "INSERT INTO  produtos (ean_produto, nome_produto, categoria_produto, descricão_produto, pre_venda_produto, pre_custo_produto, estoque) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(ean, nome, comboboxcat.get(), entrydescrição.get(), entryprevenda.get(), entryprecusto.get(), entryestoque.get())
            mycursor.execute(sqlinsert)

            sqlid = "select cod_produto from produtos where ean_produto = '{}';".format(ean) # sql para pegar o codigo do produto
            mycursor.execute(sqlid)
            for ind in mycursor:
                    print(mycursor)

            treeviewproduto.insert("","end",values=(ind, ean, nome, comboboxcat.get(), entrydescrição.get(), entryprevenda.get(), entryprecusto.get(), entryestoque.get())) # colando os dados no treeview

            entrycod.delete(0,END)
            entryean.delete(0,END)
            entrynome.delete(0,END)
            entrydescrição.delete(0,END)
            entryprecusto.delete(0,END)
            entryprevenda.delete(0,END)
            entryestoque.delete(0,END)
            comboboxcat.delete(0,END)

            time.sleep(2)
            messagebox.showinfo(title="Info",message="Usuário cadastrado com sucesso!")
            # Texto_label["text"] = "Usuário cadastrado com sucesso!"

            mycursor.close()
            connection.commit()
            connection.close()





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

    #=================labels e entrys========================
    lblanchonetename = Label(window, text="Sistema Lanchonete", bg="#DCDCDC", fg="#363636", bd=0.01, font="Broadway 35 bold")
    lblanchonetename.place(x=100, y=0)
    #codigo
    labelcod = gui.Label(frame1,text="Cód. Produto:", bg="#C0C0C0", font="Britannic 10 bold")
    labelcod.grid(row=0,column=0,sticky=W) # sticky -> para ficar um pouco mais para o oeste

    entrycod = gui.Entry(frame1, width=35, bd=4, state="disabled")
    entrycod.grid(row=0, column=1,padx=5,pady=3,ipady=3) # ipady -> para altura do entry | padxe pady -> espaço ao redor
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

    comboboxcat = ttk.Combobox(frame1, width=33, values="Lanches Salgados Doces Bebidas") # adicionando um Combobox
    comboboxcat.set("Lanches") # o combobox inicia vazio se não for selecionado uma opção para ele iniciar | para fazer isso usa-se o .set
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

    entrydescrição = gui.Text(frame1, width=30, height=5, bd=4)
    entrydescrição.grid(row=4, column=1,padx=5,pady=3,ipady=3)

    #=================botões==================================
    btcliente = gui.Button(frame1,text="Sair", fg="red", bg="#C0C0C0", padx=20, pady=2, borderwidth=5)
    btcliente.place(x=10,y=300)
    btfuncionario = gui.Button(frame1,text="Cadastrar", fg="green", bg="#C0C0C0", padx=20, pady=2, borderwidth=5, command=CadastrarProdutos)
    btfuncionario.place(x=90,y=300)

    #=================treeview==================================
    treeviewproduto = ttk.Treeview(frame2,columns=('id','ean','nome','cat','precovenda','precusto', 'estq', 'desc'),show='headings')
    treeviewproduto.column('id',minwidth=0,width=65)
    treeviewproduto.column('ean',minwidth=0,width=65)
    treeviewproduto.column('nome',minwidth=0,width=60)
    treeviewproduto.column('cat',minwidth=0,width=60)
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
MainProdutos()