def remove_exckanation_marks(s,n):
    result = ''
    exclamation_count = 0
    for char in s:
        if char == '!' and exclamation_count < n:
            exclamation_count += 1
        else:
            result += char
    return result