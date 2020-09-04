import tkinter as gui
from tkinter import *
from menu import MainMenu
from tkinter import messagebox
import mysql.connector

def MainLogin():

      #-------------Função para sair----------------
      def ExitWindow():
            if messagebox.askyesno("Sair","Deseja realmente sair?"):
                  window.destroy()

      #-------------Função para avaliar login senha----------------
      def ValidarUser():
            user = str(entryuser.get())
            password = str(entrypassword.get())
            
            connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
            mycursor = connection.cursor()

            sqlselect = "select * from usuarios where nome like '"+user+"' and senha like '"+password+"' "  # like (parecido com)
            #print(sqlselect)
            mycursor.execute(sqlselect)
            valido = mycursor.fetchall()

            if len(valido) > 0:
                  window.destroy()
                  btentrar["command"] = MainMenu()
            else:
                  messagebox.showwarning("Warning","Usuário ou senha inválida!")
                  # entryuser.delete(0, END)
                  entrypassword.delete(0, END)

            mycursor.close()
            connection.commit()
            connection.close()

      # -------------Opening Window------------------
      window = gui.Tk()
      window.title("Lanchonete | Login")
      window.configure(bg="#DCDCDC") # Gainsboro = #DCDCDC
      window.resizable(False,False)
      window.geometry("750x500") # WxH
      window.iconbitmap("imagens/ico.lanchonete.ico")	

      #------------Frames-----------------------
      framelogin = gui.Frame(window, background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3) # C0C0C0 == Silver
      framelogin.place(relwidth=0.60,relheight=0.75,relx=0.2,rely=0.15)
      # relwidth = largura do lado direito
      # relheight = altura de baixo
      # relx = largura do lado esquerdo (eixo x)
      # rely = altura de cima (eixo y)

      #------------ Widgets----------------------
      #labels
      lblanchonetename = gui.Label(window, text="Sistema Lanchonete", bg="#DCDCDC", fg="#363636", bd=0.01, font="Broadway 35 bold")
      lblogin = gui.Label(framelogin, text="Login", font="Britannic 40 bold", bg="#C0C0C0")
      lbuser = gui.Label(framelogin, text="Usuário:", font="Britannic 15 bold", bg="#C0C0C0")
      lbpassword = gui.Label(framelogin, text="Senha:", font="Britannic 15 bold", bg="#C0C0C0")
      #entrys
      entryuser = gui.Entry(framelogin, width=32, borderwidth=5)
      entrypassword = gui.Entry(framelogin, width=32, borderwidth=5,show="*")
      #botões
      btentrar = gui.Button(framelogin, text="Entrar", padx=60, pady=5, command=ValidarUser, borderwidth=5, bg="#C0C0C0", font="Britannic 9 bold")
      btexit = gui.Button(framelogin, text="Sair", fg="red", padx=20, pady=5, command=ExitWindow,borderwidth=5, bg="#C0C0C0", font="Britannic 9 bold")

      #---------------Layout widgets------------------------
      lblanchonetename.place(x=115,y=0)
      lblogin.place(x=180,y=20)
      lbuser.place(x=180,y=100)
      lbpassword.place(x=180,y=180)
      entryuser.place(x=185,y=140)
      entrypassword.place(x=185,y=220)
      btentrar.place(x=197, y=270)
      btexit.place(x=10, y=300)

      #-------------Image----------------------------
      img = PhotoImage(file= "imagens/login4.png")
      lbimage = gui.Label(framelogin, image= img, bg="#C0C0C0")
      lbimage.place(x=10,y=85)
      entryuser.focus()

      # -------------Loop End----------------------------
      window.mainloop()

MainLogin()