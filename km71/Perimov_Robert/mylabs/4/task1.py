first_number = input("Enter first_number: ")
second_number = input("Enter second_number: ")
if first_number > second_number:
   answer = (second_number + ' is smaller than ' + first_number)
elif first_number < second_number:
   answer = (first_number + ' is smaller than ' + second_number)
else:
   answer = ('numbers are equal!')
print(answer)
