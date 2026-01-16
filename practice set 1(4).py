# o+1 = 1
# 1+1 = 2
# 2+1 = 3
def fibo(n):
        a,b=0,1
        print("Fibonacci series :")
        for i in range(n):
                print(a,end = " ")
                temp=a
                a=a+b
                b=temp

num = int(input("Enter the number of term :"))
fibo(num)
