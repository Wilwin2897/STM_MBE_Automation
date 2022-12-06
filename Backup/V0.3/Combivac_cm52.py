# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:19:27 2022

@author: wilwin
pip install lakeshore
with static IP address 169.254.125.29 port 7777 for 336
and 169.254.125.30 port 23 for TLC-500
Remember to set your computer IP address to static ip 169.254.125.XXX
"""
import pyvisa as visa
from lakeshore import Model336
my_model_336 = Model336(ip_address='169.254.125.29')
ChannelA_Temp = my_model_336.get_celsius_reading("A")
ChannelB_Temp = my_model_336.get_celsius_reading("B")
ChannelC_Temp = my_model_336.get_celsius_reading("C")
ChannelD_Temp = my_model_336.get_celsius_reading("D")
All_Output = my_model_336.get_all_sensor_reading()

print(ChannelA_Temp,ChannelB_Temp,ChannelB_Temp,ChannelB_Temp)

print(All_Output)
#print(my_model_336.get_sensor_reading("A"))

 
rm = visa.ResourceManager() 
print(rm.list_resources())
#IP Address must follow: 169.254.125.xxx, where the first numbers follow your IP address
dev = 'TCPIP0::169.254.125.30::23::SOCKET'
session = rm.open_resource(dev)
print('\n TLC-500 CryoVac Temperature Controller Loaded!')
session.read_termination = '\n'
session.write_termination = '\n'  
print('IDN:' +str(session.query('*IDN?')))
print('Output:' ,[float(x) for x in session.query('getOutput').split(', ')]) 

session.close()