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
    winningModel = 0
    winningMake = 0
    lineCount = 0
    argc = len(sys.argv)
    if argc==2 and os.path.isfile(sys.argv[1]):
        print('\nloading cars from file...')
        myCars = fn.make_list(sys.argv[1])
        carCount = len(myCars)
        print('done.\n')
        print(carCount, 'cars loaded...')
        for lines in myCars:
            lineCount += 1
            print(lineCount)
            lines.displayCar()
        print('\nLet the race begin...')
        fn.race(myCars)
        print('done\n')
        for cars in myCars:
            if cars.getSpeed() > speed:
                speed = cars.getSpeed()
                winningModel = cars.getModel()
                winningMake = cars.getMake()
            print(cars.getMake(),cars.getModel(), 'ended at', cars.getSpeed())
  
        print('\nThe winner is:', winningMake, winningModel, 'at',speed)
        print('\nHitting the brakes 100 times on each car...')
        fn.stop(myCars)
        print('done\n\nCars final speed...')
        for cars in myCars:
            print(cars.getModel(), ':', cars.getSpeed())
        
    else:
        print("Error: you must enter one-and-only-one parameter that is a valid file name.")



main()
