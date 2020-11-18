import win32api
import win32print
import traceback
import tkinter as gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector # pip install mysql-connector
import pymysql # pip install pymysq
from datetime import date



    
      
def MainMEntradaDeNotas():
      
      Pedidos_window = Toplevel()
      Pedidos_window.title("Lanchonete | Entrada de Notas")
      Pedidos_window.resizable(False, False) 
      Pedidos_window.geometry("950x500")      
      Pedidos_window.iconbitmap("imagens/ico.lanchonete.ico")
      Pedidos_window.configure(bg="#DCDCDC")
        
      def Ultimocodigo(): # Pega o maior valor da coluna cod_pedido para colocar na entry Cod           

            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()
            sqlid = "SELECT MAX(cod_entrada) FROM entradanotas"
            mycursor.execute(sqlid)
            for i in mycursor:
                  print(i)
            if  i[0] ==  None :
                  i = 0 
            ultimocod = i
            CodEntrada_entry["state"] = "normal"
            CodEntrada_entry.delete(0,END)
            CodEntrada_entry.insert(0,ultimocod[0]+1)
            CodEntrada_entry["state"] = "disabled"
          
      def tecla(e): # Função para quando apertar enter no teclado fazer o calculo
            
            VlTotal_entry.delete(0,END) # Apagando o valor ja existente
            qtd = Qtd_label_entry.get() # pegando a quantidade
          
            vlUnit = VlUnit_entry.get() # pegando o valor unitario
            
            if qtd == "" or vlUnit == "":
                  messagebox.showwarning("Atenção","Digite os valores")
                  
                  Qtd_label_entry.focus()
                  qtd = 1

            total = int(qtd) * float(vlUnit) # multiplicando a quantidade com o valor unitário
            VlTotal_entry.insert(0,total) # inserindo no campo
      def excluir_item_lista(): # função para excluir item selecionado
            try:
                  itemSelecionado =  ShowItens_tv.selection()[0] # pegando o item selecionado
                  ShowItens_tv.delete(itemSelecionado) # apagando o item
                  SomandoItens() # recalculando o valor totas do pedido
            except:
                  messagebox.showinfo(title="ERRO",message="Selecione um item") # mensagem caso não exista item selecionado
      def moeda (qtd = 0, vlunit = 0 , moeda ='R$'): # Função para converte em moeda
            int(qtd)
            total = int(qtd) * float(vlunit)
            return f'{total:.2f}'#.replace('.',',') 
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
            Qtd_label_entry.insert(0,1)
            CodProd_entry.focus()
            SomandoItens()
      def pesquisarProdutos(): # Função para pesquisar o produto.
              if CodProd_entry.get() == "":
                  messagebox.showwarning("Warning","Informe um codigo para pesquisar") # Mensagem caso não encontre produto.
                  CodProd_entry.focus()
              else:

                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor = connection.cursor()

            

                  sqlPesquisar = "SELECT * FROM produtos where cod_produto= {}".format(CodProd_entry.get())
                  mycursor.execute(sqlPesquisar)
                  valido = mycursor.fetchall()


                  if len(valido) > 0:


                        for produto in valido:     # percorrendo o produto  
                              #print(produto)

                              # Apagando os campos 
                              DescProd_entry.delete(0,END)
                              VlUnit_entry.delete(0,END)
                              VlTotal_entry.delete(0,END)

                                    # Colocando os valos
                              DescProd_entry.insert(0,produto[2])
                              Un_entry.insert(0,produto[4])              
                              VlUnit_entry.insert(0,produto[6])


                              qtd = Qtd_label_entry.get()               
                              vluni = VlUnit_entry.get()               
                              total = int(qtd) * float(vluni) # calculando o total

                              VlTotal_entry.insert(0,total) # Inserindo o total
                        
                  else:
                        messagebox.showwarning("Warning","Produto não localizado") # Mensagem caso não encontre produto.
      
      def SomandoItens(): # Função soma todos os itens da lista
           total = 0
           float(total)
            # Pegando todos os itens da tree
           children =   ShowItens_tv.get_children()
          #percorrendo tods os itens e pegado so o valor total do item
           for i in children:
                 info = ShowItens_tv.item(i,"values")
                 item = info[5]
                 
                 total = float(total) + float(item)             
                 
            
           total_pedido_entry.delete(0,END)
           total_pedido_entry.insert(0,moeda(1,total))     
      
      def SalvarNota(): # Função Para Salva  o pedido, colocando no campo pedido_fechado= "N"

            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()

            CodEntrada_entry["state"] = "normal"
            sqlselect = "SELECT cod_entrada  FROM  entradanotas where  cod_entrada = '{}' ".format(CodEntrada_entry.get())  # like (parecido com)
           
            mycursor.execute(sqlselect)
            valido = mycursor.fetchall()

            if len(valido) > 0:
                  print("tem Entrada")
                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor= connection.cursor()
                  
                  CodEntrada_entry["state"] = "normal"
                  sqldeleteItens = "DELETE FROM itens_entrada where id_entrada = {};".format(CodEntrada_entry.get())
                  mycursor.execute(sqldeleteItens)
                  connection.commit()            

                  CodEntrada_entry["state"] = "normal"
                  sqldeleteVenda = "DELETE  FROM entradanotas where cod_entrada = {};".format(CodEntrada_entry.get())
                  mycursor.execute(sqldeleteVenda)
      
                  mycursor.close()
                  connection.commit()
                  connection.close()




                  # salvando os dados do pedido
                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor = connection.cursor()

                  CodEntrada_entry["state"] = "normal" 
                  CodOperador_entry["state"] = "normal"                              
                  sqlVenda = "INSERT  INTO entradanotas(cod_entrada,nome_operador,id_fornecedor,vl_total,nota_fechado) VALUES('{}','{}','{}','{}','{}')".format(CodEntrada_entry.get(),CodOperador_entry.get(),CodFornecedor_entry.get(),total_pedido_entry.get(),"N")
                  mycursor.execute(sqlVenda)         

                  mycursor.close()
                  connection.commit()
                  connection.close()
                  
                  children =   ShowItens_tv.get_children()
                  #percorrendo tods os itens e pegado so o valor total do item
                  for i in children:
                        info = ShowItens_tv.item(i,"values")
                        cod = info[0]
                        desc = info[1]
                        un = info[2]
                        qtd = info[3]
                        vlunit = info[4]
                        total_item = info[5]

                        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                        mycursor = connection.cursor()
                        sqlItens = "INSERT  INTO itens_entrada(id_entrada, cod_prod_entrada, prod_des_entrada,un_entrada, qtd_entrada, vl_init_entrada, vl_total_entrada) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(CodEntrada_entry.get(),cod,desc,un,qtd,vlunit,total_item)
                        mycursor.execute(sqlItens)
                        mycursor.close()
                        connection.commit()
                        connection.close()


                  ShowItens_tv.delete(*ShowItens_tv.get_children()) #limpa a lista
                  total_pedido_entry.delete(0,END)
                  total_pedido_entry.insert(0,"0,00")
                  CodEntrada_entry["state"] = "disabled"
                  CodOperador_entry["state"] = "disabled" 
                  Ultimocodigo()
            else:
                  print("Não tem pedido")
                  # salvando os dados do pedido
                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor = connection.cursor()

                  CodEntrada_entry["state"] = "normal"
                  CodOperador_entry["state"] = "normal" 
                  CodFornecedor = Cod_Pesquisa_entry.get()           
                  sqlEntrada = "INSERT  INTO entradanotas(cod_entrada,nome_operador,id_fornecedor,vl_total,nota_fechado) VALUES('{}','{}','{}','{}','{}')".format(CodEntrada_entry.get(),CodOperador_entry.get(),CodFornecedor,total_pedido_entry.get(),"N")
                  mycursor.execute(sqlEntrada)         

                  mycursor.close()
                  connection.commit()
                  connection.close()
                  
                  children =   ShowItens_tv.get_children()
                  #percorrendo tods os itens e pegado so o valor total do item
                  for i in children:
                        info = ShowItens_tv.item(i,"values")
                        cod = info[0]
                        desc = info[1]
                        un = info[2]
                        qtd = info[3]
                        vlunit = info[4]
                        total_item = info[5]

                        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                        mycursor = connection.cursor()
                        sqlItens = "INSERT  INTO itens_entrada(id_entrada, cod_prod_entrada, prod_des_entrada,un_entrada, qtd_entrada, vl_init_entrada, vl_total_entrada) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(CodEntrada_entry.get(),cod,desc,un,qtd,vlunit,total_item)
                        mycursor.execute(sqlItens)
                        mycursor.close()
                        connection.commit()
                        connection.close()


                  ShowItens_tv.delete(*ShowItens_tv.get_children()) #limpa a lista
                  total_pedido_entry.delete(0,END)
                  total_pedido_entry.insert(0,"0,00")
                  CodEntrada_entry["state"] = "disabled"
                  CodOperador_entry["state"] = "disabled"
                  Ultimocodigo()
      def PesquisarNota(): # Função para pesquisar pedido

            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()
           
            sqlselect = "SELECT cod_entrada, nota_fechado  FROM  entradanotas where  cod_entrada = '{}' ".format(Cod_Pesquisa_entry.get())  # like (parecido com)
           
            mycursor.execute(sqlselect)
            valido = mycursor.fetchall()
            
            if len(valido) > 0: 
                  for venda in valido:                        
                                              
                        if venda[1] == "S":
                              messagebox.showinfo(title="ERRO",message="Nota fechada não pode ser alterada")
                              Cod_Pesquisa_entry.delete(0,END)
                              Cod_Pesquisa_entry.focus()

                        else:
                              
                              connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
                              mycursor = connection.cursor()

                  
                              sqlselect = "SELECT *  FROM  entradanotas where  cod_entrada = '{}' ".format(Cod_Pesquisa_entry.get()) 
                              mycursor.execute(sqlselect) 

                              for pedido in mycursor:

                                    codigoPedido = pedido[0]
                                    operador = pedido[1]
                                    fornecedor = pedido[2]
                                    valorTotal = pedido[3]

                                    CodEntrada_entry["state"] = "normal"
                                    CodEntrada_entry.delete(0,END)
                                    CodEntrada_entry.insert(0,codigoPedido)
                                    CodEntrada_entry["state"] = "disabled"

                                    CodOperador_entry.delete(0,END)
                                    CodOperador_entry.insert(0,operador)

                                    CodFornecedor_entry.delete(0,END)
                                    CodFornecedor_entry.insert(0,fornecedor)

                                    NomeFornecedor_entry.insert(0,BuscarFornecedor())

                                    total_pedido_entry.delete(0,END)
                                    total_pedido_entry.insert(0,valorTotal)


                              ShowItens_tv.delete(*ShowItens_tv.get_children()) #limpa a lista
                              connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
                              mycursor = connection.cursor()

                              sqlselect = "SELECT cod_prod_entrada,prod_des_entrada,un_entrada,qtd_entrada,vl_init_entrada,vl_total_entrada   FROM  itens_entrada where  id_entrada = '{}' ".format(Cod_Pesquisa_entry.get()) 
                              mycursor.execute(sqlselect) 

                              for itens in mycursor:
                                    ShowItens_tv.insert("","end",values=(itens))
                                    Cod_Pesquisa_entry.delete(0,END)
                                    


                                    
            else:
                   messagebox.showinfo(title="ERRO",message="Nota não encontrada")
                   Cod_Pesquisa_entry.delete(0,END)
                   Cod_Pesquisa_entry.focus()


      def BuscarFornecedor():

          connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
          mycursor = connection.cursor()

          sqlBuscarFornecedor = "SELECT * FROM fornecedor WHERE cod_fornecedor = {}".format(CodFornecedor_entry.get())
          mycursor.execute(sqlBuscarFornecedor)

          for data in mycursor:
              cod = data[0]
              razao_social = data[1]

          NomeFornecedor_entry["state"] = "normal"
          NomeFornecedor_entry.delete(0,END)
          NomeFornecedor_entry.insert(0,razao_social)
          NomeFornecedor_entry["state"] = "disabled"

          return razao_social

      def EntradaEstoque(): # Função para da Baixa no estoque dos produtos vendidos

          children =   ShowItens_tv.get_children()
          #percorrendo tods os itens e pegado so a quantidade e o codigo do item
          for i in children:  

              info = ShowItens_tv.item(i,"values")
              cod = info[0]
              qtd = info[3]

              connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
              mycursor = connection.cursor()

              # Buscando a quantidade do estoque do produto.
              sqlEstoqueAtual = "SELECT estoque FROM produtos WHERE cod_produto = {}".format(cod)
              mycursor.execute(sqlEstoqueAtual)

              for estoqueAtual in mycursor:

                  print(estoqueAtual)
                  UpdateEstoque = int(estoqueAtual[0]) + int(qtd) # fazendo a operação para diminuir a quantidade vendida

                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor = connection.cursor()
                  # Baixando o estoque
                  sqlUpdateEstoque = "UPDATE produtos SET estoque = {} WHERE cod_produto = {}".format(UpdateEstoque,cod)
                  mycursor.execute(sqlUpdateEstoque)
                  mycursor.close()
                  connection.commit()
                  connection.close()      
      def FecharNota(): # Função Para fecjar  a nota, colocando no campo nota_fechado= "S"

            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()

            CodEntrada_entry["state"] = "normal"
            sqlselect = "SELECT cod_entrada  FROM  entradanotas where  cod_entrada = '{}' ".format(CodEntrada_entry.get())  # like (parecido com)
           
            mycursor.execute(sqlselect)
            valido = mycursor.fetchall()

            if len(valido) > 0:
                  print("tem Entrada")
                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor= connection.cursor()
                  
                  CodEntrada_entry["state"] = "normal"
                  sqldeleteItens = "DELETE FROM itens_entrada where id_entrada = {};".format(CodEntrada_entry.get())
                  mycursor.execute(sqldeleteItens)
                  connection.commit()            

                  CodEntrada_entry["state"] = "normal"
                  sqldeleteVenda = "DELETE  FROM entradanotas where cod_entrada = {};".format(CodEntrada_entry.get())
                  mycursor.execute(sqldeleteVenda)
      
                  mycursor.close()
                  connection.commit()
                  connection.close()




                  # salvando os dados do pedido
                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor = connection.cursor()

                  CodEntrada_entry["state"] = "normal" 
                  CodOperador_entry["state"] = "normal"                              
                  sqlVenda = "INSERT  INTO entradanotas(cod_entrada,nome_operador,id_fornecedor,vl_total,nota_fechado) VALUES('{}','{}','{}','{}','{}')".format(CodEntrada_entry.get(),CodOperador_entry.get(),CodFornecedor_entry.get(),total_pedido_entry.get(),"S")
                  mycursor.execute(sqlVenda)         

                  mycursor.close()
                  connection.commit()
                  connection.close()
                  
                  children =   ShowItens_tv.get_children()
                  #percorrendo tods os itens e pegado so o valor total do item
                  for i in children:
                        info = ShowItens_tv.item(i,"values")
                        cod = info[0]
                        desc = info[1]
                        un = info[2]
                        qtd = info[3]
                        vlunit = info[4]
                        total_item = info[5]

                        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                        mycursor = connection.cursor()
                        sqlItens = "INSERT  INTO itens_entrada(id_entrada, cod_prod_entrada, prod_des_entrada,un_entrada, qtd_entrada, vl_init_entrada, vl_total_entrada) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(CodEntrada_entry.get(),cod,desc,un,qtd,vlunit,total_item)
                        mycursor.execute(sqlItens)
                        mycursor.close()
                        connection.commit()
                        connection.close()
                  EntradaEstoque() 


                  ShowItens_tv.delete(*ShowItens_tv.get_children()) #limpa a lista
                  total_pedido_entry.delete(0,END)
                  total_pedido_entry.insert(0,"0,00")
                  CodEntrada_entry["state"] = "disabled"
                  CodOperador_entry["state"] = "disabled"
                  Ultimocodigo()
                  
            else:
                  print("Não tem pedido")
                  # salvando os dados do pedido
                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor = connection.cursor()

                  CodEntrada_entry["state"] = "normal"
                  CodOperador_entry["state"] = "normal" 
                  CodFornecedor = CodFornecedor_entry.get()           
                  sqlEntrada = "INSERT  INTO entradanotas(cod_entrada,nome_operador,id_fornecedor,vl_total,nota_fechado) VALUES('{}','{}','{}','{}','{}')".format(CodEntrada_entry.get(),CodOperador_entry.get(),CodFornecedor,total_pedido_entry.get(),"S")
                  mycursor.execute(sqlEntrada)         

                  mycursor.close()
                  connection.commit()
                  connection.close()
                  
                  children =   ShowItens_tv.get_children()
                  #percorrendo tods os itens e pegado so o valor total do item
                  for i in children:
                        info = ShowItens_tv.item(i,"values")
                        cod = info[0]
                        desc = info[1]
                        un = info[2]
                        qtd = info[3]
                        vlunit = info[4]
                        total_item = info[5]

                        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                        mycursor = connection.cursor()
                        sqlItens = "INSERT  INTO itens_entrada(id_entrada, cod_prod_entrada, prod_des_entrada,un_entrada, qtd_entrada, vl_init_entrada, vl_total_entrada) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(CodEntrada_entry.get(),cod,desc,un,qtd,vlunit,total_item)
                        mycursor.execute(sqlItens)
                        mycursor.close()
                        connection.commit()
                        connection.close()
                  EntradaEstoque()


                  ShowItens_tv.delete(*ShowItens_tv.get_children()) #limpa a lista
                  total_pedido_entry.delete(0,END)
                  total_pedido_entry.insert(0,"0,00")
                  CodEntrada_entry["state"] = "disabled"
                  CodOperador_entry["state"] = "disabled"
                  Ultimocodigo()  
                  
        
      
      # Label(Pedidos_window,text="Pedidos").grid(row=0,column=0,sticky=W,pady=10)
      #codigo
      CodEntrada_label = Label(Pedidos_window,text="Cód. Entrada:",bg="#C0C0C0", font="Britannic 10 bold")
      CodEntrada_label.grid(row=0,column=0,sticky=W)

      CodEntrada_entry = Entry(Pedidos_window,width=8, bd=4)
      CodEntrada_entry.grid(row=0,column=1,sticky=W)
      Ultimocodigo()
      
      #operador
      CodOperador_label = Label(Pedidos_window,text="Operador:",bg="#C0C0C0", font="Britannic 10 bold")
      CodOperador_label.grid(row=0,column=2,sticky=W)

       
      
      
      connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
      mycursor = connection.cursor()

      sqlselectUsuario = "select * from log_usuario "  # like (parecido com)            
      mycursor.execute(sqlselectUsuario)

      for user in mycursor:
            usuario = user[0]

      CodOperador_entry = Entry(Pedidos_window,width=15, bd=4)
      CodOperador_entry.grid(row=0,column=3,sticky=W)

      CodOperador_entry.insert(0,usuario)
      CodOperador_entry["state"] = "disabled"

       #Fornecedor
      CodFornecedor_label = Label(Pedidos_window,text="Fornecedor:",bg="#C0C0C0", font="Britannic 10 bold")
      CodFornecedor_label.grid(row=0,column=12,sticky=W)

      CodFornecedor_entry = Entry(Pedidos_window,width=15, bd=4)
      CodFornecedor_entry.grid(row=0,column=13,sticky=W)



      #Pesquisar Pedido
      Cod_Pesquisa_label = Label(Pedidos_window,text="Pesquisar Entrada:",bg="#C0C0C0", font="Britannic 10 bold")
      Cod_Pesquisa_label.grid(row=0,column=4,sticky=W)
      
      Cod_Pesquisa_entry = Entry(Pedidos_window,width=8, bd=4)
      Cod_Pesquisa_entry.grid(row=0,column=8,sticky=W)
      
      # Colocando Imagem no botao
      width = 20
      height = 20
      img = Image.open("imagens/ico.pesquisar.png")
      img = img.resize((width,height), Image.ANTIALIAS)
      photoImg2 =  ImageTk.PhotoImage(img)

      # imgpesq = PhotoImage(file="Imagens/ico.pesquisar.png")
      # imgpesq.configure(width=5,height=5)
      btPesquisar = Button(Pedidos_window,text="Pesquisar",image=photoImg2, bg="#DCDCDC",command=BuscarFornecedor)
      btPesquisar.place(x=790,y=0)

      NomeFornecedor_entry = Entry(Pedidos_window,width=15, bd=4)
      NomeFornecedor_entry.place(x=820,y=0)
      NomeFornecedor_entry["state"] = "disabled"



      #produto
      CodProd_label = Label(Pedidos_window,text="Cód. Prod:",bg="#C0C0C0", font="Britannic 10 bold")
      CodProd_label.grid(row=2,column=0,sticky=W)

      CodProd_entry = Entry(Pedidos_window,width=8, bd=4)
      CodProd_entry.place(x=89,y=25)
      
      # Colocando Imagem no botao
      width = 20
      height = 20
      img = Image.open("imagens/ico.pesquisar.png")
      img = img.resize((width,height), Image.ANTIALIAS)
      photoImg =  ImageTk.PhotoImage(img)

      # imgpesq = PhotoImage(file="Imagens/ico.pesquisar.png")
      # imgpesq.configure(width=5,height=5)
      btvendas = Button(Pedidos_window,text="Pesquisar",image=photoImg, bg="#DCDCDC",command=pesquisarProdutos)
      btvendas.place(x=150,y=25)

      DescProd_entry = Entry(Pedidos_window,width=19, bd=4)
      DescProd_entry.place(x=195,y=25)
      #UN
      Un_label = Label(Pedidos_window,text="UN:", bg="#C0C0C0",font="Britannic 10 bold")
      Un_label.place(x=325,y=25)

      Un_entry = Entry(Pedidos_window,width=7, bd=4)
      Un_entry.place(x=350,y=25)
      
      #quantidade
      Qtd_label = Label(Pedidos_window,text="Qtd.:",width=7, bg="#C0C0C0",font="Britannic 10 bold")
      Qtd_label.place(x=410,y=25)
      

      Qtd_label_entry = Entry(Pedidos_window,width=16, bd=4)
      Qtd_label_entry.place(x=480,y=25)
      Qtd_label_entry.insert(0,1)
      Qtd_label_entry.bind("<Return>", tecla)
      #valor
      VlUnit_label = Label(Pedidos_window,text="Valor Unit:",bg="#C0C0C0", font="Britannic 10 bold")
      VlUnit_label.grid(row=3,column=0,sticky=W)

      VlUnit_entry = Entry(Pedidos_window,width=10, bd=4)
      VlUnit_entry.grid(row=3,column=1,sticky=W)
      VlUnit_entry.bind("<Return>", tecla)
      #valor total
      VlTotal_label = Label(Pedidos_window,text="Total:",bg="#C0C0C0", font="Britannic 10 bold")
      VlTotal_label.place(x=160,y=50)

      VlTotal_entry = Entry(Pedidos_window,width=12, bd=4)
      VlTotal_entry.place(x=200,y=50)

      #botoes

      PesquisarPedido= Button(Pedidos_window,text="Pesquisar", bg="#C0C0C0", width= 5, padx=20, pady=2,command=PesquisarNota)
      PesquisarPedido.grid(row=0,column=11,sticky=W)

      view_exist = Button(Pedidos_window,text="Salva Nota", bg="#C0C0C0", width= 10, padx=20, pady=2, borderwidth=5,command=SalvarNota)
      view_exist.place(x=20,y=350)

      BtnFecharEntrada = Button(Pedidos_window,text="Fechar Nota", bg="#C0C0C0", width= 10, padx=20, pady=2, borderwidth=5,command=FecharNota)
      BtnFecharEntrada.place(x=150,y=350)

      Item_add = Button(Pedidos_window,text="Adicionar", bg="#C0C0C0", width= 5, height=1, padx=20, pady=2, command=inserir_lista)
      Item_add.place(x=300,y=50)

      Item_ex = Button(Pedidos_window,text="Excluir", bg="#C0C0C0", width= 5, padx=20, pady=2,  command=excluir_item_lista)
      Item_ex.place(x=390,y=50)



      Total_label = Label(Pedidos_window,text="Valor Total:",bg="#C0C0C0", font="Britannic 10 bold")
      Total_label.place(x=460,y=350)

      total_pedido_entry = Entry(Pedidos_window,width=9, bd=4)
      total_pedido_entry.place(x=540,y=350)
      total_pedido_entry.insert(0,"0,00")




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

