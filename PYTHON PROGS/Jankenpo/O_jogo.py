from tkinter import *
from random import choice
from time import sleep


cont=0
pc,pj=0,0

#cliques dos botôes
def bt1_click():
    ep='pedra'
    ec=choice(['pedra','papel','tesoura'])
    if ep == ec:
        lb['text'] = 'Empate!!'
    elif ec=='tesoura':
        lb['text'] = 'Você ganhou!!'
        pj=pj+1
        return pj
    else:
        lb['text'] = 'O computador ganhou!!'
        pc=pc+1
        return pc
    escolha['text'] = 'O computador escolheu {}'.format(ec)

def bt2_click():
    ep='papel'
    ec=choice(['pedra','papel','tesoura'])
    if ep == ec:
        lb['text'] = 'Empate!!'
    elif ec=='pedra':
        lb['text'] = 'Você ganhou!!'
        pj=pj+1
        return pj
    else:
        lb['text'] = 'O computador ganhou!!'
        pc=pc+1
        return pc
    escolha['text'] = 'O computador escolheu {}'.format(ec)

def bt3_click():
    ep='tesoura'
    ec=choice(['pedra','papel','tesoura'])
    if ep == ec:
        lb['text'] = 'Empate!!'
    elif ec=='papel':
        lb['text'] = 'Você ganhou!!'
        pj=pj+1
        return pj
    else:
        lb['text'] = 'O computador ganhou!!'
        pc=pc+1
        return pc
    escolha['text'] = 'O computador escolheu {}'.format(ec)
    
  
janela=Tk()
janela.geometry('750x500+0+0')
janela.title('Pedra Papel ou Tesoura')
janela.configure(background='#FFD043')

#titulo
lblTitulo = Label(janela, font=('arial', 20, 'bold'), text='Pedra Papel ou Tesoura')
lblTitulo.pack(side=TOP, fill = BOTH)


#botôes
    #botao 1
picpedra = PhotoImage(file= 'Pedra.png')
bt1 = Button(janela,image=picpedra, width=140, height=100,command=bt1_click)
bt1.place(x=100, y=300)

    #botao 2
picpapel = PhotoImage(file= 'Papel.png')
bt2 = Button(janela,image = picpapel, width=140, height=100, text='Papel',command=bt2_click)
bt2.place(x=300, y=300)

    #botao 3
pictesoura = PhotoImage(file= 'Tesoura.png')
bt3 = Button(janela, image=pictesoura, width=140, height=100, text='Tesoura',command=bt3_click)
bt3.place(x=500, y=300)

#resultado
lb = Label(janela, width = 30, height = 2, font=('arial', 18, 'bold'), text='Faça sua escolha')
lb.place(x=150, y=410)
lb.configure(background='#FFD043')

#escolha do computador
escolha = Label(janela, width = 30, height = 2, font=('arial', 18, 'bold'), text='')
escolha.place(x=150, y=200)
escolha.configure(background='#FFD043')

##placar
pontuacao = Label(janela, width = 59, height = 2, font=('arial', 12, 'bold'), text=('Computador        {}   X   {}         Jogador'.format(pc,pj)))
pontuacao.pack(side=TOP,fill = BOTH)
pontuacao.configure(background='#FFD043')


janela.mainloop()
