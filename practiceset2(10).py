pair = (1, 2, 2, 3, 2)
num=int(input("Element:"))
count=0

for i in pair[1:] :
    if i == num :
        count+=1

print(count)