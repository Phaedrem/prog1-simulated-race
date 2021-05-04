######################
# Name: Darren Bowers
# Final Project
# Purpose: Program to import .dat file, filter out incomplete data and then
# perform a race based on random number generations. 
######################

import sys
import os.path
import car as Car


def main():
    list_of_lists = []
    argc = len(sys.argv)
    if argc==2:
        if os.path.isfile(sys.argv[1]):
            fin = open(sys.argv[1], 'r')
            for line in fin:
                stripped_line = line.strip()
                line_list = stripped_line.split(',')
                list_of_lists.append(line_list)
                #model = line_list[0]
                #make = line_list[1]
            print(list_of_lists)
                
            
        else:
            print("Error: you must enter one-and-only-one parameter that is a valid file name.")
    else:
        print("Error: you must enter one-and-only-one parameter that is a valid file name.")



main()
