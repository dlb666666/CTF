import requests

for i in range(0, 15):
    response = requests.post("http://natas19.natas.labs.overthewire.org", headers={"Authorization": "Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=="}, data={"username":"admin", "password": "pass"})
    phpsessid = response.headers["Set-Cookie"].split(";")[0].split("=")[1]
    ascii_text = bytearray.fromhex(phpsessid).decode()
    print("{} -> {}".format(phpsessid, ascii_text))
