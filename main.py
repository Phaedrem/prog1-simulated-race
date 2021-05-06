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
    speed = 0
    winning_model = 0
    winning_make = 0
    line_count = 0
    argc = len(sys.argv)
    if argc==2 and os.path.isfile(sys.argv[1]):
        print('\nloading cars from file...')
        myCars = fn.make_list(sys.argv[1])
        car_count = len(myCars)
        print('done.\n')
        print(car_count, 'cars loaded...')
        for lines in myCars:
            line_count += 1
            print(line_count)
            lines.displayCar()
        print('\nLet the race begin...')
        fn.race(myCars)
        print('done\n')
        for cars in myCars:
            if cars.getSpeed() > speed:
                speed = cars.getSpeed()
                winning_model = cars.getModel()
                winning_make = cars.getMake()
            print(cars.getMake(),cars.getModel(), 'ended at', cars.getSpeed())
  
        print('\nThe winner is:', winning_make, winning_model, 'at',speed)
    else:
        print("Error: you must enter one-and-only-one parameter that is a valid file name.")



main()
