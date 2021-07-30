def swap_case(s):
    for i in range (len(s)):
        if s[i].isupper():
             return s[i].lower()
        elif s[i].islower():
            return s[i].upper()
        else:
            return s[i]
s=input()
swap_case(s)
print("".join(map(swap_case,s)))
