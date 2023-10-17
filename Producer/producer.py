import os
import time
print("Welcome to Producer section")

filep= open("Message1.txt","w")
filep.write("Producer has produced the message. Version 1")
filep.close()
fileptr= open("Message2.txt","w")
fileptr.write("Producer has produced the message. Version 2")
fileptr.close()
time.sleep(10)
print("Producer ended.")



