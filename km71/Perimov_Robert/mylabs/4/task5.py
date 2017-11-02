first = float(input("enter any number: "))
second = float(input("enter any number: "))
third = float(input("enter any number: "))
if first == second == third:
   answer = 3
elif first == second != third:
   answer = 2
elif first != second == third:
   answer = 2
elif first == third != second:
   answer = 2
else:
   answer = 0
print(answer)
