######################
# Name: Darren Bowers
# Final Project
# Purpose: Program to import .dat file, filter out incomplete data and then
# perform a race based on random number generations. 
######################

import sys
import os.path
from car import Car


def main():
    standInList = []
    argc = len(sys.argv)
    if argc==2:
        if os.path.isfile(sys.argv[1]):
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
                myCars =[Car(make,model,year)]
                standInList.append(myCars)
            for car in standInList:
                car.displayCar()
            a_file.close()
        else:
            print("Error: you must enter one-and-only-one parameter that is a valid file name.")
    else:
        print("Error: you must enter one-and-only-one parameter that is a valid file name.")



main()
