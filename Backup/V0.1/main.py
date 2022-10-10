# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 09:56:57 2022

@author: wilwin
"""

import time
import urllib3
from threading import Timer
import re
import requests
import random


class MyTimer(Timer):
    started_at = None
    def start(self):
        self.started_at = time.time()
        Timer.start(self)
    def elapsed(self):
        return time.time() - self.started_at
    def remaining(self):
        return self.interval - self.elapsed()

def random_number_gen():
    randomlist = random.sample(range(10, 3000), 4)
    print(randomlist)
    return randomlist


def read_command_lists(filename='Time_ordered_program.txt'):
    command=[]
    with open(filename) as f:
        lines =f.read().splitlines()
        for line in lines:
            if re.match("set_command",line, flags=re.I):
                tmp = line[12:].split(" ")
                while("" in tmp) :
                    tmp.remove("")
                tmp[0]=float(tmp[0])
                command.append(tmp)
    return command

def run_command_lists(command):
    threads=[]
    for line in command:
        command_name = line[1]
        if len(line)>=3:
            args = line[2:]
        else:
            args = None
        if command_name in command_dictionary:
            threads.append(MyTimer(line[0], command_dictionary[command_name],args))
        else:
            raise Exception("Method %s not implemented" % command_name)
    for thread in threads:
        thread.start()
    return threads

def update_command_time(command,newcommand,threads):
    stop_threads(threads)
    tmp=[]
    for i in range(len(command)):
        time = newcommand[i][0]
        elapsed = threads[i].elapsed()
        if (time-elapsed>=0):
            newcommand[i][0] = time-elapsed
            tmp.append(newcommand[i])
    command = tmp
    return command

def stop_threads(threads):
    for i in range(len(threads)):
        threads[i].cancel()
    time.sleep(0.1)
    print('ALL THREADS STOPPED')        

def initialization():
    print("0000")

def c_0001():
    print("0001")

def c_0002():
    print("0002")

def c_1003():
    print("1003")
 
def c_1004():
    print("1004")
    
def c_1005():
    print("1005")
    
def c_1006():
    print("1006")
    
def c_1007():
    print("1007")

def c_1008():
    print("1008")

def c_1009():
    print("1009")

def c_1010():
    print("1010")

command_dictionary={'0000': initialization, '0001': c_0001, '0002': c_0002, 
                    '1003': c_1003, '1004': c_1004, '1005': c_1005,
                    '1006': c_1006, '1007': c_1007, '1008': c_1008,
                    '1009': c_1009, '1010': c_1010}

command = read_command_lists()
threads = run_command_lists(command)
time.sleep(10)
update_command_time(command,command,threads)  

