n = int(input('enter n number: '))
m = int(input('enter m number: '))
k = int(input('enter k number: '))
a = n%2
b = m%2
if (a == 0 and k == (n/2)*m) or (b == 0 and k == (m/2)*n):
    answer = 'YES'
else:
    answer = 'NO'

print(answer)

