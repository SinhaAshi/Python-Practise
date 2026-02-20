n = int(input())
original = n
reverse = 0

while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reversed number:", reverse)

if reverse > original:
    print("Reversed number is greater than the original number")
else:
    print("Reversed number is NOT greater than the original number")