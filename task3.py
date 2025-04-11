def first_unique_char(s: str) -> str:
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char

    return "None"

s = input("Enter a string: ")
print("First non-repeating character:", first_unique_char(s))
