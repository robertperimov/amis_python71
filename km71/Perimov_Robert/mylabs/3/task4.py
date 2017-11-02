print("this program will divide apples between students")
N = int(input("enter the number of students "))
K = int(input("enter the number of apples "))
a = K // N #number of apples that each student got
b = K % N #number of apples that left in the basket
print("each student got " + str(a) + " apple(s)\nyou have " + str(b) + " apple(s) in basket remaining")
