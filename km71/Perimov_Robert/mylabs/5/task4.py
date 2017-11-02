n = int(input('enter number of kegels: '))
k = int(input('enter number of balls: '))
a = []
for i in range(1, n+1 ):
    a.append(str('I'))
for p in range(k):
  b = []
  for i in range(0,1):
    b.append(int(input('enter first hitten kegle: ')))
    b.append(int(input('enter last hitten kegle: ')))
    for j in range(b[0]-1,b[1]):
        a[j]=str('.')

print(''.join( str(n) for n in a))

