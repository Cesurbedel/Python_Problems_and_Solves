def is_leap(year):
    leap = False
    
    # Check if the year meets the leap year conditions
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
                
    return leap

# Example usage:
# year = int(input("Enter a year: "))
# print(is_leap(year))


year = int(input())
print(is_leap(year))