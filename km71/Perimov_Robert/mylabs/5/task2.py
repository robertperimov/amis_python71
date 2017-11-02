numbers = [int(i) for i in input('Enter numbers: ').split()]
n = 0
for i in numbers:
    for j in numbers:
        if i == j:
            n +=1
print('The number of pairs is : ', (k - len(numbers))/2)
