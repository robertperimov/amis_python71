def Max(list):
    global a
    if len(list) == 1:
        a = list[0]
    else:
        a = max(int(Max(list[:-1])), int(list[-1]))
    return a


def secondMax(list):
        Max(list)
        list.remove(str(a)) #removing the 1st max element
        Max(list) #searching for the 2nd max element
        return(str(a))


print(secondMax(input("please write a list ").split()))

