

"""
Match : Search :
    Search any single character 
Regular_Expression - Match.py

============================================
    ^ - serach at start
    $ - search at end
    . - search single char except "\n"
        re.DOTALL can find "\n" as well
============================================
"""

import re
str1="Welcome to PSL"
str2="PSlWelcome to psl"

match_object=re.search(r"..[e,l]",str2,re.DOTALL)   #match object
print("Original String: ",str2)
print("MatchObj: ",match_object)


if(match_object!=None):             #if match found
    print("Match is:",match_object.group())
else:
    print("Match not found...")
