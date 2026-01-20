list = [10,5,15,8,20]
largest = list[0]
second = 0

for i in list:
    if i>list[0]:
        second = largest
        largest = i
    elif i != largest & i>largest: 
        second = i

        
print(second)
