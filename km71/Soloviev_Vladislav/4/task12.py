#task12
print("Enter width of the chocolate bar")
n = int(input())
print("Enter it's length")
m = int(input())
print("Enter desired number of pieces")
k = int(input())

if (0 < k < m*n) and (k%n==0 or k%m==0):
    print("YES")
else:
    print("NO")
