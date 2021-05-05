######################
# Name: Darren Bowers
# Final Project
# Purpose: Program to import .dat file, filter out incomplete data and then
# perform a race based on random number generations. 
######################

import sys
import os.path
from car import Car
import functions as fn

FIRST_LAP = 20
PIT_STOP = 10
SECOND_LAP = 5
GO_HOME = 100


def main():
    line_count = 0
    argc = len(sys.argv)
    if argc==2 and os.path.isfile(sys.argv[1]):
        print('\nloading cars from file...')
        car_count = len(fn.make_list(sys.argv[1]))
        myCars = fn.make_list(sys.argv[1])
        print('done.\n')
        print(car_count, 'cars loaded...')
        for lines in myCars:
            line_count += 1
            print(line_count)
            lines.displayCar()
        
            
    else:
        print("Error: you must enter one-and-only-one parameter that is a valid file name.")



main()
