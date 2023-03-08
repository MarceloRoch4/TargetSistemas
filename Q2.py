import math

fib = []
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))
    
def percorreVetor(i, num, fib = []):
    for i in range(1, num+1):
        fib.append(fibo(i))
        print(fib)
        if fib[-1] == num:
            break
    

num = int(input("Digite um numero: "))


num1 = (5 * (num*num)) + 4
num2 = (5 * (num*num)) - 4


if (math.sqrt(num1) // 1) == math.sqrt(num1) :
    i = 0
    percorreVetor(i, num, fib)
    
    print("-----------------------------")
    print(f"{num} Pertence a fibonacci!")
    print("-----------------------------")
elif (math.sqrt(num2) // 1) == math.sqrt(num2):
    i = 0
    percorreVetor(i, num, fib)

    print("-----------------------------")
    print(f"{num} Pertence a fibonacci!")
    print("-----------------------------")
else:
    print(f"{num} NÃO pertence a fibonacci!")






    


