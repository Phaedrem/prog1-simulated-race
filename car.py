######################
# Name: Darren Bowers
# Final Project
# Purpose: Program to import .dat file, filter out incomplete data and then
# perform a race based on random number generations. 
######################

import sys
import os.path

class Cars:
    
    def __init__(self, model, make, year=2021):
        self.__model = model
        self.__make = make
        self.__year = int(year)
        self.__speed = 0
