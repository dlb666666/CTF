### Basics+ Level 1:  
username: paint  
password: rules  
We're given a "text" file and need to extract a username and password from it.  
At first I tried running strings on it -> No good.  
Then I tried to manually analyze the binary content with ghex:  
    - Tried to see if I could identify any magic numbers -> Nope.  
    - Tried to find a pattern regarding number of repetitions -> Wasted time.  
Then tried to see if there were any hidden/extended file attributes -> Nope.  
Started to think that there **must** be some kind of filetype trick here because  
the first few bytes really seemed special. Remembered John Hammond mentioning  
something about binwalk so I tried it out on this:  
`PC bitmap, Windows 3.x format,, 213 x 108 x 24`  
Thus changed the file extension to .bmp and voila: an image with the credentials.  

### Basics+ Level2:  
This challenge was kinda weird. Basically they wanted us to spoof the User-Agent  
header and set it to "secure_user_agent".

### Basics+ Level3:  
The hint lets us know that we are dealing with Flash, it also tells us that the  
the "flash file" has to contact the same HTTPS endpoints anything else. So poking  
around the network tab of developer tools, we find b3.swf. We can decompile it  
using ffdec (FOSS, available on GitHub, can be run as a jar). There we find the  
endpoint being contacted and the payload being sent. So just send the right number  
of points to move on.  

### Basics+ Level4:  
username: james  
password: chocolate  
The image metadata says that it was taken by a person named "james" and there is a  
comment "i like chocolate". I thought that these were the username and password but  
they didn't work. I also found b5.jpg from the next challenge by accident and tried  
using the credentials that I found from that challenge. *Later I read a hint from the  
forums that asked: "what does he like"* -> facepalm.  

### Basics+ Level5:  
username: admin  
password: safe  
Running strings on the image file shows us the credentials in plaintext at the end of  
the file. Now we're getting into "forensics" style challenges. We could have also run  
binwalk on the image file to get the text-file embedded in it.  

### Basics+ Level6:  
IP Address: 85.159.213.101  
Company hosting server: Linode
X-B6-Key header: Lajklsb#!"3jlak  
Do nslookup to get the IP.  
Go to https://www.name.com/whois-lookup/85.159.213.101 to get information about the  
company doing the hosting.  
Go to gmail and hit "show original" for any email sent by hackthis to find the  
X-B6-Key header.  

### Basics+ Level7:  

