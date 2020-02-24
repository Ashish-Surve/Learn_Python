Steps:

1. Install mysql
	set username 'root'
	set password 'root'
	create a database 'test'
	
2. Install python 2.7 
	location :'c:/python27/python' for shebang to work
	install using pip MySQLdb
	install cgi, cgitb if not installed 
		
3. Install apache 2.2 preferablly
		
		
4. 	Copy htdocs dir in apache folder and replace
	e.g. (C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs)
	Copy cgi-bin dir in apache folder and replace
	e.g. (C:\Program Files (x86)\Apache Software Foundation\Apache2.2\cgi-bin)
	
5. Now start the server.
6. Enter localhost in the addressbar
7. Enter Name as Ashish,Sunny, Nikhil, Ayush\
	Their respective details will be shown
8. SQL INJECTION
	Enter Injection Value *Ashish' OR 'A'='A* without *
9. All the records in the database are shown. this is the sql injection
