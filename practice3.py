def facto(n):
    if n < 0:
        print("Factorial is not defined for negative numbers") 
        return

    result = 1
    for i in range(1,n+1):
        result *= i
    return result   

   
num = int(input("Enter a number to find its factorial: "))
fact = facto(num)       
print("Factorial of", num, "is", fact)
