#!/usr/bin/python3

from brownie import *
import brownie 
import random as R


def linear(T):
    r=[]
    for l in T:
        r.extend(l)
    return r

def function_and(a,b):
    return a and b

def function_or(a,b):
    return a or b

def function_greater(a,b):
    return (a==1) and (b==0)


def shuffle(T):
    s = [0,1,2,3]
    R.shuffle(s)
    r =[]
    for i in s:
        r.append([_ for _ in T[i]])
    return (r,s)


#nomenclatura do artigo
def inversion(T,col):
    b = bool(R.getrandbits(1))
    for l in T:
        l[col] = l[col]^b
    return b

#nomenclatura do artigo
def encryptionOutCol(T,colOut,colCommit):
    d = [bool(R.getrandbits(1)) for _ in range(4)]
    for i in range(4):
        T[i][colOut] = T[i][colOut]^d[i]
        #T[i][colCommit] = d[i]
    return d


def main():

    TT = [ [False,False,False],
           [False,True,False],
           [True,False,False],
           [True,True,False]
    ]

    # escolhe a funcao 
    f = function_and

    
    #inicializa a tabela
    for l in TT:
        l[2] = f(l[0],l[1])

    print('TT:',TT)
    
    #escolhas
    escolhaA = bool(R.getrandbits(1))
    escolhaB = bool(R.getrandbits(1))

    print('Escolha de A:',escolhaA)
    print('Escolha de B:',escolhaB)
    
    # 1.1    
    (TTA,shuffleA) = shuffle(TT)
    
    print('Antes:',TTA)
    bA1 = inversion(TTA,0)
    bA3 = inversion(TTA,2)

    print('Inversao bA1:',bA1)
    print('Inversao bA3:',bA3)

    print('Depois:',TTA)
    
    #1.3
    #dA = encryptionOutCol(TT,2,3)
    
    #1.4 Commit
    # Falta....

    
    smc = SMC.deploy(linear(TT),linear(TTA),{'from': accounts[0]})

    #

    lida = smc.getTTA.call({'from': accounts[1]})
    print('TT Recebida por B',lida)

    
    (TTB,shuffleB) = shuffle(lida) #4.1

    print('shuffle de B:',TTB)
    # 4.2
    #dB = encryptionOutCol(TTB,2,4)
    bB2 = inversion(TTB,1) 
    bB3 = inversion(TTB,2)
    
    print('Inversao bB2:',bB2)
    print('Inversao bB3:',bB3)

    print(TTB)
    
    # envia
    smc.receiveTableFromB(TTB,{'from': accounts[1]})

    # A pega a tabela modificada de B
    lidaA = smc.getTTB.call({'from': accounts[0]})


    # A escolhe as linhas
    linhasA=[0,0]
    idx=0
    for i in range(len(lidaA)):
        if (lidaA[i][1] ^ bA1) == escolhaA:
            linhasA[idx]=i
            idx+=1
    smc.receiveLinesFromA(linhasA[0],linhasA[1],{'from': accounts[0]})

    
    # B escolhe as linhas
    linhasB=[0,0]
    idx=0
    for i in range(len(TTB)):
        if (TTB[i][1] ^ bB2) == escolhaB:
            linhasB[idx]=i
            idx+=1

    print('Linhas de B:',linhasB)
    smc.receiveLinesFromB(linhasB[0],linhasB[1],{'from': accounts[0]})

    # A envia as inversoes
    smc.receiveInversionFromA(bA3,{'from': accounts[0]})
    # B envia as inversoes
    smc.receiveInversionFromB(bB3,{'from': accounts[1]})
    
    # contrato calcula... e FIM!
    ra = smc.getValue.call({'from': accounts[0]})
    rb = smc.getValue.call({'from': accounts[1]})

   

    print ('SAIDA:',ra == f(escolhaA,escolhaB))

