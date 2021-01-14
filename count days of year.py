def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def daysInMonth(year, month):
    if month == 2:
        if isYearLeap(year)== True:
            if month == 2:
                return 29
        else :
            if month == 2:
                return 28
    else:
        if month in [4,6,9,11]:
            return 30
        elif month in [1,3,5,7,8,10,12]:
            return 31
        else:
            None
  
def dayOfYear(year, month, day):
    if year < 1582:
        return None
    if 1 > month or month > 12:
        return None
    if 1 > day or day > 31:
        return None


    y = 0
    for i in range(1,month):
        x= daysInMonth(year,i)
        y+=x
    return y + day

if dayOfYear(2000, 12, 31) == 366:
    print("Ok")
else:
    print("failed")

    
if dayOfYear(2016, 12, 31) == 366:
     print("Ok")
else:
    print("failed")

    
if dayOfYear(2001, 12, 31) == 365:
     print("Ok")
else:
    print("failed")

