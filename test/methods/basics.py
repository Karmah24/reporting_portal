def digits(n):
    if(n == 0):
        return 0
    i = 1
    while(n//10 > 0):
        i += 1
        n //= 10
    return i
