import tkinter as gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image


def MainPedidos():
      Pedidos_window = Toplevel()
      Pedidos_window.title("Lanchonete | Pedidos")
      Pedidos_window.resizable(False,False) 
      Pedidos_window.geometry("700x400") 
      Pedidos_window.iconbitmap("imagens/ico.lanchonete.ico")
      Pedidos_window.configure(bg="#DCDCDC")

      def inserir_lista():
            if CodProd_entry.get() == "":
                  messagebox.showinfo(title="ERRO",message="Digite o codigo do produto")
                  CodProd_entry.focus()
                  return
            if  DescProd_entry.get() == "":
                  messagebox.showinfo(title="ERRO",message="Digite a Descrição")
                  DescProd_entry.focus()
                  return   
            if  Un_entry.get() == "":
                  messagebox.showinfo(title="ERRO",message="Digitea Unidade")
                  Un_entry.focus()
                  return
            if  Qtd_label_entry.get() == "":
                  messagebox.showinfo(title="ERRO",message="Digite a Quantidade")
                  Qtd_label_entry.focus()
                  return  
            if  VlUnit_entry.get() == "":
                  messagebox.showinfo(title="ERRO",message="Digite o Valor Unitarios")
                  VlUnit_entry.focus()
                  return  
            if  VlTotal_entry.get() == "":
                  messagebox.showinfo(title="ERRO",message="Valor total não calculado")
                  VlTotal_entry.focus()
                  return  

            ShowItens_tv.insert("","end",values=(CodProd_entry.get(), DescProd_entry.get(), Un_entry.get(), Qtd_label_entry.get(),VlUnit_entry.get(),VlTotal_entry.get()))   
            CodProd_entry.delete(0,END)
            DescProd_entry.delete(0,END)
            Un_entry.delete(0,END)
            Qtd_label_entry.delete(0,END)
            VlUnit_entry.delete(0,END)
            VlTotal_entry.delete(0,END)
            CodProd_entry.focus()


      # Label(Pedidos_window,text="Pedidos").grid(row=0,column=0,sticky=W,pady=10)
      #codigo
      CodPedido_label = Label(Pedidos_window,text="Cód. Pedido:", font="Britannic 10 bold")
      CodPedido_label.grid(row=0,column=0,sticky=W)

      CodPedido_entry = Entry(Pedidos_window,width=30, bd=4)
      CodPedido_entry.grid(row=0,column=1,sticky=W)
      #operador
      CodOperador_label = Label(Pedidos_window,text="Operador:", font="Britannic 10 bold")
      CodOperador_label.grid(row=0,column=2,sticky=W)

      CodOperador_entry = Entry(Pedidos_window,width=30, bd=4)
      CodOperador_entry.grid(row=0,column=3,sticky=W)
      #produto
      CodProd_label = Label(Pedidos_window,text="Cód. Prod:", font="Britannic 10 bold")
      CodProd_label.grid(row=2,column=0,sticky=W)

      CodProd_entry = Entry(Pedidos_window,width=8, bd=4)
      CodProd_entry.place(x=89,y=25)

      DescProd_entry = Entry(Pedidos_window,width=19, bd=4)
      DescProd_entry.place(x=154,y=25)
      #UN
      Un_label = Label(Pedidos_window,text="UN:", font="Britannic 10 bold")
      Un_label.grid(row=2,column=2,sticky=W,padx=3)

      Un_entry = Entry(Pedidos_window,width=30, bd=4)
      Un_entry.grid(row=2,column=3,sticky=W)
      #quantidade
      Qtd_label = Label(Pedidos_window,text="Qtd.:", font="Britannic 10 bold")
      Qtd_label.grid(row=0,column=5,sticky=W)

      Qtd_label_entry = Entry(Pedidos_window,width=16, bd=4)
      Qtd_label_entry.grid(row=0,column=6,sticky=W)
      #valor
      VlUnit_label = Label(Pedidos_window,text="Valor Unit:", font="Britannic 10 bold")
      VlUnit_label.grid(row=3,column=0,sticky=W)

      VlUnit_entry = Entry(Pedidos_window,width=30, bd=4)
      VlUnit_entry.grid(row=3,column=1,sticky=W)
      #valor total
      VlTotal_label = Label(Pedidos_window,text="Valor Total:", font="Britannic 10 bold")
      VlTotal_label.grid(row=3,column=2,sticky=W)

      VlTotal_entry = Entry(Pedidos_window,width=30, bd=4)
      VlTotal_entry.grid(row=3,column=3,sticky=W)

      #botoes
      Item_add = Button(Pedidos_window,text="Adicionar",width=8,command=inserir_lista)
      Item_add.place(x=80,y=350)

      view_exist = Button(Pedidos_window,text="Imprimir")
      view_exist.place(x=20,y=350)


      #Treeview
      ShowItens_tv = ttk.Treeview(Pedidos_window,columns=('id','descricao','un','qtd','valorunit','valortotal'),show='headings')
      ShowItens_tv.column('id',minwidth=0,width=60)
      ShowItens_tv.column('descricao',minwidth=0,width=250)
      ShowItens_tv.column('un',minwidth=0,width=55)
      ShowItens_tv.column('qtd',minwidth=0,width=55)
      ShowItens_tv.column('valorunit',minwidth=0,width=55)
      ShowItens_tv.column('valortotal',minwidth=0,width=55)

      ShowItens_tv.heading('id',text="Cod. Pro")
      ShowItens_tv.heading('descricao',text="Descrição")
      ShowItens_tv.heading('un',text="Unid.")
      ShowItens_tv.heading('qtd',text="Qtde.")
      ShowItens_tv.heading('valorunit',text="Vr Unitário")
      ShowItens_tv.heading('valortotal',text="Vr Total")
      ShowItens_tv.place(x=90,y=100)


      Pedidos_window.mainloop()

