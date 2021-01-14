myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
x=[]
for i in range(len(myList)):
    if i in myList:
        x.append(i)
myList = x[:]
print(myList)
