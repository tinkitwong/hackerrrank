def is_leap(year) -> bool:
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
        
    return leap

year = 2100
print(is_leap(year))