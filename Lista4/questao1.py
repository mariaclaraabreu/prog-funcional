#1) Crie uma lista com todos os números primos entre 1 e 1000

def primos (num):

    def ver(num, it, cont):
        if num == 0:
            return []
        if it>num:
            if cont == 2:
                return [num] + ver (num-1, 1, 0)
            return ver (num-1, 1,0)
        if num % it == 0:
            return ver (num, it+1, cont+1)
        return ver (num, it+1, cont)

    return ver (num-1, it=1, cont=0)


print (primos(30))


    
    
