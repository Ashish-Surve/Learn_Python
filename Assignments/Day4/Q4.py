

"""
Match : Search :
    Accept word from kb
    Validate it containing only alphabetical content
    
Regular_Expression - Match.py

============================================
    ^    -  search at start
    $    -  search at end
    .    -  search single char except "\n"
            re.DOTALL can find "\n" as well
    |    -  o | e | x find o or e or x
    [ ]     [oex] find o or e or x
    *    -  search 0 or more occurances
    +    -  search 1 or more occurances
    ?    -  search 0 or 1 occurances
    { }  -  search multiple occurances
            {num}     - exactly num times
            {min,max} - bw min and max
            {min,}    - bw min and infinity
    ( )  -  (xy)+ finds xy 1 or more times
============================================

r"[A-Z][a-z]+            -> find Title case words
r"[^A-Za-z]              -> find all except given re
r"[.$]"                  -> find . or $ in string
r"[A-Z]{3}               -> find 3 alphabets
r[a-zA-Z0-9_]    or  \w  -> find one of digit/alpha
r[^a-zA-Z0-9_]   or  \W  -> Non Alphanumeric char
[\n\t\r\f]       or  \s  -> white space
[0-9]            or  \d  -> digits
r"^[$][0-9]+[.][0-9]{2}" -> only values in $

============================================
"""

import re

str2=input("No:")
match_object=re.fullmatch(r"\$\d+\.\d{2}",str2)   #match object
print("Original String: ",str2)
#print("MatchObj: ",match_object)


if(match_object!=None):             #if match found
    print("Valid...")
else:
    print("Not Valid...")
