year = int(input('enter any year number: '))
if (year % 400) == 0:
   answer = "leap"
else:
   if (year % 4) == 0:
      if (year % 100) != 0:
         answer = "leap"
      else:
         answer = "common"
   else:
      answer = "common"
print(answer)
