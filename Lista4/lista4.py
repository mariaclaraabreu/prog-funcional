
# 1) Crie uma lista com todos os números primos entre 1 e 1000


def primo (n):
    def veri (n, it, cont):
        if it>n:
            if cont == 2:
                return n
            return False
        if n % it == 0:
            return veri (n,it+1, cont+1)
        return veri (n,it+1, cont)
    return veri (n,1,0)

pri = [x for x in range (1,100) if primo (x)] 


# 2) Crie uma lista com os 100 primeiros elementos da série de fibonacci

def termofib (n) :
    def f(num, fib1,fib2,fib3):
        if num == n:
            return fib3
        fib3=fib1+fib2
        fib1=fib2
        fib2=fib3
        return f(num+1,fib1,fib2,fib3)

    return f(0,1,0,0)  

fibonacci = [ termofib (n) for n in range (1,101) ]

  
# 3) Crie uma lista com 100 números triangulares
#Tr= (n(n+1))/2

def func (num):
    def triang (n, inc, cont):
        if cont >= num:
            return []
        return [n + inc] + triang (n+inc, inc+1, cont+1)      
    return triang (0, inc = 0, cont=0)


# Usando compreensão de lista

triangular = [(x*(x+1))/2 for x in range(101)]



# 4) Crie uma lista com todos os números perfeitos entre 1 e 1000

def fun (num):
    def perfeito(n, it, soma):
        if it==n:
            if soma == n:
                return [n] 
            return False
        if n % it == 0:
            soma+=it
            return perfeito(n, it+1, soma)
        return perfeito(n, it+1, soma)

    return perfeito(num, it=1, soma=0)

perfeitos = [fun(x) for x in range (1,100) if fun (x) != False]




# 5) Crie uma lista com todos os 100 primeiros números quadrados perfeitos

def quadPerf (num):
    def quad(n, q=0):
        if n*n > 0:
            q=n*n
            return q
        return False

    return quad (num)

quadrado = [quadPerf(x) for x in range (1,100) if quadPerf(x)]


