# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:39:00 2022

@author: wilwin
"""
import minimalmodbus
import socket
from time import sleep
import urllib3

class Eurotherm3508(minimalmodbus.Instrument):
    """Instrument class for Eurotherm 3500 process controller.

    Args:
        * portname (str): port name
        * slaveaddress (int): slave address in the range 1 to 247
    """
    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)

    def get_pv_loop1(self):
        """Return the process value (PV) for loop1."""
        return self.read_register(289, 1)

    def is_manual_loop1(self):
        """Return True if loop1 is in manual mode."""
        return self.read_register(273, 1) > 0

    def get_op_loop1(self):
        """Return the manual output (OP) for loop1."""
        return self.read_register(3, 1)

    def get_sp_loop1(self):
        """Return the (working) setpoint (SP) for loop1."""
        return self.read_register(5, 1)
    
    def get_sp_loop1(self):
        """Return the  setpoint (SP) for loop1."""
        return self.read_register(2, 1)
    
    def set_sp_loop1(self, value):
        """Set the SP1 for loop1.

        Note that this is not necessarily the working setpoint.

        Args:
            value (float): Setpoint (most often in degrees)
        """
        self.write_register(24, value, 1)
    
    def set_op_loop1(self, value):
        """Set the OP1 for loop1.
            value (float): Setpoint (most often in degrees)
        """
        self.write_register(3, value, 1)
        
    def set_op_rate(self, value):
        """Set the increase rate of the op"""
        self.write_register(37, value,1)
    
    def get_PID_Proportional(self):
        self.write_register(6,1)
        
    def get_PID_Integral(self):
        self.write_register(8,1)
    
    def get_PID_Derivative(self):
        self.write_register(9,1)
    def set_PID_Proportional(self, value):
        self.write_register(6, value,1)
        
    def set_PID_Integral(self, value):
        self.write_register(8, value,1)
    
    def set_PID_Derivative(self, value):
        self.write_register(9, value,1)



class PrologixGPIBEthernet:
    PORT = 1234

    def __init__(self, host, timeout=1):
        self.host = host
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM,
                                    socket.IPPROTO_TCP)
        self.timeout = 0
        self.set_timeout(timeout)

    def connect(self):
        self.socket.connect((self.host, self.PORT))

        self._setup()

    def close(self):
        self.socket.close()

    def select(self, addr):
        self._send('++addr %i' % int(addr))

    def write(self, cmd):
        self._send(cmd)

    def read(self, num_bytes=1024):
        self._send('++read eoi')
        return self._recv(num_bytes)

    def query(self, cmd, buffer_size=1024*1024):
        self.write(cmd)
        return self.read(buffer_size)

    def set_timeout(self, timeout):
        # see user manual for details on accepted timeout values
        # https://prologix.biz/downloads/PrologixGpibEthernetManual.pdf#page=13
        if timeout < 1e-3 or timeout > 3:
            raise ValueError('Timeout must be >= 1e-3 (1ms) and <= 3 (3s)')

        self.timeout = timeout
        self.socket.settimeout(self.timeout)

    def _send(self, value):
        encoded_value = ('%s\n' % value).encode('ascii')
        self.socket.send(encoded_value)

    def _recv(self, byte_num):
        value = self.socket.recv(byte_num)
        return value.decode('ascii')

    def _setup(self):
        # set device to CONTROLLER mode
        self._send('++mode 1')

        # disable read after write
        self._send('++auto 0')

        # set GPIB timeout
        self._send('++read_tmo_ms %i' % int(self.timeout*1e3))

        # do not require CR or LF appended to GPIB data
        self._send('++eos 3')


class PrologixGPIBEthernetDevice:
    def __init__(self, address, *args, **kwargs):
        self.address = address
        self.gpib = PrologixGPIBEthernet(*args, **kwargs)

    def connect(self):
        self.gpib.connect()
        self.gpib.select(self.address)

    def close(self):
        self.gpib.close()

    def write(self, *args):
        return self.gpib.write(*args)

    def read(self, *args):
        return self.gpib.read(*args)

    def query(self, *args):
        return self.gpib.query(*args)

    def idn(self):
        return self.query('*IDN?')

    def reset(self):
        self.write('*RST')
        

class FUG_MCP_Voltage(PrologixGPIBEthernetDevice):
    def get_voltage(self):
        return self.query('>M0?')
    
    def get_current(self):
        return self.query('>M1?')
    
    def set_V_ramp_func(self,value):
        """
        0: Standard, ">S0A" follows the programmed value in ">S0"
        immediately.
        1: ">S0A" follows the value in ">S0" with the adjusted ramp rate upwards and 
        downwards.
        2: ">S0A" follows the value in ">S0" with the adjusted ramp rate only upwards. When 
        programming downwards ">S0A" follows">S0" immediately.
        3: ">S0A" follows the value in ">S0" with a special ramp function only upwards. When programming downwards, ">S0A" follows 
        ">S0" immediately. Ramp between 0...1 with 11.11E-3 per second. Above 1: with ">S0R"
        4: Same as 2, but ">S0" as well as ">S0A" are set to zero if ">DON" = "0"
        """
        return print(self.query('>S0B '+str(value)))
    
    def set_V_ramp_rate(self,value):
        return print(self.query('>S0R '+str(value))) #Volt/s
    
    def check_V_ramp_status(self):
        if self.query('>S0S'):
            print("The voltage is equals to the set point")
        else:
            print("The voltage is not equal to the set point")
        return 
    
    def V_set_point(self,value):
        return print(self.query('U'+str(value)))
    
    def I_set_point(self,value):
        return print(self.query('I'+str(value)))
    
    def V_current_set_point(self):
        return print(self.query('>S0A?'))
    
    def output(self,value):#1 on 0 off, not that easy, please check the manual before using
        return print(self.query('F'+str(value)))
    
class AutoShutter:
    def __init__(self, IP, *args, **kwargs):
        self.IP = IP
        self.Angle1 = 0
        self.Angle2 = 0
        self.Angle3 = 0
        self.Angle4 = 0
        
    def send_command(self,Angle1,Angle2,Angle3,Angle4):
        """Long-running task."""
        self.Angle1 = Angle1
        self.Angle2 = Angle2
        self.Angle3 = Angle3
        self.Angle4 = Angle4
        http = urllib3.PoolManager()
        string = str(self.Angle1)+','+ str(self.Angle2)+','+str(self.Angle3)+','+str(self.Angle4)+','
        print( "http://"+self.IP+"/command_"+string)
        try:
            http.request("GET", "http://"+self.IP+"/command_"+string, timeout=1,retries=False)
        except Exception as error:
            print(error)
            pass
