import re
str1="Welcome to PSL"
str2="Welcome to psl"
str3="Welcome to aaaPSLaaa . PSL here."

patternObj=re.compile("PSL")    #pattern already complied

print("Original String: ",str1)
print("PatternObj: ",patternObj)

match_object=patternObj.search(str3)    #match object

if(match_object!=None):             #if match found
    print(patternObj.search(str1))
else:
    print("Match not found...")
