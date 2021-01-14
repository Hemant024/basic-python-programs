#                           REVERSE STRING


#           case 1
#string="python"
#x = string[::-1]                    # using slicing
#print(x)


#           case 2


#y= "".join(reversed("hey"))         # reversed function only reverse and then give it
#print(y)                            # dataype list or str("") and join them using join method




#           case 3

def reverse_for_loop(s):                # using for loop in function
    s1 = ''
    for c in s:
        s1 = c + s1                   # appending chars in reverse order
    return s1
print(reverse_for_loop("python reverse"))
