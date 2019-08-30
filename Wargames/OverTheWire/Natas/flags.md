# Flags

## URL Format:
http://natas0.natas.labs.overthewire.org

## Passwords:
**natas0:**  natas0  
**natas1:**  gtVrDuiDfck831PqWsLEZy5gyDz1clto  
**natas2:**  ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi  
**natas3:**  sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14  
**natas4:**  Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ  
**natas5:**  iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq  
**natas6:**  aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1  
**natas7:**  7z3hEENjQtflzgnT29q7wAvMNfZdh0i9  
**natas8:**  DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe  
**natas9:**  W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl  
**natas10:** nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu  
**natas11:** U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK  
**natas12:** EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3  
**natas13:** jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY  
**natas14:** Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1  
**natas15:** AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J  
**natas16:** WaIHEacj63wnNIBROHeqi3p9t0m5nhmh  
**natas17:** 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw  

## Brief Explainations:
**0:** http://natas0.natas.labs.overthewire.org  

**0 -> 1:** f12, view the source HTML.  

**1 -> 2:** f12, view the source HTML again.  

**2 -> 3:** `<img src="files/pixel.png">` is a hint that we can directly access  
some files if the webserver is poorly configured, which it is. Go to:  
http://natas2.natas.labs.overthewire.org/files/users.txt  

**3 -> 4**: *If Google can't find the page, then it's probably because there  
is a robots.txt file* which will list endpoints that web crawlers are requested  
to avoid indexing.  

**4 -> 5**: Spoof the `Referer` header and resend.  

**5 -> 6**: Just modify the `loggedin` cookie and set it to 1 (auth is usually  
managed via. cookies). Reload.  

**6 -> 7**: go to http://natas6.natas.labs.overthewire.org/includes/secret.inc  
and view the source to get secret = `FOEIUWGHFEEUHOFUOIU`.  

**7 -> 8**: Use the hint from clicking on the home link and then viewing f12.  
then exploit the shitty PHP code (to do a directory traversal attack). Go to  
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8  

**8 -> 9**: Just reverse whatever "encryption" they're doing. Use PHP or Python.  
```
<?php
    $decodedsecret =base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362")));
    print("{$decodedsecret}\n");
?>
```  

**9 -> 10**: It's a direct bash injection vulnerability.  
Just enter something like `; cat /etc/natas_webpass/natas10 #`  

**10 - >11:** Abuse the fact that we can still modify arguments to grep.  
command with arguments used: `grep -e ".\*" -R /etc/natas_webpass #`  

**11 -> 12:** Reverse the bad xor crypto. If a ^ k = b, then a ^ b = k. We know  
both a (plaintext) and b (ciphertext). Note: %3D at the end of a base64 string  
indicates that it's url-encoded; replace it with a "=".  

**12 -> 13:** We're allowed to upload a file of our choice; we can change/spoof  
the file(name) extention via f12.; the file will be stored within the webroot.  
Thus we can upload and execute our own code.  

**13 -> 14:** We're dealing with the same attack as before which is a file  
injection vulnerability but this time, they are using `exif_imagetype` in their  
PHP code, a quick google search shows us that the way this validation works is  
via. magic numbers. So inserting 0XFFD8FFE0 as raw binary at the start of the  
php file (This kinda stuff is common in forensics challenges) will trick tools  
like `file` in Linux and `exif_imagetype` in PHP into believing that we uploaded  
a `JPEG image data` type file. We can do this with Ghex. Spoof the filename via.  
f12 just like last time and upload a PHP payload like:  
```
<?php $results = exec('cat /etc/natas_webpass/natas14'); print($results); ?>
```
So the complete file in hex (with the magic numbers prepended) would be:  
```
����<?php $results = exec('cat /etc/natas_webpass/natas14'); print($results);?>
```

**14 -> 15:** A very straight-forward and simple SQL injection attack. Fun fact,  
for some reason -- does not work for commenting but # does.  
Username: " or 1; #  
password: lite  

**15 -> 16:** This is also an SQLi attack, but unlike last time, we can't  
directly bypass any authentication. So this is full out blind SQLi (officially  
speaking the previous challenge was also blind SQLi, but just not to the same  
degree). For finding the password, we'll need to write a script (for the first  
time in Natas). We can follow a technique similar to what was demonstrated by  
LiveOverflow in https://www.youtube.com/watch?v=za_9hrq-ZuA. The user natas16  
exists so now we just need to intelligently brute force the password using > or  
<.  
Gotchas:  
    - the like clause in SQL is case insensitive, so we need to fix that.  
      Use something like COLLATE or BINARY.  

**16 -> 17:** *I needed a hint, so I got a pretty good one from
https://www.zigosec.com/2018/09/22/overthewire-natas-16/: they don't block
$,(,) so we can exploit command substitution :).* We can't modify files on
the system otherwise I could have overwritten dictionary.txt and just queried
that with a "." grep command. `^$(cut -c1-3 /etc/natas_webpass/natas16)` is
nice but there's the issue of case insensitivity from grep and numbers aren't
supported.

I looked at the solution from the above blog only to find that the author was
guessing the password character by character. Was kinda disappointed since I
was expecting something else (I particularly avoided this method since I
thought that it felt pretty inefficient and that there was a more impressive
hack). Every one seems to have used to same approach, so I stopped cribbing
and just made a script. It took FOREVER to run off of my network.

With this challenge, I learnt that I need to use scripts more and if a method
works, I should just use it even if it's slow. Hackers are patient.
