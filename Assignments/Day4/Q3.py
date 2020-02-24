words = ["abc", "123aaa", "xyz", "ABC" , "123", "ZZZZZ"]


print("List Comprehension")
alpabetical_words =[word for word in words if str(word).isalpha()]
print(alpabetical_words)

import re
print("Regular Expression")

#match_object=re.fullmatch("[a-zA-Z]+",str2.strip())   #match object
nwlt=[word for word in words if re.fullmatch("[a-zA-Z]+",str(word).strip())]
   
print(nwlt)
