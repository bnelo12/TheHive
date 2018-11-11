#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 19:15:45 2018

TheHive Client Host Script
  ________         __  ___          
 /_  __/ /_  ___  / / / (_)   _____ 
  / / / __ \/ _ \/ /_/ / / | / / _ \ 
 / / / / / /  __/ __  / /| |/ /  __/
/_/ /_/ /_/\___/_/ /_/_/ |___/\___/ 
             monetize your PC 

@author: kyr_n
"""


import urllib.request
import sys
import time
import subprocess

#splash screen
logo = "  ________         __  ___          \n /_  __/ /_  ___  / / / (_)   _____ \n  / / / __ \/ _ \/ /_/ / / | / / _ \ \n / / / / / /  __/ __  / /| |/ /  __/\n/_/ /_/ /_/\___/_/ /_/_/ |___/\___/ \n             monetize your PC       \n" #you what? XD
print(logo)
time.sleep(0.5)


'''-------------------------
    INSTALL/UPDATE PACKAGES
   -------------------------'''


print("[PIP INSTALL FLASK]")
subprocess.call(["pip", "install", "flask"])
print("[PIP INSTALL SOCKETIO]")
subprocess.call(["pip", "install", "socketio"])
print("[PIP INSTALL PYMONGO]")
subprocess.call(["pip", "install", "pymongo"])
print("[PIP INSTALL EVENTLET]")
subprocess.call(["pip", "install", "eventlet"])



'''-----------
    BENCHMARK
   -----------'''

subprocess.call(["clear"])
   
tier = 0
pi = 3.141592

start = time.time() / 60 #divide by 60 to convert to seconds
print("\n[BENCHMARKING]")



'''
The benchmarking here basically works by running an insane amount complexed
maths problems and timing how long it takes the processor to complete them
'''

for i in range(1,1000):
    if i % 13 == 0:
        print("#", end = "", flush = True)
              
    for x in range(1,1000):
        pi * 2**x

    for x in range(1,1000):
        float(x) / pi
            
        for x in range(1,1000):
            float(pi) / x
            
            
                
end = time.time() / 60

duration = end - start

time.sleep(0.5)



'''-------------
    ASSIGN TIER
   -------------'''

if duration <= 1.5:
    tier = 1 #£0.05/min
elif duration <= 2:
    tier = 2 #£0.025/min
elif duration <= 2.5:
    tier = 3 #£0.005/min
else:
    tier = 4 #£0.0005/min


subprocess.call(["clear"])
print(logo)



'''-------
    STATS
   -------'''

print("[Tier " + str(tier) + "]") #what tier plan the machine is on

#get ip in JSON
ip = ""
src = urllib.request.urlopen("https://api.ipify.org/?format=json")
json = src.read().decode()


#extract ip
for letter in json:
    if letter.isdigit() or letter == ".":
        ip += str(letter)

print("IP: " + ip +"\n")
print("Awaiting Connection...")


#100% didn't steal this part off stackoverflow...
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()

loop = True
count = 0

while loop:
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
    count =+ 1
    if count == 3750:
        loop = False
    ### TODO: Set loop to False when connection detected ###



#############################
### TODO: SECURITY ISSUES ###
#############################

# Possible stack overflow / divide by zero exploit if the user changes the system time whilst running the script

# Changing system time during benchmarking could result in a higher tier being achieved
    
# TODO: Implement a way of getting time from an external source? Could effect results based on internet/network speeds...












'''--------
    SOCKET
   --------''

ip = ""
port = 22
max_connections = 10

#get ip in JSON
src = urllib.request.urlopen("https://api.ipify.org/?format=json")
json = src.read().decode()

#extract ip
for letter in json:
    if letter.isdigit() or letter == ".":
        ip += str(letter)


#set up FTPS socket
def FTPS():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), port))
    serversocket.listen(max_connections)
        
    ''
        Get system OS and gain root access if Mac
    ''
    if (os.name == "posix"):
        if os.access('/root', os.R_OK|os.X_OK):
            os.chdir('/root')
            FTPS()
    else:
        FTPS()        

print("FTPS SOCKET SET UP\nHOST IP "+ip+"\nPORT "+str(port)+"\nMAX " + str(max_connections) + " CONNECTIONS\n\nReturn to start")

'''