from tkinter import *
from produtos import MainProdutos
from clientes import MainClientes
from usuario import MainUsuario
from vendas import MainVendas
# from login import User
from cadastro_empresa import MainEmpresa
from cadastro_Fornecedor import MainFornecedor
from TipoPagamento import TipoPagamentos
from entradaNotas import MainMEntradaDeNotas
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
 

def MainMenu():
    def quit_window():
      if messagebox.askokcancel("Sair","Deseja realmente sair?"):
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
        mycursor = connection.cursor()

        sqlDeleteUsuario = "DELETE FROM  log_usuario "
        mycursor.execute(sqlDeleteUsuario)
        connection.commit()    

        window.destroy()
    # ------------Opening Window----------------------------------
    window = Tk()
    window.title("Lanchonete | Menu")
    window.geometry("750x500") # WxH
    window.configure(bg="#DCDCDC")
    window.iconbitmap("imagens/ico.lanchonete.ico")
    window.protocol("WM_DELETE_WINDOW",quit_window)

    # print(user)

    
    # def Logoff(): # função para deslogar
    #     logoff = messagebox.askokcancel("Logoff","Deseja realmete deslogar desse usuário?")
    #     if logoff == 1:
    #         window.destroy()
    #         MainLogin()
    #     else:
    #         pass

    # ------------imagem----------------------------------
    img = ImageTk.PhotoImage(Image.open("imagens/img_menu.jpg"))
    panel = Label(image = img)
    panel.grid(row=0,column=0)
    # ------------Widgets----------------------------------
    lblanchonetename = Label(window, text="Sistema Lanchonete",bg="black", fg="white", bd=10, font="Broadway 35 bold")
    lblanchonetename.place(x=100,y=5)

    # framelogin = Frame(window, background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3) # C0C0C0 == Silver
    # framelogin.place(relwidth=0.60,relheight=0.75,relx=0.2,rely=0.15)

    #botões
    imgpro = PhotoImage(file="Imagens/ico.produtos.png")
    imgcli = PhotoImage(file="Imagens/ico.cliente.png")
    imgusu = PhotoImage(file="Imagens/ico.usuario.png")
    imgven = PhotoImage(file="Imagens/ico.vendas.png")
    imgrela = PhotoImage(file="Imagens/ico.relatorio.png")
    
    
    btprodutos = Button(window,text="Produtos",image = imgpro, bg="#DCDCDC", width= 120, height=60, padx=20, pady=10, borderwidth=4, command=MainProdutos)
    btprodutos.place(x=10,y=80)

    btclientes = Button(window,text="Clientes",image= imgcli, bg="#DCDCDC", width= 120, height=60, padx=20, pady=10, borderwidth=4, command=MainClientes)
    btclientes.place(x=10,y=150)

    btusuario = Button(window,text="Usuários",image= imgusu, bg="#DCDCDC", width= 120, height=60, padx=20, pady=10, borderwidth=4, command=MainUsuario)
    btusuario.place(x=10,y=220)

    btvendas = Button(window,text="Vendas",image = imgven, bg="#DCDCDC", width= 120, height=60, padx=20, pady=10, borderwidth=4, command=MainVendas)
    btvendas.place(x=10,y=290)

    btvendas = Button(window,text="Relatórios", image = imgrela, bg="#DCDCDC", width= 120, height=60, padx=20, pady=10, borderwidth=4)
    btvendas.place(x=10,y=360)

    #menu
    menu_bar = Menu(window)

    arquivo = Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label="Arquivo",menu=arquivo)
    arquivo.add_command(label="Imprimir")
    arquivo.add_separator()
    arquivo.add_command(label="Logoff")
    arquivo.add_separator()   
    arquivo.add_command(label="Sair",command=quit_window)

    exibir = Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label="Exibir",menu=exibir)
    exibir.add_command(label="Vendas",command=MainVendas)
    exibir.add_separator()
    exibir.add_command(label="Clientes",command=MainClientes)
    exibir.add_separator()   
    exibir.add_command(label="Usuários",command=MainUsuario)
    exibir.add_separator() 
    exibir.add_command(label="Empresa",command=MainEmpresa)
    exibir.add_separator()
    exibir.add_command(label="Fornecedor",command=MainFornecedor)
    exibir.add_separator()  
    exibir.add_command(label="Tipos Pagamentos",command=TipoPagamentos)
    
    estoque = Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label="Estoque",menu=estoque)
    estoque.add_command(label="Entrada de Notas",command=MainMEntradaDeNotas)

    exibir = Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label="Ajuda",menu=exibir)
    exibir.add_command(label="Tutorial")
    exibir.add_separator()
    exibir.add_command(label="Suporte técnico")
    exibir.add_separator()   
    exibir.add_command(label="Telefone e informações de contato")

    

    window.configure(menu=menu_bar)

    

    # ------------Loop End----------------------------------
    window.mainloop()
