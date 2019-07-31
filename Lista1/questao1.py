lista = [40, 2, "ui",5,7]
def somaElem(lista):
    if not lista:
        return 0
    if type(lista[0])==int:
        return lista [0] + somaElem (lista[1:])
    else:
        return somaElem(lista[1:])

print (somaElem(lista))


