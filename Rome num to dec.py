def value(r):
    if r == 'I':
        return 1
    elif r == 'V':
        return 5
    elif r == 'X':
        return 10
    elif r == 'L':
        return 50
    elif r == 'C':
        return 100
    elif r == 'D':
        return 500
    elif r == 'M':
        return 1000
    else:
        return -1

def roman_to_decimal(roman_str):
    res = 0
    i = 0
    while i < len(roman_str):
        s1 = value(roman_str[i])
        if i + 1 < len(roman_str):
            s2 = value(roman_str[i + 1])
            if s1 >= s2:
                res += s1
                i += 1
            else:
                res += s2 - s1
                i += 2
        else:
            res += s1
            i += 1
    return res

# Example usage
user_input = input("Enter a Roman numeral: ")
decimal_value = roman_to_decimal(user_input.upper())
print(f"Decimal value of {user_input} is {decimal_value}")
