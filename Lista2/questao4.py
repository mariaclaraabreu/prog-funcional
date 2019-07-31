#Eescreva um funcao que receba um natural n e uma funcao geradora. A funcao
#deve retornar uma lista de n numeros gerados de acordo com a geradora.
#Ex: f(5
print ("Digite um numero")
n = int(input())
print ("Digite uma opcao geradora:")
opcao = input()

def par (n):
    if n ==0:
        return []
    if n % 2 == 0:
        return [n] + (par(n-1))
    return par(n-1)

def primo (n):
    if n == 0:
        return []
    def verificar (n, it=1, cont=0):
        if it>n:
            if cont == 2:
                return [n] + (primo(n-1))
            return primo(n-1)
        if n % it ==0:
            return verificar (n, it+1, cont+1)
        return verificar (n, it+1, cont)
    return verificar (n)
        

def geradora (n, opcao):
    if opcao == "par":
        return par (n)
    if opcao == "primo":
        return primo(n)


