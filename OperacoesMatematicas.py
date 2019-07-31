def soma_(x,y):
    return x+y
    
def soma(a,b):
    if (a & b) << 1:
        return soma_((a^b),(a & b) << 1)
    return a ^ b

print("SOMA: ", soma_(5,7))

def inversao(x):
    return -x

print("INVERSAO: ", inversao(-10))

def subtracao(x,y):
    return soma(x,inversao(y))

print("SUBTRACAO: ", subtracao(-10, -5))

def multiplicacao(x,y):
    if y > 0:
        return soma(x,multiplicacao(x, y-1))
    elif y < 0:
        return soma(inversao(x),multiplicacao(x, y+1))
    else:
        return 0

print("MULTIPLICACAO: ", multiplicacao(10, -2))

def divisao1(valor,divisor):
    if valor > 0:
        if divisor > 0:
            return 1 + divisao1(subtracao(valor, divisor), divisor)
        elif divisor < 0:
            return inversao(1 + divisao1(subtracao(valor, inversao(divisor)),inversao(divisor)))
    elif valor < 0:
        if divisor < 0:
            return 1 + divisao1(subtracao(valor, divisor), divisor)
        elif divisor > 0:
            return inversao(1 + divisao1(subtracao(inversao(valor), divisor),divisor))
    else:
        return 0

print("DIVISAO1: ", divisao1(10, 2))

def divisao2(x, y, aux = 0):
    if x < y :
        return aux;
    return divisao2(subtracao(x,y), y, aux+1);

print("DIVISAO2: ", divisao2(10, 3))

def incremento(x, inc = 1):
    return soma(x, inc)

print("INCREMENTO: ", incremento(10))

def decremento(x, dec = 1):
    return subtracao(x, dec)

print("DECREMENTO: ", decremento(10))

def potencia(base,expoente):
    if expoente > 0:
        return multiplicacao(base, potencia(base, expoente-1))
    elif expoente < 0:
        #Trocar 1/... por funcao divisao(1,...)
        return 1/potencia(base, inversao(expoente))
    else:
        return 1
    
print("POTENCIA: ", potencia(2, 2))    

def procura(y, base, valor):
        if y <= valor:
            if potencia(y, base) == valor:
                return y
            else:
                return procura(y+1, base, valor)
        else:
            return 0
        
def raizQuadrada(x):
    if x < 0:
        return 0
    else:    
        return procura(1, 2, x)

print("RAIZ QUADRADA: ", raizQuadrada(9))

def raiz(valor, base):
    if valor < 0:
        return 0
    else:
        return procura(1, base, valor)
    
print("RAIZ: ", raiz(8, 3))



def igual(a,b):
    if (a ^ b):
        return False
    return True

print("IGUAL: ", igual(3, 5))

def diferente(a,b):
    if (a ^ b):
        return True
    return False

print("DIFERENTE: ", diferente(3, 5))

def valorAbsoluto(x):
    return raizQuadrada(multiplicacao(x, x))

print("VALOR ABSOLUTO: ",valorAbsoluto(-10))

def maiorQue(x, y):
    if igual(subtracao(soma(x,y),valorAbsoluto(subtracao(x,y)))>>1,y) and igual(x,y) == False:
        return True
    return False    


print("MAIOR QUE: ", maiorQue(7, 5))

def menorQue(x, y):
    if maiorQue(x, y) == False and igual(x, y) == False:
        return True
    return False

print("MENOR QUE: ", menorQue(5, 5))

def maiorIgual(x, y):
    if maiorQue(x, y) or igual(x, y):
        return True
    return False

print("MAIOR IGUAL: ", maiorIgual(5, 3))

def menorIgual(x, y):
    if menorQue(x, y) or igual(x, y):
        return True
    return False

print("MENOR IGUAL: ", menorIgual(2, 3))