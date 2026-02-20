s = "hello"
if len(s)>=5:
    mid = len(s) // 2
    if s[mid].lower() in 'aeiou':
        print("The middle character is a vowel.")
    else:        
        print("The middle character is not a vowel.")
else:  
    print("The string is too short .")