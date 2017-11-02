#(x1 = 1; x2 = 1) - black tile
x1 = int(input("enter x1: "))
y1 = int(input("enter y1: "))
x2 = int(input("enter x2: "))
y2 = int(input("enter y2: "))

if (x1 % 2) == (y1 % 2) == 1:
   tile_1 = 'black'
elif (x1 % 2) == (y1 % 2) == 0:
   tile_1 = 'white'
elif (x1 % 2) != (y1 % 2):
   tile_1 = 'white'

if (x2 % 2) == (y2 % 2) == 1:
   tile_2 = 'black'
elif (x2 % 2) == (y2 % 2) == 0:
   tile_2 = 'white'
elif (x2 % 2) != (y2 % 2):
   tile_2 = 'white'

if tile_1 == tile_2:
   answer = 'yes'
else:
   answer = 'no'


print(answer)
