lst = [5,6,1,2]
if len(lst) % 2 == 0:
    if lst[:2] == lst[-2:]:
        print("Same slice.")
    else:
        print("Different slice.")
else:
    print("The list has an odd number of elements.")