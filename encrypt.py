# Your task is to write a program which:

# asks the user for one line of text to encrypt;
# asks the user for a shift value (an integer number from the range 1..25 - 
# note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
# prints out the encoded text.

string =input('enter value here: ')
value = int(input('enter shift value from range 1 to 25: '))
lst = []
finalstrg=''
for i in string:
    if i.isalpha():
        if i.upper()==i:
            asc=ord(i)            
            if asc+value>90:#                
                l=chr((value-(90-asc))+64)
                finalstrg+=l

            else:                
                l=chr(asc+value)
                finalstrg+=l
        else:
            asc=ord(i)            
            if asc+value>122:              
                l=chr((value-(122-asc))+96)
                finalstrg+=l
            else:
                l=chr(asc+value)
                finalstrg+=l
    else:
        finalstrg+=i
print(finalstrg)

#                                    or in list o/p

string =input('enter value here: ')
value = int(input('enter shift value from range 1 to 25: '))
lst = []
for i in string:
    if i.isalpha():
        if i.upper()==i:
            asc=ord(i)            
            if asc+value>90:#                
                lst.append(chr((value-(90-asc))+64))
            else:                
                lst.append(chr(asc+value))
        else:
            asc=ord(i)            
            if asc+value>122:              
                lst.append(chr((value-(122-asc))+96))
            else:
                lst.append(chr(asc+value))
    else:
        lst.append(i)
print(lst)
