# calculate Digit of Life 

def f(x):
    y=0
    for i in range(len(x)):
        s=int(x[i])
        y=y+s
    return y

x= input('enter you DOB: ')
if len(x) < 2 or len(x)> 8:
    print("invalid input")
else:
    t=f(x)
    x=str(t)
    print(f(x))