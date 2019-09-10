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
