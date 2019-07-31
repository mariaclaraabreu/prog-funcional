#Escreva uma funcao que receba duas listas numéricas e retorne
# uma única lista com
# os elementos da entrada intercalados
#Ex: f([1,2,3,4, [5,6,7,8])
#saida: [1,5,2,6,3,7,4,8]
#OBS as listas nao precisam ter o mesmo tamanho

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]


def fun (lista1, lista2):
    if lista1 and lista2 == []:
        return []
    if lista1 and lista2 != []:
        print ("entrou")
        return [lista1[0] + lista2[0]]+ fun(lista1[1:], lista2[1:])
    #if lista2 == []:
     #   return [lista1[0]] + fun(lista1[1:], lista2)
    #if lista1 == []:
     #   return [lista2[0]] + fun(lista1, lista2[1:])

print (fun(lista1, lista2))




def interc(lista1, lista2, lista3=[]):
    if lista1 == [] or lista2== []:
        return lista3

    def interc2 (l1, l2, l3):
        if l1 == [] or l2 == []:
            return interc(l1, l2,l3)
        [l1[0]] + l3
        [l2[0]] + l3
        return interc2(l1[1:], l2 [1:],l3)
    
        #return interc2(lista1, lista2, lista3)

listi = [1,2,3]
lis = [5,6]

n = 10

#print ([n] + lis)

#print (interc (lista1, lista2))
