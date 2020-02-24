

"""
Match : Search :
    find a pattern at without re compiling at beginning. 
Regular_Expression - Match.py

================================----==========
    ^ - serach at start
    $ - search at end
================================----==========
"""

import re
str1="Welcome to PSL"
str2="PSlWelcome to psl"

match_object=re.search(r"PSL$",str2,re.IGNORECASE)   #match object
print("Original String: ",str2)
print("MatchObj: ",match_object)


if(match_object!=None):             #if match found
    print("Match is:",match_object.group())
else:
    print("Match not found...")
