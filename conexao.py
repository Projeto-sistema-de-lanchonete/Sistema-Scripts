import mysql.connector # pip install mysql-connector
import pymysql # pip install pymysq


def ConexaoBanco():

  connection = mysql.connector.connect(host="localhost",user="root",password="",database="bdlanchonete")
  mycursor = connection.cursor()

  return mycursor