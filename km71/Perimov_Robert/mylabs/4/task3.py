first_number = float(input("Enter first_number: "))
second_number = float(input("Enter second_number: "))
third_number = float(input("Enter third_number: "))
if first_number > second_number > third_number:
   answer = (str(third_number) + ' is the smallest number')
elif first_number > second_number < third_number:
   answer = (str(second_number) + ' is the smallest number')
elif first_number < second_number < third_number:
   answer = (str(first_number) + ' is the smallest number')
elif first_number == second_number < third_number:
   answer = (str(second_number) + ' and ' + str(first_number) + ' are the smallest numbers')
elif first_number == second_number > third_number:
   answer = (str(third_number) + ' is the smallest number')
elif first_number > second_number == third_number:
   answer = (str(second_number) + ' and ' + str(third_number) + ' are the smallest numbers')
elif first_number < second_number == third_number:
   answer = (str(first_number) + ' is the smallest number')
elif first_number == third_number < second_number:
   answer = (str(first_number) + ' and ' + str(third_number) + ' are the smallest numbers')
elif first_number == third_number > second_number:
   answer = (str(second_number) + ' is the smallest number')
elif first_number == second_number == third_number:
   answer = ('numbers are equal!')
print(answer)
#rfr ;t z pfljk,fkcz rjulf ltkfk 'ne pflfxe
