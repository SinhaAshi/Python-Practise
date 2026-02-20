lst = [4,3,2,1]
mid = len(lst) // 2
first_half = sum(lst[:mid])
second_half = sum(lst[mid:]) 
if first_half > second_half:
    print("first half greater")
elif first_half < second_half:
    print("second half greater")
else:
    print("Both halves have the same sum.")