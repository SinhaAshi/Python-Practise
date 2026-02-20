n = 3456
while n >= 10:
    temp=n
    s = 0
    while temp!= 0:
        s += temp % 10
        temp //= 10
    n = s
print(n)