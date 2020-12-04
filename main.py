# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:25:59 2020

@author: 597799
"""
#import csv
import pandas as pd

def day1(input):
    for num1 in input:
        for num2 in input:
            if(num1 + num2 == 2020):
                return num1*num2
    return None

def loadInput():
    input = {}
    
    day1_loc = 'day1\input.txt'
    day1_input = (pd.read_csv(day1_loc))['num'].tolist()
           
    input['day1'] =  day1_input
    return input
        


def main():
    input = loadInput()
    print('Day 1: ' + str(day1(input['day1'])) )
        


if __name__ == "__main__":
    # execute only if run as a script
    main()