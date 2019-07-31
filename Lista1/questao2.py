

def pares(numero):
    if numero % 2 ==0:
        return True
    else:
        return False

def fun(lista):
    if len(lista)==1:
        return 0
    else:
        lista((filter(pares, lista)))
        return fun(lista[1:])

print (fun([1,5,6]))
