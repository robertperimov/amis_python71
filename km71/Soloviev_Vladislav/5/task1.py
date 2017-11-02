#task1
list = input()
list = list.split(' ')
petya = int(input())

for i in range(len(list)):
    if petya > int(list[i]):
        position = i+1
        break
else: position= len(list) +1
print(position)
