first_x = int(input('enter first starting coordinate: '))
first_y = int(input('enter second starting coordinate: '))
second_x = int(input('enter first ending coordinate: '))
second_y = int(input('enter first starting coordinate: '))
if first_y > 8 or first_x > 8 or second_y > 8 or second_x > 8:
    answer = 'coordinate should not be > 8'
else:
    a = first_x+first_y
    b = second_x+second_y
    if abs(a-b)==1 or abs(a-b)==3:
        answer = "YES"
    else:
        answer = "NO"

print(answer)

