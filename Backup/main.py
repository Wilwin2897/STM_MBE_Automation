# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 09:56:57 2022

@author: wilwin
"""

import time
import urllib3
from threading import Timer
start = time.time()

def read_command_lists(filename='Time_ordered_program.py'):
    with open(filename) as f:
        lines = f.readlines()
        print(lines)

read_command_lists()
def my_job():
    print('text')
    
end = time.time()
t = Timer(10.0, my_job)
t.cancel()
t = Timer(1.0, my_job)
t.start()

print(end - start)
#print("PROGRAM TERMINATION\n")  
#S.cancel()