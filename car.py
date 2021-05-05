######################
# Name: Darren Bowers
# Final Project
# Purpose: Program to import .dat file, filter out incomplete data and then
# perform a race based on random number generations. 
######################

import sys
import os.path
import random

MINIMUM_SPEED = 0

class Car:
    
    def __init__(self, make, model, year):
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

    def getSpeed(self):
        return(self.__speed)

    def __setMake(self,make):
        if make == '':
            raise ValueError
        else:
            self.__make = make

    def __setModel(self,model):
        self.__model = model

    def __setYear(self,year):
        try:
            self.__year = int(year)
            if (self.__year >= 1910 and self.__year <= 2021):
                self.__year = year
            else: self.__year = 2021
        except:
            self.__year = 2021
            
    def displayCar(self):
        print('Make:',self.getMake())
        print('Model:',self.getModel())
        print('Year:',self.getYear())


    def accelerate(self):
        chance = random.randint(0,1)
        if chance == 0:
            self.__speed += 5
        else:
            self.__speed += 10

    def decelerate(self):
        chance = random.randint(0,1)
        if chance == 0:
            self.__speed -= 5
        else:
            self.__speed -= 10
        if self.__speed < MINIMUM_SPEED:
            self.__speed = MINIMUM_SPEED
