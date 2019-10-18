import datetime
import mysql.connector

cnx = mysql.connector.connect(host='localhost',
                              user='root',
                              password='')
cursor = cnx.cursor()

opcao=1
while opcao!=3:
    opcao=int(input("1-inclui / 2-lista / 3-sai / 4-excluir: "))
    if opcao==1:
        nome=str(input("nome:"))
        telefone=str(input("telefone:"))
        query = "INSERT INTO teste (nome, telefone) VALUES (%s, %s)"
        val = (nome, telefone)
        cursor.execute(query,val)
        cnx.commit()
        print("Registro inserido")
        print()
        
    elif opcao==2:
        query = ("SELECT * from teste")
        cursor.execute(query)
        for (nome, telefone) in cursor:
            print(nome,telefone)
        print()    

    elif opcao==4:
        telefone=str(input('Informe o telefone do registro a ser excluído:'))
        query = "delete from teste where telefone = '{}'".format(telefone)
        cursor.execute(query)
        cnx.commit()
        print("Registro excluido")
        print()

cursor.close()
cnx.close()
