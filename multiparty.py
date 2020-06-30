#https://chaum.com/publications/multiparty_computation.pdf

import random as R

def prety(L):
    print "----"
    for _l in L:
        print _l


# escolhe as linhas de T que sao "iguais escolha" antes da mascara
# sel sao os indices do subconjunto de T
def getLines(T,col,escolha,sel,mascara):
    r=[]
    for i in sel:
        if escolha ^ mascara == T[i][col]:
            r.append(i)
    return r
        
#nomenclatura do artigo
def inversion(T,col):
    b = bool(R.getrandbits(1))
    for l in TT:
        l[col] = l[col]^b
    return b

#nomenclatura do artigo
def encryptionOutCol(T,colOut,colCommit):
    d = [bool(R.getrandbits(1)) for _ in range(4)]
    for i in range(4):
        T[i][colOut] = T[i][colOut]^d[i]
        T[i][colCommit] = d[i]
    return d



def function_and(a,b):
    return a and b

def function_or(a,b):
    return a or b

def function_greater(a,b):
    return (a==1) and (b==0)


    
for teste in range(1000):
    #Tabela Verdade
    # Entrada A, Entrada B, Saida, COmmi A,commit B)
    
    TT = [ [False,False,False,False,False],
           [False,True,False,False,False],
           [True,False,False,False,False],
           [True,True,True,False,False]
    ]

    # escolhe a funcao 
    f = function_greater
    #inicializa a tabela
    for l in TT:
        l[2] = f(l[0],l[1])


    # Esta computacao eh privada... A executa no seu computador
    # 1.1
    # Falta armazenar o embaralhamento para poder fazer o commit
    R.shuffle(TT)

    #1.2 - Inversion
    bA1 = inversion(TT,0)
    bA3 = inversion(TT,2)
    #1.3
    dA = encryptionOutCol(TT,2,3)
    
    #1.4 Commit
    # Falta....


    #A envia para B pelo SC....
    

    # B pega pelo SC e executa em seu computador
    # Falta armazenar o embaralhamento para poder fazer o commit
    R.shuffle(TT) #4.1

    # 4.2
    dB = encryptionOutCol(TT,2,4)
    bB2 = inversion(TT,1) 
    bB3 = inversion(TT,2) 


    # desconsiderando o laço de teste, esta parte sera executada no smart contract
    # o SC contera o resultado da operacao sem conhecer os operandos
    for _ in range(10000):
        escolhaA = bool(R.getrandbits(1))
        linhasA = getLines(TT,0,escolhaA,[0,1,2,3],bA1)
        escolhaB = bool(R.getrandbits(1))
        linhasB = getLines(TT,1,escolhaB,linhasA,bB2)
        print escolhaA,escolhaB,TT[linhasB[0]][2] ^ TT[linhasB[0]][3] ^TT[linhasB[0]][4]  ^bA3 ^bB3
        assert( f(escolhaA,escolhaB) == (TT[linhasB[0]][2] ^ TT[linhasB[0]][3] ^TT[linhasB[0]][4])^bA3 ^bB3)
    
