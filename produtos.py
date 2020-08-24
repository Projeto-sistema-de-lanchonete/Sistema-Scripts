import tkinter as gui
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def MainProdutos():
    # ------------Opening Window----------------------------------
    window = gui.Tk()
    window.title("Lanchonete | Produtos")
    window.iconbitmap("imagens/ico.lanchonete.ico")
    window.geometry("750x500") # WxH
    window.resizable(False,False)
    window.configure(bg="#DCDCDC")

    #=================labels e entrys========================
    mynot  = ttk.Notebook(window, width= 710, height=450)
    mynot.pack(pady=65)

    # ------------Frames----------------------------------
    frame1 = gui.Frame(mynot,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
    frame1.place(relwidth=0.80,relheight=0.73,relx=0.1,rely=0.15)
    mynot.add(frame1, text="Dados do produto")

    frame2 = gui.Frame(mynot,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
    frame2.place(relwidth=0.80,relheight=0.73,relx=0.1,rely=0.15)
    mynot.add(frame2, text="visualisar produtos")

    #=================labels e entrys========================
    lblanchonetename = Label(window, text="Sistema Lanchonete", bg="#DCDCDC", fg="#363636", bd=0.01, font="Broadway 35 bold")
    lblanchonetename.place(x=100, y=0)
    #codigo
    labelcod = gui.Label(frame1,text="Cód. Produto:", bg="#C0C0C0", font="Britannic 10 bold")
    labelcod.grid(row=0,column=0,sticky=W) # sticky -> para ficar um pouco mais para o oeste

    entrycod = gui.Entry(frame1, width=35, bd=4)
    entrycod.grid(row=0, column=1,padx=5,pady=3,ipady=3) # ipady -> para altura do entry | padxe pady -> espaço ao redor
    #EAN
    labelean = gui.Label(frame1,text="EAN/GTIN:", bg="#C0C0C0", font="Britannic 10 bold")
    labelean.grid(row=1,column=0,sticky=W)

    entryean = gui.Entry(frame1, width=35, bd=4)
    entryean.grid(row=1, column=1,padx=5,pady=3,ipady=3)
    #nome
    labelnome = gui.Label(frame1,text="Nome:", bg="#C0C0C0", font="Britannic 10 bold")
    labelnome.grid(row=2,column=0,sticky=W)

    entryean = gui.Entry(frame1, width=35, bd=4)
    entryean.grid(row=2, column=1,padx=5,pady=3,ipady=3)
    #categoria
    labelcat = gui.Label(frame1,text="Categoria:", bg="#C0C0C0", font="Britannic 10 bold")
    labelcat.grid(row=3,column=0,sticky=W)

    comboboxcat = ttk.Combobox(frame1, width=33, values="categoria1 categoria2 categoria3") # adicionando um Combobox
    comboboxcat.set("categoria1") # o combobox inicia vazio se não for selecionado uma opção para ele iniciar | para fazer isso usa-se o .set
    comboboxcat.grid(row=3, column=1,padx=5,pady=3,ipady=3)
    #preço de venda
    labelprevenda = gui.Label(frame1,text="Preço de venda:", bg="#C0C0C0", font="Britannic 10 bold")
    labelprevenda.grid(row=0,column=2,sticky=W)

    entryprecusto = gui.Entry(frame1, width=35, bd=4)
    entryprecusto.grid(row=0, column=3,padx=5,pady=3,ipady=3)
    #preço de custo
    labelprecusto = gui.Label(frame1,text="Preço de custo:", bg="#C0C0C0", font="Britannic 10 bold")
    labelprecusto.grid(row=1,column=2,sticky=W)

    entryprecusto = gui.Entry(frame1, width=35, bd=4)
    entryprecusto.grid(row=1, column=3,padx=5,pady=3,ipady=3)
    #estoque
    labelestoque = gui.Label(frame1,text="Estoque atual:", bg="#C0C0C0", font="Britannic 10 bold")
    labelestoque.grid(row=2,column=2,sticky=W)

    entryprecusto = gui.Entry(frame1, width=35, bd=4)
    entryprecusto.grid(row=2, column=3,padx=5,pady=3,ipady=3)
    #descrição
    labeldescrição = gui.Label(frame1,text="Descrição:", bg="#C0C0C0", font="Britannic 10 bold")
    labeldescrição.grid(row=4,column=0,sticky=W)

    entrydescrição = gui.Text(frame1, width=30, height=5, bd=4)
    entrydescrição.grid(row=4, column=1,padx=5,pady=3,ipady=3)

    #=================botões==================================
    btcliente = gui.Button(frame1,text="Sair", fg="red", bg="#C0C0C0", padx=20, pady=2, borderwidth=5)
    btcliente.place(x=10,y=300)
    btfuncionario = gui.Button(frame1,text="Salvar", fg="green", bg="#C0C0C0", padx=20, pady=2, borderwidth=5)
    btfuncionario.place(x=90,y=300)

    #=================treeview==================================
    ShowItens_tv = ttk.Treeview(frame2,columns=('id','ean','nome','cat','precovenda','precusto', 'estq', 'desc'),show='headings')
    ShowItens_tv.column('id',minwidth=0,width=65)
    ShowItens_tv.column('ean',minwidth=0,width=65)
    ShowItens_tv.column('nome',minwidth=0,width=60)
    ShowItens_tv.column('cat',minwidth=0,width=60)
    ShowItens_tv.column('precovenda',minwidth=0,width=60)
    ShowItens_tv.column('precusto',minwidth=0,width=60)
    ShowItens_tv.column('estq',minwidth=0,width=60)
    ShowItens_tv.column('desc',minwidth=0,width=200)

    ShowItens_tv.heading('id',text="Cód. Prod ")
    ShowItens_tv.heading('ean',text="EAN/GTIN ")
    ShowItens_tv.heading('nome',text="Nome ")
    ShowItens_tv.heading('cat',text="Categ. ")
    ShowItens_tv.heading('precovenda',text="Pr. Venda ")
    ShowItens_tv.heading('precusto',text="Pr. Custo ")
    ShowItens_tv.heading('estq',text="Estoque ")
    ShowItens_tv.heading('desc',text="Descriçao ")
    ShowItens_tv.pack()

    # ------------Loop End----------------------------------
    window.mainloop()
