#Palindrome
s=input("Enter a string for Palindrome")
s=s.lower()

s1=s[::1]
news=s[::-1]
print(s)

if(s1==news):
    print("is a Palindrome")
else:
    print("is not a Palidrome")

print("=======================================")
