lista = [1,2,3,4,5,6]
pivo = input()

def fun (lista, pivo, lista1=[], lista2=[]):
    if len(lista)==0:
        return 0
    else:
        if lista[0]<pivo:
            lista1=lista[0]
            return  fun(lista[1:], pivo, lista1, lista2)
        if lista[0]>=pivo:
            lista2=lista[0]
            return fun(lista[1:], pivo, lista1, lista2)

print (fun(lista, pivo))
