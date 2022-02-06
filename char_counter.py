def char_count(string):
    count_upper = 0
    count_lower = 0
    for char in string:
        if 65 <= ord(char) <= 90:
            count_upper += 1
        elif 97 <= ord(char) <= 122:
            count_lower += 1
    return f"There are {count_upper} upper case letters and {count_lower} lower case letters"

