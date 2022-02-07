def char_count(string):
    count_upper = 0 # create 2 variables counters for upper and lower case letters
    count_lower = 0
    for char in string: # create for loop that will add to counters depending on if upper or lower case
        if 65 <= ord(char) <= 90:
            count_upper += 1
        elif 97 <= ord(char) <= 122:
            count_lower += 1
    return f"There are {count_upper} upper case letters and {count_lower} lower case letters" # print statement that displays total count

