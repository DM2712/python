a = int (input("Enter your First Number: "))
b = int (input("Enter your Second Number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD is:", a)
