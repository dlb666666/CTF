import re
import math
import requests

digits = [chr(i) for i in range (ord('0'), ord('9')+1)]
uppercase_letters = [chr(i) for i in range (ord('A'), ord('Z')+1)]
lowercase_letters = [chr(i) for i in range (ord('a'), ord('z')+1)]

valid_chars = digits + uppercase_letters + lowercase_letters
mock_password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"

LOWER_BOUND = 0
UPPER_BOUND = len(valid_chars)

def is_equal(guess):
    if re.match("^{}".format(guess), mock_password):
        return True
    return False

def is_less(guess):
    return guess < mock_password

def find_next_correct_char(password):
    lower_bound = LOWER_BOUND
    upper_bound = UPPER_BOUND
    index = int(math.floor(float(lower_bound+upper_bound)/2))
    while True:
        guess = password + valid_chars[index]
        if is_equal(guess):
            return valid_chars[index]
        elif is_less(guess):
            lower_bound = index
            index = int(math.ceil(float(index+upper_bound)/2))
        else:
            upper_bound = index
            index = int(math.floor(float(lower_bound+index)/2))

if __name__ == '__main__':
    password = ""
    for i in range(32):
        c = find_next_correct_char(password)
        password += c
        print("Updated password: %s" % password)
    print("\nFinal password: %s" % password)
