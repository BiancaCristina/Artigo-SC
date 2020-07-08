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

    # 1.1    
    (TTA,shuffleA) = shuffle(TT)

    bA1 = inversion(TT,0)
    bA3 = inversion(TT,2)
    #1.3
    dA = encryptionOutCol(TT,2,3)
    
    #1.4 Commit
    # Falta....

    
    smc = SMC.deploy(linear(TT),linear(TTA),{'from': accounts[0]})

    #

    lida = smc.getTTA.call({'from': accounts[1]})
    print(lida)

    
    (TTB,shuffleB) = shuffle(lida) #4.1

    print(TTB)
    # 4.2
    dB = encryptionOutCol(TTB,2,4)
    bB2 = inversion(TTB,1) 
    bB3 = inversion(TTB,2) 

    
    # envia
    smc.receivesTableFromB(linear(TTB),{'from': accounts[1]})

    

    # A pega a tabela modificada de B

    # A escolhe as linhas

    # B escolhe as linhas

    # A envia as inversoes

    # B envia as inversoes

    # contrato calcula... e FIM!

    
