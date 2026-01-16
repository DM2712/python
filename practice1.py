ID = int (input("Enter your ID: "))

if ID <= 1 :
    print(" Not a prime number")
else:
    for i in range(2, ID):
        if (ID % i) == 0:
            print(" Non - prime number")
            break
    else:
        print(" Prime number")
