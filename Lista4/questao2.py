#Crie uma lista com os 100 primeiros elementos da série de fibonacci
def fib(num=100):
    def fib2(num, aux1,aux2,aux3):
        if num == 0:
            return[]
        if num!=0:
            aux3= aux1 +aux2
            aux1=aux2
            aux2=aux3
            num=num-1
            return [aux3,] + fib2(num-1,aux1,aux2,aux3)
    return  fib2(num,1,0,0)

print (fib())
