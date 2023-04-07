def is_leap(year):
    leap = False
    bbb=222
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))