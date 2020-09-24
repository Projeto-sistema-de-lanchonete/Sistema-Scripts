import tkinter as gui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector # pip install mysql-connector
import pymysql # pip install pymysq



def TipoPagamentos():

      Tipo_Pagamento_window = Toplevel()
      Tipo_Pagamento_window.title("Lanchonete | Tipos de Pagamentos")
      Tipo_Pagamento_window.resizable(True,True) 
      #Tipo_Pagamento_window.geometry("750x500")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          /;//  ") 
      Tipo_Pagamento_window.iconbitmap("imagens/ico.lanchonete.ico")
      Tipo_Pagamento_window.configure(bg="#DCDCDC")

      def Ultimocodigo(): # Pega o maior valor da coluna cod_pedido para colocar na entry Cod           

            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()
            sqlid = "SELECT MAX(cod_pag) FROM tipo_pag"
            mycursor.execute(sqlid)
            for i in mycursor:
                  print(i)
            if  i[0] ==  None :
                  i = 0 
            ultimocod = i
            Cod_entry["state"] = "normal"
            Cod_entry.delete(0,END)
            Cod_entry.insert(0,ultimocod[0]+1)
            Cod_entry["state"] = "disabled"
      def SalvarTipoDePagamento():
        # salvando os dados do pedido
        connection = pymysql.connect(host="localhost",user="root",password="",database="bdlanchonete")
        mycursor = connection.cursor()
          
        sqlPag = "INSERT  INTO tipo_pag(cod_pag,desc_pag) VALUES('{}','{}')".format(Cod_entry.get(),Desc_entry.get())
        mycursor.execute(sqlPag)         

        mycursor.close()
        connection.commit()
        connection.close()
        Desc_entry.delete(0,END)
        Ultimocodigo()
        CarregarTree()



      def CarregarTree():
        ShowTipPag_tv.delete(*ShowTipPag_tv.get_children()) #limpa a lista
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
        mycursor = connection.cursor()

        sqlselect = "SELECT * FROM  tipo_pag"
        mycursor.execute(sqlselect) 

        for itens in mycursor:
              ShowTipPag_tv.insert("","end",values=(itens))
               


      Cod_label = Label(Tipo_Pagamento_window,text = "Codigo")
      Cod_label.grid(row=0, column=1)
    

      Cod_entry = Entry(Tipo_Pagamento_window,width = 8)
      Cod_entry.grid(row=0,column= 2)
      Ultimocodigo()
      
      Desc_label = Label(Tipo_Pagamento_window,text="Descrição")
      Desc_label.grid(row=0,column=3)

      Desc_entry = Entry(Tipo_Pagamento_window)
      Desc_entry.grid(row=0,column= 4)

      Btn_ADD = Button(Tipo_Pagamento_window,text="Adicionar",command=SalvarTipoDePagamento)
      Btn_ADD.grid(row=0,column=5)


       #Treeview
      ShowTipPag_tv = ttk.Treeview(Tipo_Pagamento_window,columns=('id','descricao'),show='headings')
      ShowTipPag_tv.column('id',minwidth=0,width=60)
      ShowTipPag_tv.column('descricao',minwidth=0,width=250)
      
      ShowTipPag_tv.heading('id',text="Cod. Tipo")
      ShowTipPag_tv.heading('descricao',text="Descrição")
      
      ShowTipPag_tv.grid(row=2,column=1,columnspan=4)
      CarregarTree()



      Tipo_Pagamento_window.mainloop()