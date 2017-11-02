students_height = [int(i) for i in input('Enter height of people: ').split()]
peter_height = int(input('Enter Peters height: '))
position = 1
for i in students_height:
    if i >= peter_height:
        position +=1
print('Peters position is:',position)
