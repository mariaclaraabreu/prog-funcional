# 1) Escreva uma funçao que receba uma lista ou tupla e retorne a
#soma de todos os elementos numericos

def somatorio (lista):
    if lista == []:
        return 0
    if type (lista[0]) == int:
             return lista[0] + somatorio(lista[1:])
    return somatorio (lista[1:])



# 2) Escreva uma função que receba uma lista de números e um filtro e retorne
# uma lista com todos os elementos que satisfazem o filtro
#ex: func ([1,2,3,4,5,6], par)
# saida: [2,4,6]
#filtro: uma função que retorna true ou false


def par (num):
    return num % 2 == 0

def impar (num):
    return num % 2 != 0


def func (lista, funcao):
    if not lista:
        return []
    if funcao(lista[0]):
        return [lista[0]] + func (lista[1:], funcao)
    return func (lista[1:], funcao)




# 3) Escreva uma função que receba uma lista e um pivô (índice) e retorne duas
# listas, uma com todos os numeros menores que o pivo e outra  com os maiores ou
# iguais. Não permita que ocorra index error

def mem (lista, pivo):
    def menores (l, p, lmenores,var):
        if not l:
            return maiores(lista, pivo, [] , lista[pivo], lmenores)
        if l[0] < var:
            return menores(l[1:],p, lmenores + [l[0]], var)
        return menores(l[1:],p, lmenores,var)
    def maiores (l2, p2, lmaiores,var2, lmenores):
        if not l2:
            return lmaiores, lmenores 
        if l2[0] >= var2:
            return maiores(l2[1:],p2, lmaiores + [l2[0]], var2, lmenores)
        return maiores(l2[1:],p2, lmaiores,var2,lmenores) 
    return menores (lista, pivo,[],lista[pivo])
        


# 4) Escreva uma função que receba duas listas e retorne uma lista de tuplas com
# os elementos de ambas as listas que tenha o mesmo indice. Complete com um
# caractere "-" caso as listas tenham tamanhos diferentes.
# func ([1,2,3,4], [3,4,5,6,7])
# saida: [(1,3), (2,4), (3,5)

def ltuplas (lista1,lista2):
    def lt (l1,l2,l):
        if not l1 and not l2:
            return l
        if not l1:
            l+=[('-',l2[0])]
            return lt(l1,l2[1:],l)
        if not l2:
            l+=[(l1[0],'-')]
            return lt(l1[1:],l2,l)
        l+=[(l1[0],l2[0])]
        return lt(l1[1:],l2[1:],l)

    return lt(lista1, lista2, [])




# 5) Escreva uma funcao que receba um natural n e diga se ele é primo

def primo (num):
    def verifica (num, it, cont):
        if it>num:
            if cont==2:
                return "eh primo"
            return "nao primo"
        if num % it == 0:
            return verifica (num, it+1, cont+1)
        return verifica (num, it+1, cont)


    return verifica(num,1,0)
    


# 6) Escreva uma função que receba um natural n e gere uma sequência de n números
# primos

def seqPrimos (n):
    if n == 0:
        return []
    def ver (n,it,cont):
        if it>n:
            if cont==2:
                return seqPrimos(n-1) + [n]
            return seqPrimos(n-1)
        if n % it==0:
            return ver (n,it+1,cont+1)
        return ver (n,it+1,cont)
    return ver (n,1,0)






