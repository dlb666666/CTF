### Main Level 1:  
username: in  
password: out  
Similar to Natas 0 and 1, the username and password are in the source code.  
You have to use the find function (ctrl+f) to find it though since it's in  
a weird place.  

### Main Level 2:  
username: resu  
password: ssap  
This was a pretty stupid extension of the previous challenge. Instead of
being in a comment, the username/password are now in hidden spans in the
formset itself.

### Main Level 3:  
username: heaven  
password: hell  
The username and password were checked in the JavaScript. So just read the JS.  

### Main Level 4:
username: 999  
password: 911  
A comment in the HTML source code indirectly suggests performing a directory  
traversal attack. Credentials are stored in an xml file.  
https://www.hackthis.co.uk/levels/extras/ssap.xml  
`<user><name>Admin</name><username>999</username><password>911</password></user>`  

### Main Level 5:  
password: 9286jas  
Again, just inspect the JS.

### Main Level 6:  
Just inspect element > change one of the options to "Ronald" and select it.

### Main Level 7:
username: 48w3756
password: u3qh458
The hint says something about search engines, so just like one of the first  
Natas challenges, look for the site's robots.txt file.  

### Main Level 8:
username: B00B
password: FEED
https://www.hackthis.co.uk/levels/extras/secret.txt
1011 0000 0000 1011
1111 1110 1110 1101
Hint says use base-16

### Main Level 9:
Go to the forgot credentials page. Then change the hidden email2 parameter to
your email, and then enter your email into the form and hit enter. Somehow
this a hack.... some shitty credentials reminder system this must be...

### Main Level 10:
This was kinda harder. I felt like this was a hashed password but I didn't  
know which algorithm was used to get it. I also didn't want to try using a  
dictionary and then discovering which word hashed to the given code. *So I   
started thinking about rainbow tables and realized that it might be too   
complex for this problem. Then I looked at the forums and someone suggested  
directly googling the hashed value.* I later found that rainbow tables were
the right way to go and that they were using sha-256.  
encrypted password available at: https://www.hackthis.co.uk/levels/extras/level10pass.txt
69bfe1e6e44821df7f8a0927bd7e61ef208fdb25deaa4353450bc3fb904abd52:f1abe1b083d12d181ae136cfc75b8d18a8ecb43ac4e9d1a36d6a9c75b6016b61
