import mysql.connector
from tkinter import *

cnx = mysql.connector.connect(host='localhost',
                              user='root')
cursor=cnx.cursor()

query = "create database IF NOT EXISTS kingburguer"
cursor.execute(query)

query = "use kingburguer"
cursor.execute(query)

query= "CREATE TABLE IF NOT EXISTS registros(\
    id INT(5) AUTO_INCREMENT PRIMARY KEY,\
    nome VARCHAR(20) NOT NULL,\
    sobrenome VARCHAR(30) NOT NULL,\
    telefone VARCHAR(9) NOT NULL,\
    email VARCHAR(30)\
)"
cursor.execute(query)

opcao=4
while opcao!=0:
    opcao=int(input('1-inserir registros / 2-ver registros / 3-excluir registros / 0-sair :'))
    while opcao!=1 and opcao!=2 and opcao!=3 and opcao!=0:
        print("Opção inválida.")
        opcao=int(input('1-inserir registros / 2-ver registros / 3-excluir registros / 0-sair :'))
    if opcao==1:
        nome=str(input("nome: "))
        sobrenome=str(input("sobrenome: "))
        telefone=str(input("telefone: "))
        email=str(input("email: "))
        query = "insert into registros (nome, sobrenome, telefone, email) values ('{}','{}','{}','{}')".format(nome, sobrenome, telefone, email)
        cursor.execute(query)
        cnx.commit()
        print("registro inserido!")
        print()

    elif opcao==2:
        query = ("SELECT * from registros")
        cursor.execute(query)
        print("==========================REGISTROS===============================")
        for (id, nome, sobrenome, telefone, email) in cursor:
            print(id, nome, sobrenome, telefone, email)
        print()  

    elif opcao==3:
        id=str(input('Informe o ID do registro a ser excluído: '))
        query = "delete from registros where id = '{}'".format(id)
        cursor.execute(query)
        cnx.commit()
        print("Registro excluido")
        print()

cursor.close()
cnx.close()
