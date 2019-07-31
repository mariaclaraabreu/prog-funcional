# 4) Crie uma lista com todos os números perfeitos entre 1 e 1000

def fun (num):
    if num == 0:
        return []
    def perfeito(n, it, soma):
        if it==n:
            if soma == n:
                return [n] + fun (num-1)
            return fun (num-1)
        
        if n % it == 0:
            soma+=it
            return perfeito(n, it+1, soma)
        return perfeito(n, it+1, soma)

    return perfeito(num, it=1, soma=0)

print (fun(40))

def funee (num):
    def perfeito(n, it, soma):

        if it==n:
            if soma == n:
                return True
            return False
        
        if n % it == 0:
            soma+=it
            return perfeito(n, it+1, soma)
        return perfeito(n, it+1, soma)

    return perfeito(num, it=1, soma=0)



triangular = [(x*(x+1))/2 for x in range(101)]

#p = [num = fun(n), num==True for n in range(101)]


