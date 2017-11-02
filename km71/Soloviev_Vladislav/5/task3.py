#task3
mass = input("Введите элементы списка через пробел - ").split()
print("Уникальные элементы списка:")
for k in range(len(mass)):
    if mass.count(mass[k]) == 1:
        print(mass[k], " ")
input()
