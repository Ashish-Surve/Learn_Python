

"""
Match : Search :
    find a pattern at without re compiling. 
Regular_Expression - Match.py
"""

import re
str1="Welcome to PSL"
str2="PSLWelcome to psl"
str3="Welcome to aaaPSLaaa . PSL here."

match_object=re.search("PSL",str3)   #match object
print("Original String: ",str3)
print("MatchObj: ",match_object)


if(match_object!=None):             #if match found
    print(match_object)
else:
    print("Match not found...")
