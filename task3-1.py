def first_unique_char(s: str) -> str:
    for i in range(len(s)):
        is_unique = True
       
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                is_unique = False
                break
        if is_unique:
            return s[i]
    
   
    return "None"

# Input
s = input("Enter a string: ")

# Output
print("First non-repeating character:", first_unique_char(s))
