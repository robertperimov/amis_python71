#task5
a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
c = int(input("Enter the first number: "))

if a==b==c:
    answer = 3
elif a==b or a==c or b==c:
    answer = 2
else:
    answer = 0
print(answer)
