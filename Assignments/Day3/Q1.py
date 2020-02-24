from FileReadModule import Read as rd
import os

if(__name__=="__main__"):
    fname=os.path.abspath("country.txt")
    try:
        print(rd.ReadfromFile(fname))
    except(FileNotFoundError):
        print("File Not Found")
    except(Exception):
        print("Error Occured...")
    
    
