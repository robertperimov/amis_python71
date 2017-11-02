a = []
for i in range(8):
    a.append(int(input('enter first coordinate: ')))
    a.append(int(input('enter second coogdinate: ')))
for j in a:
        k = (a[j] + a[j+2])%2
        l = (a[j+1] + a[j+3])%2
        if a[j] == a[j+2] or a[j+1] == a[j+3] \
              or (k == l and a[j+1] == a[j] and a[j+3] == a[j+2]) or (
              k == l and a[j] + a[j+1] == a[j+2] + a[j+3]) or (
              abs((a[j+1] + a[j]) - (a[j+3] + a[j+2])) % 2 == k):
              answer = 'YES'
        else:
          answer = 'NO'
print(answer)

