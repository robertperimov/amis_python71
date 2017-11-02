#task7
print("Enter coordinates of the first square")
x1 = int(input())
y1 = int(input())
print("Enter coordinates of the second square")
x2 = int(input())
y2 = int(input())

if 0<x1<9 and 0<x2<9 and 0<y1<9 and 0<y2<9:
    if ((x1%2!=0 and y1%2!=0) or (x1%2==0 and y1%2==0)) and ((x2%2!=0 and y2%2!=0) or (x2%2==0 and y2%2==0)) or ((x1%2!=0 and y1%2==0) or (x1%2==0 and y1%2!=0)) and ((x2%2!=0 and y2%2==0) or (x2%2==0 and y2%2!=0)):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
