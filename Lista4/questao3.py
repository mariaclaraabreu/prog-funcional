#Crie uma lista com 100 números triangulares
#Tr= (n(n+1))/2

def func (num):
    def triang (n, inc, cont):
        if cont >= num:
            return []
        return [n + inc] + triang (n+inc, inc+1, cont+1)      
    return triang (0, inc = 0, cont=0)

print (func(100))

# Usando compreensão de lista

triangular = [(x*(x+1))/2 for x in range(101)]
print (triangular)

