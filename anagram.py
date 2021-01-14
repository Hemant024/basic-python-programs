# t1 and t2 anre anagram or not test here

# type 1
def check(t1,t2):  
    l=0
    for i in t1:
        if i in t2:
            l+=1
        if i not in t2:
            print("Not anagram")
            break
    if l==len(t1):
        print("Anagrams")
t1 = list((input('enter 1: ')).lower())
t2 = list((input('enter 2: ')).lower())
check(t1,t2)

#           OR

#type 2

# function to check if two strings are 
# anagram or not  
def check(s1, s2): 
      
    # the sorted strings are checked  
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")          
          
# driver code   
s1 ="Listen".lower()
s2 ="silent".lower()
check(s1,s2)

