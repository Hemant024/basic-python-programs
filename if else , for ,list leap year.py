#if-elis-else and using list with for loop
#gregorian calander (find out leap  year)



list = [1900, 2016,1987,2000]
for i in range(len(list)):
    year = list[i]

    if year % 4 != 0:
        print("False")
    elif year % 100 != 0:
        print("True")
    elif year % 400 != 0:
        print("False")
    else:
        print("True")
