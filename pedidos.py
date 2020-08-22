import tkinter as gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image



  
        
 
 
 
 

def deletar_lista():
      print()


def MainPedidos():
  Pedidos_window = Toplevel()
  Pedidos_window.title("Pedidos")
  Pedidos_window.resizable(False,False)  
  Pedidos_window.iconbitmap("logo.ico")

  def inserir_lista():
    if  CodProd_entry.get() == "":
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


  

  Label(Pedidos_window,text="Pedidos",font="Ariel").grid(row=0,column=0,sticky=W,pady=10)

  CodPedido_label = Label(Pedidos_window,text="Cod. Pedido :")
  CodPedido_label.grid(row=0,column=0,sticky=W)

  CodPedido_entry = Entry(Pedidos_window,width=10)
  CodPedido_entry.grid(row=0,column=1,sticky=W)

  CodOperador_label = Label(Pedidos_window,text="Operador :")
  CodOperador_label.grid(row=0,column=2,sticky=W,padx=60)

  CodOperador_entry = Entry(Pedidos_window,width=10)
  CodOperador_entry.grid(row=0,column=3)


  CodProd_label = Label(Pedidos_window,text="Cod. Prod :")
  CodProd_label.grid(row=1,column=0,sticky=W)

  CodProd_entry = Entry(Pedidos_window,width=10)
  CodProd_entry.grid(row=1,column=1,sticky=W)

  DescProd_entry = Entry(Pedidos_window,width=20)
  DescProd_entry.grid(row=1,column=2,sticky=W)


  Un_label = Label(Pedidos_window,text="UN :")
  Un_label.grid(row=1,column=3,sticky=W,padx=3)

  Un_entry = Entry(Pedidos_window,width=4)
  Un_entry.grid(row=1,column=4,padx=3)

  Qtd_label = Label(Pedidos_window,text="Qtd. :")
  Qtd_label.grid(row=1,column=5,sticky=W)

  Qtd_label_entry = Entry(Pedidos_window,width=6)
  Qtd_label_entry.grid(row=1,column=6,sticky=W)

  VlUnit_label = Label(Pedidos_window,text="Valor Unit :")
  VlUnit_label.grid(row=1,column=7,sticky=W)

  VlUnit_entry = Entry(Pedidos_window,width=6)
  VlUnit_entry.grid(row=1,column=8,sticky=W)

  VlTotal_label = Label(Pedidos_window,text="Valor Total :")
  VlTotal_label.grid(row=1,column=9,sticky=W)

  VlTotal_entry = Entry(Pedidos_window,width=8)
  VlTotal_entry.grid(row=1,column=10,sticky=W)


  Item_add = Button(Pedidos_window,text="Adicionar",font="Ariel,17",width=8,command=inserir_lista)
  Item_add.grid(row=1,column=11,rowspan=2,padx=20,sticky=W)


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
  ShowItens_tv.grid(row=3,column=0,columnspan=12,padx=5)


  







  view_exist = Button(Pedidos_window,text="Imprimir")
  view_exist.grid(row=4,column=13,rowspan=2,columnspan=4,padx=20,sticky=W+E)

  Pedidos_window.mainloop()
