import mysql.connector
from tkinter import *
from tkinter import messagebox

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


def btsalvar_click():
    nome=entrynome.get()
    nome.strip()
    nome.capitalize()
        
    sobrenome=entrysn.get()
    sobrenome.strip()
    sobrenome.capitalize()
    
    telefone=entrytel.get()
    telefone.strip()
    
    email=entryemail.get()
    email.strip()
    
    entrynome.delete(first=0, last=200)
    entrysn.delete(first=0, last=200)
    entrytel.delete(first=0, last=200)
    entryemail.delete(first=0, last=200)
    query = "insert into registros (nome, sobrenome, telefone, email) values ('{}','{}','{}','{}')".format(nome, sobrenome, telefone, email)
    cursor.execute(query)
    cnx.commit()
    messagebox.showinfo("Cadastro", "DADOS INSERIDOS!")
    
janela=Tk()
janela.geometry('750x500+0+0')
janela.title('KINGBURGUER')
janela.configure(background='#61BCFF')
#titulo
lblTitulo = Label(janela, font=('arial', 20, 'bold'), text='KINGBURGUER')
lblTitulo.pack(side=TOP, fill = BOTH)

#label1
label1 = Label(janela, font=('arial', 18, 'bold'), text='CADASTRO DE CLIENTES')
label1.place(x=220, y=150)
label1.configure(background='#61BCFF')

#entrada do nome
entrynome = Entry(janela,width=30)
entrynome.place(x=100, y=290)
nomelabel = Label(janela, font=('arial', 10, 'bold'), text='nome:')
nomelabel.place(x=50, y=289)
nomelabel.configure(background='#61BCFF')

#entrada do sobrenome
entrysn = Entry(janela,width=30)
entrysn.place(x=440, y=290)
snlabel = Label(janela, font=('arial', 10, 'bold'), text='sobrenome:')
snlabel.place(x=350, y=289)
snlabel.configure(background='#61BCFF')

#entrada do telefone
entrytel = Entry(janela,width=30)
entrytel.place(x=100, y=350)
tellabel = Label(janela, font=('arial', 10, 'bold'), text='telefone:')
tellabel.place(x=30, y=349)
tellabel.configure(background='#61BCFF')

#entrada do email
entryemail = Entry(janela,width=30)
entryemail.place(x=440, y=350)
emaillabel = Label(janela, font=('arial', 10, 'bold'), text='email:')
emaillabel.place(x=385, y=349)
emaillabel.configure(background='#61BCFF')

#botao salvar
btsalvar = Button(janela, width=10, height=2, text='Salvar', command=btsalvar_click)
btsalvar.place(x=545, y=400)

##opcao=4
##while opcao!=0:
##    opcao=int(input('1-inserir registros / 2-ver registros / 3-excluir registros / 0-sair :'))
##    while opcao!=1 and opcao!=2 and opcao!=3 and opcao!=0:
##        print("Opção inválida.")
##        opcao=int(input('1-inserir registros / 2-ver registros / 3-excluir registros / 0-sair :'))
##    if opcao==1:
##        nome=str(input("nome: "))
##        sobrenome=str(input("sobrenome: "))
##        telefone=str(input("telefone: "))
##        email=str(input("email: "))
##        query = "insert into registros (nome, sobrenome, telefone, email) values ('{}','{}','{}','{}')".format(nome, sobrenome, telefone, email)
##        cursor.execute(query)
##        cnx.commit()
##        print("registro inserido!")
##        print()
##
##    elif opcao==2:
##        query = ("SELECT * from registros")
##        cursor.execute(query)
##        print("==========================REGISTROS===============================")
##        for (id, nome, sobrenome, telefone, email) in cursor:
##            print(id, nome, sobrenome, telefone, email)
##        print()  
##
##    elif opcao==3:
##        id=str(input('Informe o ID do registro a ser excluído: '))
##        query = "delete from registros where id = '{}'".format(id)
##        cursor.execute(query)
##        cnx.commit()
##        print("Registro excluido")
##        print()
##
##cursor.close()
##cnx.close()
