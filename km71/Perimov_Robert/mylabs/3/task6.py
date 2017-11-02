print("school decided to create 3 new groups and put them in separate classes. Each 2 students requires 1 desk.")
a = int(input("number of students in the first group "))
b = int(input("number of students in the second group "))
c = int(input("number of students in the third group "))
d = a // 2
if (a%2) == 1:
   d += 1
e = b // 2
if (b%2) == 1:
   e += 1
f = c // 2
if (c%2) == 1:
   f += 1
answer = d + e + f
print("number of desks needed: " + str(answer))
