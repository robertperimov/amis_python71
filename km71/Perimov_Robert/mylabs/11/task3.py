def backward(list):
    if len(list) < 2:
        return list
    else:
        x = len(list)//2
        return backward(list[x:])+backward(list[:x]) #using recursion to reverse the list


print(backward(input("please write a list ").split())) #trying recursion on the users list
