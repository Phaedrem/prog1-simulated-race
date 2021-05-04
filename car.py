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
        self.__setMake(make)
        self.__setModel(model)
        self.__setYear(year)
        self.__speed = 0

    def getMake(self):
        return(self.__make)

    def getModel(self):
        return(self.__model)

    def getYear(self):
        return(self.__year)

    def __setMake(self,make):
        self.__make = make

    def __setModel(self,model):
        self.__model = model

    def __setYear(self,year):
        if isinstance(year,int) and (year >= 1910 and year <= 2021):
            self.__year = year
        else:
            self.__year = 2021
