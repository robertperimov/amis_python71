#task2
mass = input("Введите элементы списка через пробел - ").split()
a = 0
for k in mass:
    for m in mass:
        if k == m:
            a = a + 1
    a = a - 1
print("кол-во пар - ",a//2)
input()
