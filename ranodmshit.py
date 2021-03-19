# my code
names = "Joshua"
password = "123"
yes = "Yes"
no = "No"

#code from some random place
from os import system, name 
  
from time import sleep 
  
def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')
#code from some random place 

print("hey what is your name")
user_name = input()
if user_name == names:
    print("Hello, " + user_name)
else:
    print("Invalid Name")
    sleep(1)
    exit()

print("password?")
user_password = input()
if  user_password == password:
    print("Access Granted")
else:
    print("Access Denied")
sleep(1)
clear()

print("Do you want to load?")
load = input()
if load == yes:
    sleep(1)
    clear()
    print("Loading...")
    sleep(2)
else:
    print("Ok, canceling")
    sleep(1)
    exit()
# my code
