

"""
Match : Method :
    find a pattern at beggining of a string. 
Regular_Expression - Match.py
"""

import re
str1="Welcome to PSL"
str2="PSLWelcome to psl"
str3="Welcome to aaaPSLaaa . PSL here."

patternObj=re.compile("psl")    #pattern already complied

print("Original String: ",str2)
print("PatternObj: ",patternObj)

match_object=patternObj.match(str2)   #match object

if(match_object!=None):             #if match found
    print(match_object)
    print(patternObj.search(str2))
else:
    print("Match not found...")
