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
  
    
    
    
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
