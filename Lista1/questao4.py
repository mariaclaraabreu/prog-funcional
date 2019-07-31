lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
tupla = ()
def fun (lista1, lista2, tupla):
    if len(lista1) and len(lista2)==0:
        return 0
    else:
        tupla = (lista1[0], lista2[0] )
        return fun (lista1[1:], lista2[1:], tupla)

print (fun (lista1, lista2, tupla))