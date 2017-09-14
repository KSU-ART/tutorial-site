year = int(raw_input())
print is_leap(year)

def is_leap(year):
    leap = False
    
    if (year % 4 == 0):
        leap = True;
        if (year % 100):
            leap = False;
            if (year % 400):
                leap = True;
    
    return leap