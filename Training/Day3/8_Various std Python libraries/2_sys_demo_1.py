

"""sys. stdin  stdout stderr"""
#2_sys_demo_1.py
import sys
#fh = open("hello.txt","w")
#fh.write("Hello")

sys.stdout = open("hello.txt","w")  #re directing sys.stdout (screen/console) to a file now
print ("AAAAAAAAAAAAAAAAaa")  #instead of printing on console, it will print inside file hello.txt 
sys.stdout.close()


























'''
stdin
stdout
stderr
#!/usr/bin/env python

 f1 = open("hello.txt","w")
 f1.write("Hello !!!")
'''
