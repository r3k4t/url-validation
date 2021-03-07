import os
import sys
import validators

os.system("clear")

print(chr(27)+"[33m")

print("==========================================")
print("              Url Validation              ")
print("==========================================")
print("      Author : Rahat Khan Tusar(rkt)      ")
print("      Github : https://github.com/r3k4t   ")
print("==========================================")

url = input("Enter a url:")
if not validators.url(url):
  print(chr(27)+"[31m")
  print ("url is not  valid.")
else :
  print(chr(27)+"[32m")
  print ("url is valid.")
 
