# Tested 2015-01-15 23:19:51

def no_teen_sum(a, b, c):
    sum = 0
    for x in a,b,c:
        sum = sum + fix_teen(x)
return sum

def fix_teen(n):
    if n is 15 or n is 16:
        return n
    if n >= 13 and n <= 19:
        return 0
    return n
