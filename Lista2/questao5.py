#escreva uma função que receba uma seuqencia de listas e retorne
#o maior elemento contido nelas:
#ex: f([1,2,3,4], [5,6,7,8])
#resultado : 8
lista1 = [-1,-2,-3,-4]
lista2 = [5,6,7,8]



def conc (lis1, lis2):
    if lis1 != []:
        return lis1 + [,lis2[0]] + conc (lis1,lis2[1:])

    if

def funca (lista1, lista2):
    if not lista1:
        return mai (lista2, ma)
    if not lista1 and not lista2:
        return ma
    
    def mai (l, ma):
        if not l:
            return funca(l,lista2)
               
        if l[0] > ma:
            return mai(l[1:], ma=l[0])
        return mai(l[1:], ma)
    return mai(lista1, ma=lista1[0])






print (funca(lista1, lista2))
