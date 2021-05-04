######################
# Name: Darren Bowers
# Final Project
# Purpose: Program to import .dat file, filter out incomplete data and then
# perform a race based on random number generations. 
######################

import sys
import os.path

class Car:
    
    def __init__(self, make, model, year=2021):
        self.__model = model
        self.__make = make
        self.__year = year
        self.__speed = 0

    def getMake(self):
        return(self.__make)

    def getModel(self):
        return(self.__model)

    def getYear(self):
        return(self.__year)
