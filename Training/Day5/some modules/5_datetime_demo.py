

#5_datetime_demo.py

from datetime import date  
now = date.today()
print ("Today is = ",now)    #Today is =  2020-01-02

Ord1 = now.toordinal()+3   #dyas incremented by 3     
print (date.fromordinal(Ord1).strftime('%m-%d-%y'))     #01-05-20

print ("-------------------------------------------------------------")
# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print (age.days)

print ("-------------------------------------------------------------")
print (dir(date))
