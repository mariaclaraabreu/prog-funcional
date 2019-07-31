print("Digite um numero")
n = input()
it = 1
cont=0

def fun (n, it, cont):
    if it <= n:
        if n % it == 0:
            return fun(n, it+1, cont+1)

    else:
        if cont <=2:
            return "primo"
        else:
            return "Nao-primo"

print (fun(n, it, cont))
