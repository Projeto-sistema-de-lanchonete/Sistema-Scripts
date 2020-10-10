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



def MainVendas():

      Pedidos_window = Toplevel()
      Pedidos_window.title("Lanchonete | Vendas")
      Pedidos_window.resizable(False, False) 
      Pedidos_window.geometry("750x500")      
      Pedidos_window.iconbitmap("imagens/ico.lanchonete.ico")
      Pedidos_window.configure(bg="#DCDCDC")
          
      def Ultimocodigo(): # Pega o maior valor da coluna cod_pedido para colocar na entry Cod           

            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()
            sqlid = "SELECT MAX(cod_pedido) FROM vendas"
            mycursor.execute(sqlid)
            for i in mycursor:
                  print(i)
            if  i[0] ==  None :
                  i = 0 
            ultimocod = i
            CodPedido_entry["state"] = "normal"
            CodPedido_entry.delete(0,END)
            CodPedido_entry.insert(0,ultimocod[0]+1)
            CodPedido_entry["state"] = "disabled"
          
      def tecla(e): # Função para quando apertar enter no teclado fazer o calculo

            VlTotal_entry.delete(0,END) # Apagando o valor ja existente
            qtd = Qtd_label_entry.get() # pegando a quantidade
          
            vlUnit = VlUnit_entry.get() # pegando o valor unitario
            
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
                              VlUnit_entry.insert(0,produto[5])


                              qtd = Qtd_label_entry.get()               
                              vluni = VlUnit_entry.get()               
                              total = int(qtd) * float(vluni) # calculando o total

                              VlTotal_entry.insert(0,total) # Inserindo o total
                        
                  else:
                        messagebox.showwarning("Warning","Produto não localizado") # Mensagem caso não encontre produto.
      def InserirPagamento():
            def SomandoPagamentos(valorPedido): # Função soma todos os pagamento da lista
                  total = 0
                  float(total)
                        # Pegando todos os itens da tree
                  children =   ShowTipPag_tv.get_children()
                  #percorrendo tods os itens e pegado so o valor total do item
                  for i in children:
                        info = ShowTipPag_tv.item(i,"values")
                        item = info[1]
                        
                        total = float(valorPedido) - float(item)
                        valorPedido = total             
                        
                        
                  RestaValorPedido_entry.delete(0,END)
                  RestaValorPedido_entry.insert(0,moeda(1,total))
                   

            def InserirPagLista(): # Função inseri os pagamentos na lista
                  ShowTipPag_tv.insert("","end",values=(comboboxcat.get(), ValorPagamento_entry.get()))   
                  ValorPagamento_entry.delete(0,END)
                  comboboxcat.set("Selecione")
                  SomandoPagamentos(ValorPedido_entry.get())

                  resta = RestaValorPedido_entry.get()

                  if resta == "0.00" :
                        Btn_ADD["state"] = "disabled"
                        Btn_Ex["state"] = "normal"
            def ExcluirPagLista(): # Função Exclui os pagamentos na lista
                   try:
                        itemSelecionado =  ShowTipPag_tv.selection()[0] # pegando o item selecionado
                        ShowTipPag_tv.delete(itemSelecionado) # apagando o item
                        SomandoPagamentos(ValorPedido_entry.get()) # recalculando o valor totas do pedido
                        Btn_ADD["state"] = "normal"

                   except:
                        messagebox.showinfo(title="ERRO",message="Selecione um item") # mensagem caso não exista item selecionado
            def GravarPag(): # Função salva o pagamento no banco
                  children =   ShowTipPag_tv.get_children()
                  #percorrendo todos os pagamento 
                  for i in children:
                        info = ShowTipPag_tv.item(i,"values")
                        pag = info[0]
                        valor = info[1]
                        codigoPedido=CodPedido_entry.get()

                        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                        mycursor = connection.cursor()
                        sqlItens = "INSERT  INTO venda_pag(id_venda, desc_pag,valor_pag) VALUES('{}','{}','{}')".format(codigoPedido,pag,valor)
                        mycursor.execute(sqlItens)
                        mycursor.close()
                        connection.commit()
                        connection.close()
                  GerarArquivo(codigoPedido)      

            def FinalizarPag(): #Finaliza o Pedido e realiza o pagamento

                  # salvando os dados do pedido
                  connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor = connection.cursor()

                  CodPedido_entry["state"] = "normal"
                  sqlselect = "SELECT cod_pedido  FROM  vendas where  cod_pedido = '{}' ".format(CodPedido_entry.get())  # like (parecido com)
            
                  mycursor.execute(sqlselect)
                  valido = mycursor.fetchall()


                  if len(valido) > 0:
                  
                        print("tem pedido")
                        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                        mycursor= connection.cursor()
                        
                        CodPedido_entry["state"] = "normal"
                        sqldeleteItens = "DELETE FROM itens_venda where id_venda = {};".format(CodPedido_entry.get())
                        mycursor.execute(sqldeleteItens)
                        connection.commit()            

                        CodPedido_entry["state"] = "normal"
                        sqldeleteVenda = "DELETE  FROM vendas where cod_pedido = {};".format(CodPedido_entry.get())
                        mycursor.execute(sqldeleteVenda)
            
                        mycursor.close()
                        connection.commit()
                        connection.close()

                        # salvando os dados do pedido
                        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                        mycursor = connection.cursor()

                        CodPedido_entry["state"] = "normal"            
                        sqlVenda = "INSERT  INTO vendas(cod_pedido,cod_operador,id_clientes,vl_total,pedido_fechado) VALUES('{}','{}','{}','{}','{}')".format(CodPedido_entry.get(),CodOperador_entry.get(),1,total_pedido_entry.get(),"S")
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
                              sqlItens = "INSERT  INTO itens_venda(id_venda, cod_prod_venda, prod_des_venda,un_venda, qtd_venda, vl_init_venda, vl_total_venda) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(CodPedido_entry.get(),cod,desc,un,qtd,vlunit,total_item)
                              mycursor.execute(sqlItens)
                              mycursor.close()
                              connection.commit()
                              connection.close()
                        GravarPag()      
                        BaixaEstoque()
                        ImprimirArquivo(CodPedido_entry.get())


                        ShowItens_tv.delete(*ShowItens_tv.get_children()) #limpa a lista
                        total_pedido_entry.delete(0,END)
                        total_pedido_entry.insert(0,"0,00")
                        CodPedido_entry["state"] = "disabled"
                        Ultimocodigo()
                        Pagamento_window.destroy() # Fecha a janela
                  else:
                        
                        print("Não tem pedido")
                        # salvando os dados do pedido
                        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                        mycursor = connection.cursor()

                        CodPedido_entry["state"] = "normal"            
                        sqlVenda = "INSERT  INTO vendas(cod_pedido,cod_operador,id_clientes,vl_total,pedido_fechado) VALUES('{}','{}','{}','{}','{}')".format(CodPedido_entry.get(),CodOperador_entry.get(),1,total_pedido_entry.get(),"N")
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
                              sqlItens = "INSERT  INTO itens_venda(id_venda, cod_prod_venda, prod_des_venda,un_venda, qtd_venda, vl_init_venda, vl_total_venda) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(CodPedido_entry.get(),cod,desc,un,qtd,vlunit,total_item)
                              mycursor.execute(sqlItens)
                              mycursor.close()
                              connection.commit()
                              connection.close()
                        GravarPag()      
                        BaixaEstoque()
                        ImprimirArquivo(CodPedido_entry.get())


                        ShowItens_tv.delete(*ShowItens_tv.get_children()) #limpa a lista
                        total_pedido_entry.delete(0,END)
                        total_pedido_entry.insert(0,"0,00")
                        CodPedido_entry["state"] = "disabled"
                        Ultimocodigo()


                        Pagamento_window.destroy()# Fecha a janela

            Pagamento_window = Toplevel()
            Pagamento_window.title("Lanchonete | Pagamento")
            Pagamento_window.resizable(True,True) 
            #Pagamento_window.geometry("750x500")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          /;//  ") 
            Pagamento_window.iconbitmap("imagens/ico.lanchonete.ico")
            Pagamento_window.configure(bg="#DCDCDC")

            ValorPedido_label = Label(Pagamento_window,text = "Valor Pedido")
            ValorPedido_label.grid(row=0, column=1)
      

            ValorPedido_entry = Entry(Pagamento_window,width = 8)
            ValorPedido_entry.grid(row=0,column= 2)
            ValorPedido_entry.insert(0,total_pedido_entry.get())
            ValorPedido_entry["state"] = "disabled"

            labelcat = gui.Label(Pagamento_window,text="Pagamento:", bg="#C0C0C0", font="Britannic 10 bold")
            labelcat.grid(row=3,column=0,sticky=W)

            # Preencher ComboBo
            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()

            sqlselect = "SELECT desc_pag FROM  tipo_pag"
            mycursor.execute(sqlselect)

            tipo=[]
            for pagamento in mycursor:
                
                  tipo.append(pagamento)
                

            comboboxcat = ttk.Combobox(Pagamento_window, width=15, values=tipo, state="readonly") # adicionando um Combobox
            comboboxcat.set("Selecione") # o combobox inicia vazio se não for selecionado uma opção para ele iniciar | para fazer isso usa-se o .set
            comboboxcat.grid(row=3, column=1,padx=5,pady=3,ipady=3)

            ValorPagamento_label = Label(Pagamento_window,text = "Valor:")
            ValorPagamento_label.grid(row=3, column=2)
      

            ValorPagamento_entry = Entry(Pagamento_window,width = 8)
            ValorPagamento_entry.grid(row=3,column= 3)
           
           
            Btn_ADD = Button(Pagamento_window,text="Adicionar",command=InserirPagLista)
            Btn_ADD.grid(row=3,column=5)


            #Treeview
            ShowTipPag_tv = ttk.Treeview(Pagamento_window,columns=('pag','valor'),show='headings')
            ShowTipPag_tv.column('pag',minwidth=0,width=100)
            ShowTipPag_tv.column('valor',minwidth=0,width=150)
            
            ShowTipPag_tv.heading('pag',text="Pagamento")
            ShowTipPag_tv.heading('valor',text="Valor")            
            ShowTipPag_tv.grid(row=6,column=1,columnspan=6)

            Btn_Ex = Button(Pagamento_window,text="Excluir",command=ExcluirPagLista)
            Btn_Ex.grid(row=7,column=5)

            RestaValorPedido_label = Label(Pagamento_window,text = "Resta")
            RestaValorPedido_label.grid(row=8, column=1)

            RestaValorPedido_entry = Entry(Pagamento_window,width = 8)
            RestaValorPedido_entry.grid(row=8,column= 2)
            RestaValorPedido_entry.insert(0,total_pedido_entry.get())

            Btn_Ex = Button(Pagamento_window,text="Finalizar Pagamento",command=FinalizarPag)
            Btn_Ex.grid(row=8,column=3)
            Btn_Ex["state"] = "disabled"

            Pagamento_window.mainloop()
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
      
      def SalvarPedido(): # Função Para Salva  o pedido, colocando no campo pedido_fechado= "N"

            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()

            CodPedido_entry["state"] = "normal"
            sqlselect = "SELECT cod_pedido  FROM  vendas where  cod_pedido = '{}' ".format(CodPedido_entry.get())  # like (parecido com)
           
            mycursor.execute(sqlselect)
            valido = mycursor.fetchall()

            if len(valido) > 0:
                  print("tem pedido")
                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor= connection.cursor()
                  
                  CodPedido_entry["state"] = "normal"
                  sqldeleteItens = "DELETE FROM itens_venda where id_venda = {};".format(CodPedido_entry.get())
                  mycursor.execute(sqldeleteItens)
                  connection.commit()            

                  CodPedido_entry["state"] = "normal"
                  sqldeleteVenda = "DELETE  FROM vendas where cod_pedido = {};".format(CodPedido_entry.get())
                  mycursor.execute(sqldeleteVenda)
      
                  mycursor.close()
                  connection.commit()
                  connection.close()




                  # salvando os dados do pedido
                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor = connection.cursor()

                  CodPedido_entry["state"] = "normal"            
                  sqlVenda = "INSERT  INTO vendas(cod_pedido,cod_operador,id_clientes,vl_total,pedido_fechado) VALUES('{}','{}','{}','{}','{}')".format(CodPedido_entry.get(),CodOperador_entry.get(),"teste",total_pedido_entry.get(),"N")
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
                        sqlItens = "INSERT  INTO itens_venda(id_venda, cod_prod_venda, prod_des_venda,un_venda, qtd_venda, vl_init_venda, vl_total_venda) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(CodPedido_entry.get(),cod,desc,un,qtd,vlunit,total_item)
                        mycursor.execute(sqlItens)
                        mycursor.close()
                        connection.commit()
                        connection.close()


                  ShowItens_tv.delete(*ShowItens_tv.get_children()) #limpa a lista
                  total_pedido_entry.delete(0,END)
                  total_pedido_entry.insert(0,"0,00")
                  CodPedido_entry["state"] = "disabled"
                  Ultimocodigo()
            else:
                  print("Não tem pedido")
                  # salvando os dados do pedido
                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor = connection.cursor()

                  CodPedido_entry["state"] = "normal"            
                  sqlVenda = "INSERT  INTO vendas(cod_pedido,cod_operador,id_clientes,vl_total,pedido_fechado) VALUES('{}','{}','{}','{}','{}')".format(CodPedido_entry.get(),CodOperador_entry.get(),"teste",total_pedido_entry.get(),"N")
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
                        sqlItens = "INSERT  INTO itens_venda(id_venda, cod_prod_venda, prod_des_venda,un_venda, qtd_venda, vl_init_venda, vl_total_venda) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(CodPedido_entry.get(),cod,desc,un,qtd,vlunit,total_item)
                        mycursor.execute(sqlItens)
                        mycursor.close()
                        connection.commit()
                        connection.close()


                  ShowItens_tv.delete(*ShowItens_tv.get_children()) #limpa a lista
                  total_pedido_entry.delete(0,END)
                  total_pedido_entry.insert(0,"0,00")
                  CodPedido_entry["state"] = "disabled"
                  Ultimocodigo()
      def PesquisarPedido(): # Função para pesquisar pedido

            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()
           
            sqlselect = "SELECT cod_pedido, pedido_fechado  FROM  vendas where  cod_pedido = '{}' ".format(Cod_Pesquisa_entry.get())  # like (parecido com)
           
            mycursor.execute(sqlselect)
            valido = mycursor.fetchall()
            
            if len(valido) > 0: 
                  for venda in valido:                        
                                              
                        if venda[1] == "S":
                              messagebox.showinfo(title="ERRO",message="Pedido fechado não pode ser alterado")
                              Cod_Pesquisa_entry.delete(0,END)
                              Cod_Pesquisa_entry.focus()

                        else:
                              
                              connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
                              mycursor = connection.cursor()

                  
                              sqlselect = "SELECT *  FROM  vendas where  cod_pedido = '{}' ".format(Cod_Pesquisa_entry.get()) 
                              mycursor.execute(sqlselect) 

                              for pedido in mycursor:

                                    codigoPedido = pedido[0]
                                    operador = pedido[1]
                                    cliente = pedido[2]
                                    valorTotal = pedido[3]

                                    CodPedido_entry["state"] = "normal"
                                    CodPedido_entry.delete(0,END)
                                    CodPedido_entry.insert(0,codigoPedido)
                                    CodPedido_entry["state"] = "disabled"

                                    CodOperador_entry.delete(0,END)
                                    CodOperador_entry.insert(0,operador)

                                    total_pedido_entry.delete(0,END)
                                    total_pedido_entry.insert(0,valorTotal)


                              ShowItens_tv.delete(*ShowItens_tv.get_children()) #limpa a lista
                              connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
                              mycursor = connection.cursor()

                              sqlselect = "SELECT cod_prod_venda,prod_des_venda,un_venda,qtd_venda,vl_init_venda,vl_total_venda   FROM  itens_venda where  id_venda = '{}' ".format(Cod_Pesquisa_entry.get()) 
                              mycursor.execute(sqlselect) 

                              for itens in mycursor:
                                    ShowItens_tv.insert("","end",values=(itens))
                                    Cod_Pesquisa_entry.delete(0,END)
                                    


                                    
            else:
                   messagebox.showinfo(title="ERRO",message="Pedido  não encontrado")
                   Cod_Pesquisa_entry.delete(0,END)
                   Cod_Pesquisa_entry.focus()
               
      def BaixaEstoque(): # Função para da Baixa no estoque dos produtos vendidos

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
                        #print(estoqueAtual)
                        UpdateEstoque = int(estoqueAtual[0]) - int(qtd) # fazendo a operação para diminuir a quantidade vendida

                        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                        mycursor = connection.cursor()
                        # Baixando o estoque
                        sqlUpdateEstoque = "UPDATE produtos SET estoque = {} WHERE cod_produto = {}".format(UpdateEstoque,cod)
                        mycursor.execute(sqlUpdateEstoque)
                        mycursor.close()
                        connection.commit()
                        connection.close()
      def GerarArquivo(NumeroPedido): # Funçao para gerar o arquivo do pedido
            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()

            sqlBuscarEmpresa = "SELECT * FROM empresa"
            mycursor.execute(sqlBuscarEmpresa)

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
            hoje = date.today()

            with open("pedidos/Pedido"+str(NumeroPedido) +'.txt','w+') as pedido:

                  pedido.write("PEDIDO " + "Data: " + str(hoje.day)+"/"+str(hoje.month)+"/"+ str(hoje.year)+"\n")
                  pedido.write("----------------------------------------\n")
                  pedido.write(razao_social+"\n")
                  pedido.write(nome_fantasia+"\n")
                  pedido.write(end + ","+"Nº "+ num +"\n" + bairro + ","+ cep + " - " + cidade + "/" + uf +"\n")
                  pedido.write("----------------------------------------\n")

                  connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
                  mycursor = connection.cursor()

                  #buscando o pedido
                  sqlPedido = "SELECT * FROM VENDAS WHERE cod_pedido = {}".format(NumeroPedido)
                  mycursor.execute(sqlPedido)

                  for venda in mycursor:
                        cod_pedido = venda[0]
                        cod_operador = venda[1]
                        id_clientes = venda[2]
                        vl_total = venda[3]
                        data_create = venda[5]

                  #Buscando o Cliente do pedido      
                  sqlCliente = "SELECT * FROM clientes WHERE cod_cliente = {}".format(id_clientes)
                  mycursor.execute(sqlCliente)

                  # cod_cliente,nome_cliente,datanasc_cliente,cpf_cliente,rg_cliente,end_cliente,
                  # nunend_cliente,bairro_cliente,cep_cliente,cidade_cliente,uf_cliente,fone_cliente,celular_cliente,email_cliente      
                  for Cliente in mycursor:
                        print(Cliente)
                  pedido.write("Dados do Cliente: \n")                        
                  pedido.write("Cod.: " + str(Cliente[0]) + " Nome: " + str(Cliente[1] + "\n"))
                  pedido.write("CPF: " + str(Cliente[3]) +"\n")
                  pedido.write("End.: " + str(Cliente[5])+","+ str(Cliente[6])+"\n")
                  pedido.write("Bairro: " + str(Cliente[7]) + " CEP: " + str(Cliente[8]) + " - "+ str(Cliente[9]) + "/" + str(Cliente[10]) + "\n")
                  pedido.write("Contato: " + str(Cliente[12]) + "\n")
                  pedido.write("Pedido: " + str(cod_pedido) + "\n")
                  pedido.write("---------------------------------------- \n")


                  sqlItens = "SELECT * FROM itens_venda WHERE id_venda = {}".format(NumeroPedido)
                  mycursor.execute(sqlItens)
                  # id_venda,cod_prod_venda,prod_des_venda,un_venda,qtd_venda,vl_init_venda,vl_total_venda

                  pedido.write("ITEM CODIGO  DESCRIÇÃO  QTD  UN VLUN  VLT  \n")
                  contador = 1
                  totalItens = 0
                  for itens in mycursor:
                        pedido.write(str(contador) + " " + str(itens[1]) + " " + str(itens[2]) + " " + str(itens[4]) + " " + str(itens[3]) + " " + str(itens[5]) + " " + str(itens[6]) + "\n")
                        contador = contador + 1
                        totalItens = totalItens + itens[6]


                  pedido.write("---------------------------------------- \n")

                  pedido.write("PAGAMENTO\n")
                  
                  sqlPagamento = "SELECT * FROM venda_pag WHERE id_venda = {}".format(NumeroPedido)
                  mycursor.execute(sqlPagamento)

                  # id_venda,desc_pag,valor_pag
                  pedido.write("SubTotal ................R$ " + str(totalItens) +"\n")
                  for pagamento in mycursor:
                        pedido.write(str(pagamento[1]) +"................R$ " + str(pagamento[2]) + "\n" )
                  pedido.write("Total................R$ " + str(vl_total))
                
                  

      def ImprimirArquivo(numeroPedido,event=None): #Função para Imprimir o Pedido
            try:
                 
                  # Definindo o caminho do arquivo para impressão
                  arquivo = "C:/Users/Itamar/Documents/GitHub/Sistema-Scripts/pedidos/Pedido"+ str(numeroPedido) +'.txt'
                  _printer = StringVar(Pedidos_window)
                  # Setando a impressora padrão do windows
                  _printer.set(win32print.GetDefaultPrinter())
                  #print(_printer)
      
                  PRINTER_DEFAULTS = {"DesiredAccess":win32print.PRINTER_ALL_ACCESS} 
                  pHandle = win32print.OpenPrinter(_printer.get(), PRINTER_DEFAULTS)
                  properties = win32print.GetPrinter(pHandle, 2)            
                  win32print.SetPrinter(pHandle, 2, properties, 0)

                  try:
                        #win32print.SetDefaultPrinter(_printer.get())
                        win32api.ShellExecute(0, "print", arquivo, None,  ".",  0)
                        win32print.ClosePrinter(pHandle)
                  except:
                        pass
                        messagebox.showerror("Error", "Não foi passivel imprimir o pedido.")
            except:
                  pass
                  messagebox.showerror("Error", "Não foi passivel imprimir o pedido.")

     
      # Label(Pedidos_window,text="Pedidos").grid(row=0,column=0,sticky=W,pady=10)
      #codigo
      CodPedido_label = Label(Pedidos_window,text="Cód. Pedido:",bg="#C0C0C0", font="Britannic 10 bold")
      CodPedido_label.grid(row=0,column=0,sticky=W)

      CodPedido_entry = Entry(Pedidos_window,width=8, bd=4)
      CodPedido_entry.grid(row=0,column=1,sticky=W)
      Ultimocodigo()
      
      #operador
      CodOperador_label = Label(Pedidos_window,text="Operador:",bg="#C0C0C0", font="Britannic 10 bold")
      CodOperador_label.grid(row=0,column=2,sticky=W)
      
      CodOperador_entry = Entry(Pedidos_window,width=15, bd=4)
      CodOperador_entry.grid(row=0,column=3,sticky=W)

      #Pesquisar Pedido
      Cod_Pesquisa_label = Label(Pedidos_window,text="Pesquisar pedido:",bg="#C0C0C0", font="Britannic 10 bold")
      Cod_Pesquisa_label.grid(row=0,column=4,sticky=W)
      
      Cod_Pesquisa_entry = Entry(Pedidos_window,width=8, bd=4)
      Cod_Pesquisa_entry.grid(row=0,column=5,sticky=W)


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
      Un_entry.insert(0,"UN")
      #quantidade
      Qtd_label = Label(Pedidos_window,text="Qtd.:",width=7, bg="#C0C0C0",font="Britannic 10 bold")
      Qtd_label.place(x=410,y=25)
      

      Qtd_label_entry = Entry(Pedidos_window,width=16, bd=4)
      Qtd_label_entry.place(x=480,y=25)
      Qtd_label_entry.insert(0,1)
      Qtd_label_entry.bind("<Key>", tecla)
      #valor
      VlUnit_label = Label(Pedidos_window,text="Valor Unit:",bg="#C0C0C0", font="Britannic 10 bold")
      VlUnit_label.grid(row=3,column=0,sticky=W)

      VlUnit_entry = Entry(Pedidos_window,width=10, bd=4)
      VlUnit_entry.grid(row=3,column=1,sticky=W)
      VlUnit_entry.bind("<Key>", tecla)
      #valor total
      VlTotal_label = Label(Pedidos_window,text="Total:",bg="#C0C0C0", font="Britannic 10 bold")
      VlTotal_label.place(x=160,y=50)

      VlTotal_entry = Entry(Pedidos_window,width=12, bd=4)
      VlTotal_entry.place(x=200,y=50)

      #botoes

      PesquisarPedido= Button(Pedidos_window,text="Pesquisar", bg="#C0C0C0", width= 5, padx=20, pady=2,command=PesquisarPedido)
      PesquisarPedido.grid(row=0,column=6,sticky=W)

      view_exist = Button(Pedidos_window,text="Salva Pedido", bg="#C0C0C0", width= 10, padx=20, pady=2, borderwidth=5,command=SalvarPedido)
      view_exist.place(x=20,y=350)

      Item_add = Button(Pedidos_window,text="Adicionar", bg="#C0C0C0", width= 5, height=1, padx=20, pady=2, command=inserir_lista)
      Item_add.place(x=300,y=50)

      Item_ex = Button(Pedidos_window,text="Excluir", bg="#C0C0C0", width= 5, padx=20, pady=2,  command=excluir_item_lista)
      Item_ex.place(x=390,y=50)

      Item_ex = Button(Pedidos_window,text="Fechar Pedido", bg="#C0C0C0", width= 10, padx=20, pady=2, borderwidth=5, command=InserirPagamento)
      Item_ex.place(x=150,y=350)


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

