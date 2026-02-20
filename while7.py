num = 1223334444
digit = 4
count = 0
while num > 0:
    if num % 10 == digit:
        count += 1
    num //= 10
print(count)