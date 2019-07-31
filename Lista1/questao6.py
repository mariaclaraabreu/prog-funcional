

n = input()
num =1
def  fun (n, num):
    if n==0:
        return 0
    def fun2 (num, it=1):
        if num == it:
            return fun (n-1, num+1)
        if num % it ==0:
            return fun2(num-1, it+1)

print (fun (n,num))
