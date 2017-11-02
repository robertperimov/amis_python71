#task4
N = int(input("Введите количество кеглей - "))
mass = ["I"]*N
K = int(input("Введите количество бросков - "))
for i in range (K):
    li = int(input("введите номер первой сбитой кегли - "))
    ri = int(input("введите номер последней сбитой кегли - "))
    for k in range(li, ri+1):
        mass[k-1] = "."
for m in range(len(mass)):
    print(mass[m], end = "")
input()
