#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 23:50:09 2022

@author: wilwin
"""

"""
Here is for general parameters used for all process
"""

universalparams ={  
  "Heatrate<300": 8.0,
  "Heatrate<800": 6,
  "Heatrate>800": 3.5,
  "Coolrate<300": -8.0,
  "Coolrate<800": -6,
  "Coolrate>800": -3.5,
  "Pressthreshold": 2,
  "IonbeamVrate": 0,
  "FilamentIrate": 0,
  "IonbeamVmax": 0,
  "FilamentImax": 0,
  "Shutterangle_A": 90,
  "Shutterangle_B": 90, 
  "Shutterangle_C": -180,
  "Shutterangle_D": 90,
  "Maxdegas_A": 1150,
  "Maxdegas_B": 1150,
  "Maxdegas_C": 1475,
  "Maxdegas_D": 1475,
  }

"""
Here is for some process dependent default parameters
"""
Calibration_Sn = {
  "Shutteropentemp_A": False,
  "Shutteropentemp_B": False,
  "Shutteropentemp_C": False,
  "Shutteropentemp_D": False,
  "Shutteropentime_A": False,
  "Shutteropentime_B": False,
  "Shutteropentime_C": False,
  "Shutteropentime_D": False,
  "Shutteropenclose_A": False,
  "Shutteropenclose_B": False,  
  "Shutteropenclose_C": False,
  "Shutteropenclose_D": False,
  "Delay": 0,
  "Capping_A": False,  
  "Capping_B": False,  
  "Capping_C": False,  
  "Capping_D": False,  
  "AnnealingIonbeamV": 0,  
  "AnnealingFilamentI": 0,  
  "Annealingtime": 0,  
  "Calibration": False,  
}