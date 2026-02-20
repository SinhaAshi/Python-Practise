s = "code9"
last = s[-1]
if last.isdigit():
    print("The last character is a digit.")
elif last.isalpha():
    print("The last character is a letter.")  
else:
    print("The last character is neither a digit nor a letter.")