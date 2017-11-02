numbers = [int(i) for i in input('Enter numbers: ').split()]
for i in numbers:
    k = numbers.count(i)
    if k == 1:
        print(i, end=' ')
