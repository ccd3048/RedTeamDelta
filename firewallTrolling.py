#!/usr/bin/python3
'''
@author ccd3048
This is my firewall rule adding script which allows us access through the linux firewalls every 50 seconds
this is to be run only on the linux boxes and is incredibly simple yet effective.
'''
import os
import time

def main():
    commands = [
        "firewall-cmd --add-source --permanent 10.170.0.0 255.255.255.0",
        "firewall-cmd --reload"]
    
    while True():
        for command in commands:
            os.popen(command)
        time.sleep(50)