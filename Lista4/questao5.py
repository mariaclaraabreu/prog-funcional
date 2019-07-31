# 5) Crie uma lista com todos os 100 primeiros números quadrados perfeitos

def fun (num):
    if num == 0:
        return []
    def quad(n, q=0):
        if n==num:
            return []
        if n*n > 0:
            q=n*n
            return [q] + quad (n+1)
        return quad (n+1)

    return quad (1)

#print (fun(100))



