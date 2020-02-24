#!c:/python27/python

# Import modules for CGI handling 
import cgi, cgitb 

import MySQLdb
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')

#first_name="'Ashish' OR 1 = 1"
#first_name="Ashish' OR 1 = 1 or 'A'='A"

#SQL INJECTION VALUE       Ashish' OR 1 = 1 or 'A'='A

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Displaying Details Shoonya</title>"
print "</head>"
print "<body>"

#connect
db = MySQLdb.connect("localhost","root","root","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE \
       WHERE FIRST_NAME = '%s'" % (first_name)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   if(results==None):
       print "No records found."
       exit(0)
   #print "%s" % (results)
                                 #Business LOGIC    
   print "Record Details--"    
   for row in results:
      fname = row[0]
      lname = row[1]
      passwordd=row[2]
      age = row[3]
      sex = row[4]
      income = row[5]
      # Now print fetched result
      print "<h2>Name: %s %s Age: %d Gender: %s Income: %d</h2>" % (fname, lname,age,sex,income)
      
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()


print "</body>"
print "</html>"
