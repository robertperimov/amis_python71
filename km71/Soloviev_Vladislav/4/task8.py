#task8
print("Enter primary coordinates of the Dark Lord")
x1 = int(input())
y1 = int(input())
print("Enter final coordinates of the Dark Lord")
x2 = int(input())
y2 = int(input())

if 0<x1<9 and 0<x2<9 and 0<y1<9 and 0<y2<9:
    if x1-x2>=-1 and x1-x2<=1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
