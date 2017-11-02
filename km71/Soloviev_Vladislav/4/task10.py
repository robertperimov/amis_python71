#task10
print("Enter primary coordinates of the Queen")
x1 = int(input())
y1 = int(input())
print("Enter final coordinates of the Queen")
x2 = int(input())
y2 = int(input())

if 0<x1<9 and 0<x2<9 and 0<y1<9 and 0<y2<9:
    if abs(x1-x2)==abs(y1-y2) or x1==x2 or y1==y2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
