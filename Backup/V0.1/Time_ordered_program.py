#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 23:50:09 2022

@author: wilwin
"""
#PROGRAMMED ACTION LISTS
#################################################
#0000-0999 : System and program related checks
#################################################
# 0000 : Initialization
# 0001 : System status 
# 0002 : Ethernet communication check

#################################################
#1000-1999 : Data inputs related commands
#################################################
# 1002 : Print out the effusion cells temperatures (All)
# 1003-1006 : Print out the effusion cells temperatures A-D
# 1007 : Print out the pressures (All)
# 1008 : Print out the beam flux monitor
# 1009 : Print out the HVPS voltages (V) and current (I)
# 1010 : Print out the e-beam heater voltages (V) and current (I)

#################################################
#2000-2999 : Data inputs related commands
#################################################
# 2001_90 : preset the opening angle of shutter A as 90
# 2002_90 : preset the opening angle of shutter B as 90
# 2003_-180 : preset the opening angle of shutter C as -180
# 2004_0 : preset the opening angle of shutter B as 60
# 2005 : preset all opening angle to zero
# 2006 : Send EXECUTE command to the shutter control unit (SCU) 

#################################################
#3000-3999 : Eurotherm controller related commands
#################################################
# 3001 : Increase the temperature of Eurotherm 3408 by 1% (A)
# 3002 : Decrease the temperature of Eurotherm 3408 by -1% (A)
# 3003 : Increase the temperature of Eurotherm 3408 by 1% (B)
# 3004 : Decrease the temperature of Eurotherm 3408 by -1% (B)
# 3005 : Increase the temperature of Eurotherm 3408 by 1% (C)
# 3006 : Decrease the temperature of Eurotherm 3408 by -1% (C)
# 3007 : Increase the temperature of Eurotherm 3408 by 1% (D)
# 3008 : Decrease the temperature of Eurotherm 3408 by -1% (D)

#################################################
#4000-4999 : Eurotherm controller related commands
#################################################

######################
#PROGRAM STARTS HERE
######################
#set_command [Time (second)] [commands] [arguments] 
set_command 0 0000
set_command 5 0001
set_command 10 0002
set_command 15 1003
set_command 15 1004
set_command 15 1005
set_command 15 1006
set_command 20 1007
set_command 22 1008
set_command 22 1009
set_command 22 1010 
#Start the command part for Shutter control unit
set_command 60 2001_90 2002_90 2003_-180 2004_0
set_command 61 2010
set_command 80 2005 2010
#Start the command for the Eurotherm Temperature controller
set_command 90 3001 3003 1002
set_command 95 3001 3003 1002
set_command 100 3001 3003 1002
set_command 105 3001 3003 1002