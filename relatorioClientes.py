from tkinter import *
import tkinter as gui
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import pymysql # pip install pymysq
import mysql.connector # pip install mysql-connector

import os

def mp(mm):
  return mm/0.352777

pastaSalva = os.path.dirname(__file__)
def criarRelatoriosCliente():
  try:
    cnv = canvas.Canvas(pastaSalva+"\\Relatorios\Clientes\Relatorio1.pdf",pagesize=A4) #Criando o arquivo

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

    # Cabeçalho

    cnv.rect(mp(10),mp(250),width=150,height=90,fill=0)
    cnv.drawString(mp(75),mp(275),razao_social+ " CPF/CNPJ: " + cpf_cnpj)
    cnv.drawString(mp(75),mp(270),nome_fantasia)
    cnv.drawString(mp(75),mp(265),end + ","+"Nº "+ num) 
    cnv.drawString(mp(75),mp(260),bairro + ","+ cep + " - " + cidade + "/" + uf)


    # Conteudo

    cnv.drawString(mp(10),mp(230),"Código")
    cnv.drawString(mp(30),mp(230),"Nome")
    cnv.drawString(mp(80),mp(230),"Telefone")
    cnv.drawString(mp(110),mp(230),"Email")

    #Conexão com Banco de Dados
    connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
    mycursor = connection.cursor()

    sqlid = "select cod_cliente,nome_cliente,celular_cliente,email_cliente from clientes;"# sql para pegar os clientes
    mycursor.execute(sqlid)

    i = 220
    for cliente in mycursor:
      codigo = cliente[0]
      nome = cliente[1]
      telefone = cliente[2]
      email = cliente[3]
      y = mp(i)

      cnv.drawString(mp(10),y,str(codigo))
      cnv.drawString(mp(30),y,nome)
      cnv.drawString(mp(80),y,telefone)
      cnv.drawString(mp(110),y,email)

      i = i - 5 
    
    cnv.save()

    os.startfile(pastaSalva+"\\Relatorios\Clientes\Relatorio1.pdf")

  except:
    messagebox.showinfo(title="ERRO", message="Erro ao criar PDF")

RelatorioClientes_window = Toplevel()
RelatorioClientes_window.title("Lanchonete | Relatório CLientes")
RelatorioClientes_window.resizable(False, False) 
RelatorioClientes_window.geometry("750x500")      
RelatorioClientes_window.iconbitmap("imagens/ico.lanchonete.ico")
RelatorioClientes_window.configure(bg="#DCDCDC")

btn=Button(RelatorioClientes_window,text="Criar PDF",command=criarRelatoriosCliente)
btn.pack(side="left",padx=10)



RelatorioClientes_window.mainloop()








