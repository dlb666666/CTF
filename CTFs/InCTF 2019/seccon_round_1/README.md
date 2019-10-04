NOTE: I did not properly document my progress here since I was focussing on speed.

Challenges Solved:
1. Forensics 100 pts: Simply run binwalk to get an image with the flag in it.
2. Web Exploitation 100pts: The flag was in a cookie.
3. Web Exploitation 200pts: Craft an XXE payload to read the contents of the source
   code (process.php) and then you'll find the link to another PHP file, extract the
   source code of that file to find the flag embedded in a comment or something.
   <!DOCTYPE email [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=process.php"> ]>
   NOTE: https://github.com/swisskyrepo/PayloadsAllTheThings is an absolutely beautiful repository.