from Nanoscale_instruments import PrologixGPIBEthernetDevice
from time import sleep

class ExampleDevice(PrologixGPIBEthernetDevice):
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

my_device = ExampleDevice(host='169.254.92.52', address=8)

# open connection
my_device.connect()

# run predefined commands
print(my_device.idn())
print(my_device.get_voltage())
print(my_device.get_current())
my_device.check_V_ramp_status()
print(my_device.V_current_set_point())
my_device.output(1)
my_device.V_set_point(0)   
my_device.set_V_ramp_func(1)
my_device.set_V_ramp_rate(10)
my_device.I_set_point(0.0001)#Keep the current below 0.1 ma for Cv MODE
#my_device.check_V_ramp_status()
#my_device.set_V_ramp_func(1)
#my_device.set_V_ramp_rate(1)
#my_device.V_set_point(1)    



#my_device.close()