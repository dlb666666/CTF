### Level 1:
The most basic form of SQLi, trying to use something like ' OR 1=1; --
works. If you made a mistake, the exact query would have been revealed
in an error message.

### Level 2:
Another simple case of SQLi (not blind) where the SQL injection was
happening in the query for filtering users when viewing them (a GET
parameter). See attack.py for a simple exfiltration script.

To find out which user to attack, a bit of guess work reveals that
there is a field called ADMIN. So using that and a qucik manual query
we find out that "bellamond" was the admin.
