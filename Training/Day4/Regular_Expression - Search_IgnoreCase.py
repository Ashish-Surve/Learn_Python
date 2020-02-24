

"""
Match : Search :
    find a pattern at without re compiling. 
Regular_Expression - Match.py
"""

import re
str1="Welcome to PSL"
str2="Welcome to psl"
str3="Welcome to aaaPSLaaa . PSL here."

match_object=re.search(r"PSL",str2,flags=re.IGNORECASE)   #match object
print("Original String: ",str2)
print("MatchObj: ",match_object)


if(match_object!=None):             #if match found
    print("Match is:",match_object.group())
else:
    print("Match not found...")
