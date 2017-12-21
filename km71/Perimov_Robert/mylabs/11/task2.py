def Min(list):
    if len(list) == 1:
        return list[0]
    else:
        return min(Min(list[:-1]), list[-1]) #finding the min element using recursion

print(Min(input("please write a list ").split())) #using the function on users list
