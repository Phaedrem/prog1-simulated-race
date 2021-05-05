######################
# Name: Darren Bowers
# Final Project
# Purpose: Program to import .dat file, filter out incomplete data and then
# perform a race based on random number generations. 
######################

import sys
import os.path
from car import Car

FIRST_LAP = 20
PIT_STOP = 10
SECOND_LAP = 5
GO_HOME = 100

def make_list(file):
    myCars = []
    a_file = open(sys.argv[1], 'r')
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split(',')
        length = len(line_list)
        if length >= 2 and length < 4:
            make = line_list[0]
            model = line_list[1]
            if length == 3:
                year = line_list[2]
            else:
                year = ''
            try:
                myCars.append(Car(make,model,year))
            except:
                pass
    return(myCars)
    a_file.close()

def race(myCars):
    for speed in range(FIRST_LAP):
        for cars in myCars:
            cars.accelerate()
    for speed in range(PIT_STOP):
        for cars in myCars:
            cars.decelerate()
    for speed in range(SECOND_LAP):
        for cars in myCars:
            cars.accelerate()    
    return(myCars)

def stop(myCars):
    for speed in range(GO_HOME)
        for cars in myCars:
            cars.decelerate()
    return(myCars)
