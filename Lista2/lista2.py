# 1) Escreva uma função que receba uma lista com número e a ordene. A função
# deve ter uma opção para ordem reversa.
#Ex: ordena (lista, reverso=false)

#[5,3,2,4]

def ordena (l, op):
    if not l:
        return []
    def ord (l,op,numerolista,armaz):
        if numerolista<=l[0]:
            return ord (l[1:],op,numerolista,armaz)
        




    return ord(l, op,l[0],0)




# 2) Escreva uma função que receba duas listas numéricas e retorne uma única
#lista com os elementos da entrada intercalados
#Ex: f([1,2,3,4],[5,6,7,8])
#saida: [1,5,2,6,3,7,4,8]
#obs: as listas não precisam ter o mesmo tamanho  OK

def interc (l1,l2):
    def inter (lis1,lis2,l):
        if not lis1 and not lis2:
            return l
        if not lis1:
            return inter(lis1,lis2[1:],l+[lis2[0]])
        if not lis2:
            return inter (lis1[1:],lis2,l+[lis1[0]])
        return inter (lis1[1:],lis2[1:],l+[lis1[0], lis2[0]])

    return inter(l1,l2,[])



# 3) escreva uma função que receba um natural n e retorne o n-ésimo termo da
# sequencia de finacci   OK

def termofib (n) :
    def f(num, fib1,fib2,fib3):
        if num == n:
            return fib3
        fib3=fib1+fib2
        fib1=fib2
        fib2=fib3
        return f(num+1,fib1,fib2,fib3)

    return f(0,1,0,0)  



# 4) escreva uma função que receba um natural n e uma função geradora. A função
# deve retornar uma lista de n numeros gerados de acordo com a geradora
#Ex: f(5,fibonacci)
#saida: [1,1,3,4,7]

def par (n):
    if n ==0:
        return []
    if n % 2 == 0:
        return [n] + (par(n-1))
    return par(n-1)

def primo (n):
    if n == 0:
        return []
    def verificar (n, it, cont):
        if it>n:
            if cont == 2:
                return [n] + (primo(n-1))
            return primo(n-1)
        if n % it ==0:
            return verificar (n, it+1, cont+1)
        return verificar (n, it+1, cont)
    return verificar (n,1,0)
        

def geradora (n, opcao):
    if opcao == par:
        return par (n)
    if opcao == primo:
        return primo(n)




# 5) Escreva uma função que receba uma sequeência de listas e retorna o maior
# elemento contido nelas
#ex: f([1,2,3,4],[5,6,7,8])
#saida: 8


def maiorr (lista1,lista2):
    def ma (l1,l2,maior):
        if not l1 and not l2:
            return maior
        if not l1:
            if l2[0] > maior:
                return ma(l1,l2[1:],maior=l2[0])
            return ma(l1,l2[1:],maior)
        if not l2:
            if l1[0]>maior:
                return ma (l1[1:],l2,maior=l1[0])
            return ma (l1[1:],l2,maior)
        if l1[0] > l2[0]:
            return ma (l1[1:],l2[1:], maior = l1[0])
        return ma (l1[1:],l2[1:], maior = l2[0])
    return ma(lista1,lista2,0)





#def maior (*listas):
 #   def m(l,ma):
  #      if not l:
   #         return ma
    #    if l[0]>ma:
     #       return m(l[1:],ma=l[0])
      #  return m(l[1:],ma)
    #return m(listas,0)


# 6) Escreva uma função que receba duas listas numéricas e retorne uma lista de
#tuplas com o produto cartesiano da entrada
#ex: f ([1,2,3],[4,5,6])
#saida: [(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)]
