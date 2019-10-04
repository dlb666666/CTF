# Flags  

## Enter Space-Time Coordinates:
Just run the strings command on the given binary to find the flag embedded in
plaintext.  
**flag:** CTF{welcome_to_googlectf}

## Ad:
https://www.youtube.com/watch?v=QzFuwljOj8Y  
Pause the video at around 16.5 seconds and use 0.25x speed to find the flag.  
**flag**: CTF{9e796ca74932912c216a1cd00c25c84fae00e139}

## Satellite:
Open wireshark and begin capturing packets (the hint for this comes from the
google drive document link we get after the connection). Now using `init_sat`,
connect to the osmium satellite. Dig through the packets to find that the
password is in one of the TCP packets as plaintext, here's the hexdump:  
```
0000   55 73 65 72 6e 61 6d 65 3a 20 62 72 65 77 74 6f
0010   6f 74 20 70 61 73 73 77 6f 72 64 3a 20 43 54 46
0020   7b 34 65 66 63 63 37 32 30 39 30 61 66 32 38 66
0030   64 33 33 61 32 31 31 38 39 38 35 35 34 31 66 39
0040   32 65 37 39 33 34 37 37 66 7d 09 31 36 36 2e 30
0050   30 20 49 53 2d 31 39 20 32 30 31 39 2f 30 35 2f
0060   30 39 20 30 30 3a 30 30 3a 30 30 09 53 77 61 74
0070   68 20 36 34 30 6b 6d 09 52 65 76 69 73 69 74 20
0080   63 61 70 61 63 69 74 79 20 74 77 69 63 65 20 64
0090   61 69 6c 79 2c 20 61 6e 79 77 68 65 72 65 20 52
00a0   65 73 6f 6c 75 74 69 6f 6e 20 70 61 6e 63 68 72
00b0   6f 6d 61 74 69 63 3a 20 33 30 63 6d 20 6d 75 6c
00c0   74 69 73 70 65 63 74 72 61 6c 3a 20 31 2e 32 6d
00d0   09 44 61 69 6c 79 20 61 63 71 75 69 73 69 74 69
00e0   6f 6e 20 63 61 70 61 63 69 74 79 3a 20 32 32 30
00f0   2c 30 30 30 6b 6d c2 b2 09 52 65 6d 61 69 6e 69
0100   6e 67 20 63 6f 6e 66 69 67 20 64 61 74 61 20 77
0110   72 69 74 74 65 6e 20 74 6f 3a 20 68 74 74 70 73
0120   3a 2f 2f 64 6f 63 73 2e 67 6f 6f 67 6c 65 2e 63
0130   6f 6d 2f 64 6f 63 75 6d 65 6e 74 2f 64 2f 31 34
0140   65 59 50 6c 75 44 5f 70 69 33 38 32 34 47 41 46
0150   61 6e 53 32 39 74 57 64 54 63 4b 78 50 5f 58 55
0160   78 78 37 65 33 30 33 2d 33 45 0a
```  
**flag:** CTF{4efcc72090af28fd33a2118985541f92e793477f}

## Work Computer:  
**nc readme.ctfcompetition.com 1337**  
Then we find that we are given a shell with restricted vulnerabilities
and in the directory we arrive at there is are two files README.flag and
ORME.flag. Doing ls /etc/bin and /bin shows us which executables we have,
cat and less aren't there. But man page after man page we'll find a command
that help us. *Use fold or some of the other executables to get the contents
of README.flag*  
 **flag:** CTF{4ll_D474_5h4ll_B3_Fr33}

## Home Computer:
We are given a .ntfs file. Mount it. Poking around we find a hint in the
folder /Users/Family/Documents/credentials.txt about extra attributes. Use
getfattr to read the attributes. We find that credentials.txt has a user.FILE0
key and can't see the value *(that's because it's raw binary data). So we
extract this by running getfattr --values-only* and redirect the output to a
.jpg file which we can then open to get the flag.  
**flag:** CTF{congratsyoufoundmycreds}
