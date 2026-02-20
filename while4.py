a = 1234
even_count = 0
odd_count = 0
while a > 0:
     digit = a % 10
     if digit % 2 == 0:
         even_count += 1
     else:
         odd_count += 1
     a = a // 10
print(even_count)
print(odd_count)


