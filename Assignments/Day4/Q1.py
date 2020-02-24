try:
    f=open("emails.txt","r")
except(IOError):
    print("File Handling error")

import re

for str2 in f:
    match_object=re.fullmatch('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',str2.strip())   #match object
    print("Email Address: ",str2.strip(),end=" : ")
    #print("MatchObj: ",match_object)


    if(match_object!=None):             #if match found
        print("Valid...")
    else:
        print("Not Valid...")

