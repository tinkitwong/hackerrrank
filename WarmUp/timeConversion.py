def timeConversion(s):
    hours = ""
    if s[-2] == "P":
        if s[:2] == "12":
            hours += s[:2]
        else:
            hours += str(( int(s[:2]) + 12 ) % 24 )
    else:
        hours += str(int(s[:2]) % 12)
    print(hours)
    if len(hours) == 1 : 
        hours = "0" + hours
    a = hours  + s[2:-2]
    print(a)
    return a

timeConversion("12:45:54PM")