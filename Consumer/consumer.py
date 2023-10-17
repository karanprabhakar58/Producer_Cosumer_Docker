import os

print("Welcome to Consumer section")
print("File is read from Volume : " + os.getcwd())
files = os.listdir(os.getcwd())
path = os.getcwd() + "/"
for f in files:
    if f.endswith(".txt"):
        print("Contents of File " + f + " is as follows ========= ")
        fileopen = open(path + f,"r")
        for line in fileopen:
            print(line)






