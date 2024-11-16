def swap(st):
    vowels = 'aeiou'
    result = ""
    for char in st:
        if char.lower() in vowels:
            result += char.upper()
        else:
            result += char
    return result