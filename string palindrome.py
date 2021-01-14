# input string in palindrome or not tst here

#type  1
l='txt please'
k=l.lower()
print(k)
lst=[]
for i in k:         
    if i==' ':          # to remove space
        pass
    else:
        lst.append(i)
q=[]
for j in range((len(lst))//2):  
    
    if lst[j]==lst[-(j+1)]:         # compare 1st half str to 2nd half dtr
         q.append(1)
    else:
        print('It\'s not a palindrome')
        break
j=0
for i in q:    
    j+=i    
if j==(len(lst))//2  :
    print('It\'s a palindrome')

#                                OR



#type 2
# text = input("Enter text: ")

# # remove all spaces...
# text = text.replace(' ','')

# # ... and check if the word is equal to reversed itself
# if len(text) > 1 and text.upper() == text[::-1].upper():
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")
