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

def main():
    argc = len(sys.argv)
    if argc==2 and os.path.isfile(sys.argv[1]):
        for i in fn.make_list(sys.argv[1]):
            i.displayCar()
    else:
        print("Error: you must enter one-and-only-one parameter that is a valid file name.")



main()
