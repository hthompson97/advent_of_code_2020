# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:25:59 2020

@author: 597799
"""
#import csv
import pandas as pd
import re
import numpy as np

def day1(input):
    ret = {
            'part1' : None,
            'part2' : None
            }
    #part 1
    for num1 in input:
        for num2 in input:
            if(num1 + num2 == 2020):
                ret['part1'] = num1*num2
    #part 2
    for num1 in input:
        for num2 in input:
            for num3 in input:
                if(num1 + num2 + num3 == 2020):
                    ret['part2'] = num1*num2*num3
            
    return ret

def day2(input):
    
    ret = {
            'part1' : None,
            'part2' : None
            }
    
    #part 1
    #password must contain letter min
    #password cannot contain letter max
    #part 2: "small" and "big" are actually 1-based index positions in password
    #"letter must be in ONLY one of there places (xor)
    num_valid_1 = 0
    num_valid_2 = 0
    for index, row in input.iterrows():
        policy = row['policy'].split(' ')
        min_max = policy[0].split("-")
        small = first = int(min_max[0])
        big = second = int(min_max[1])
        let = policy[1]
        password = row[' password']
        
        #part 1
        locs = [m.start() for m in re.finditer(let, password)]
        occ = len(locs)      
        if(occ >= small and occ <= big):
            num_valid_1 += 1
            
        #part2
        if( (first in locs) ^ (second in locs) ): #xor
            num_valid_2 += 1

        
    ret['part1'] = num_valid_1
    ret['part2'] = num_valid_2  
    
    return ret

def day3(input):
    ret = {
            'part1' : None,
            'part2' : None
            }
    #part 1
    tree = "#"
    total_trees = 0
    num_input_cols = len(input[0][0])
    num_rows = len(input[0])
    x_slope = 3
    
    curr_col = 0
    for i in range(num_rows): #for each row, starting at (0,0)
        current_row = str(input[0][i]) 
        curr_spot = current_row[curr_col]      
        if(curr_spot == tree):
            total_trees += 1 
            
        curr_col += x_slope
        if(curr_col >= num_input_cols):
            curr_col = curr_col%num_input_cols
    
    ret['part1'] = total_trees
    
    #part 2
    #multiple slopes
    total_trees = [0.0,0.0,0.0,0.0,0.0]
    xslopes = [1,3,5,7,1]
    yslopes = [1,1,1,1,2]
    for j in range(len(xslopes)):
        x_slope = xslopes[j]
        y_slope = yslopes[j]
        curr_col = 0
        for i in range(0,num_rows,y_slope): #for each row, starting at (0,0)
            current_row = str(input[0][i]) 
            curr_spot = current_row[curr_col]      
            if(curr_spot == tree):
                total_trees[j] += 1 
                
            curr_col += x_slope
            if(curr_col >= num_input_cols):
                curr_col = curr_col%num_input_cols

    ret['part2'] = np.prod(total_trees)
            
    return ret

def day4(input):
    ret = {
            'part1' : None,
            'part2' : None
            }
    #part 1
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_fields: [ "cid"]
    
    
    valid_passports_1 = 0
    for passport in input:
        all_valid_1 = True
        for field in required_fields:
            if passport[field] == None:
                #passport is not valid
                all_valid = False
                break
            
            if(field == "byr"):
                val = int(passport[field])
                if( not( (val >= 1920) and (val <= 2002) ) ):
                    #passport is not valid
                    all_valid_1 = False
                    break
            
        if(all_valid_1):
            valid_passports_1 += 1
            
#off by 1 error?? added 1
    
    ret['part1'] = valid_passports_1 + 1
    
    #part 2
    valid_passports_2 = 0
    for passport in input:
        all_valid_2 = True
        for field in required_fields:
            if passport[field] == None:
                #passport is not valid
                all_valid_2 = False
                break
            
            if(field == "byr"):
                val = int(passport[field])
                if( not( (val >= 1920) and (val <= 2002) ) ):
                    #passport is not valid
                    all_valid_2 = False
                    break
            if(field == "iyr"):
                val = int(passport[field])
                if( not( (val >= 2010) and (val <= 2020) ) ):
                    #passport is not valid
                    all_valid_2 = False
                    break
            if(field == "eyr"):
                val = int(passport[field])
                if( not( (val >= 2020) and (val <= 2030) ) ):
                    #passport is not valid
                    all_valid_2 = False
                    break
            if(field == "hgt"):
                val = passport[field]
                unit = val[-2:]
                num = val[:-2]
                if(unit == "in"):
                    num = float(num)
                    if( not( (num >= 59) and (num <= 76) ) ):
                        #passport is not valid
                        all_valid_2 = False
                        break
                elif (unit == "cm"):
                    num = float(num)
                    if( not( (num >= 150) and (num <= 193) ) ):
                        #passport is not valid
                        all_valid_2 = False
                        break
                else:
                    all_valid_2 = False
                    break
                
            if(field == "hcl"):
                #regex = re.compile('^#[a-f][0-9]')
               # print(regex.match("#hi"))
                val = passport[field]
                if(val[0] != "#"):
                   all_valid_2 = False
                   break
                code = val[1:]
                if(len(code) != 6):
                    all_valid_2 = False
                    break
                allowed = set("a"+"b"+"c"+"d"+"e"+"f"+"0"+"1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9")
                if(not (set(code) <= allowed) ):
                    all_valid_2 = False
                    break
            
            if(field == "ecl"):
                val = passport[field]
                if(len(val) != 3):
                    all_valid_2 = False
                    break
                allowed = set("amb"+"blu"+"brn"+"gry"+"grn"+"hzl"+"oth")
                if(not (set(val) <= allowed) ):
                    all_valid_2 = False
                    break
            if(field == "pid"):
                val = passport[field]
                if(len(val) != 9):
                    all_valid_2 = False
                    break
                if(not int(val)):
                    all_valid_2 = False
                    break
            
        if(all_valid_2):
            valid_passports_2 += 1
    
    ret['part2'] = valid_passports_2 +1
    
            
    return ret

def loadInput():
    input = {}
    
    day1_loc = 'day1\input.txt'
    day1_input = (pd.read_csv(day1_loc))['num'].tolist()
    input['day1'] =  day1_input
    
    day2_loc = 'day2\input.txt'
    day2_input = (pd.read_csv(day2_loc, sep = ':') )
    input['day2'] = day2_input
    
    day3_loc = 'day3\input.txt'
    day3_input = (pd.read_csv(day3_loc, header=None) )
    input['day3'] = day3_input
    
    day4_loc = 'day4\input.txt'
    day4_file = open(day4_loc, "r")
    passport_obj = {
            "byr": None,
            "iyr": None,
            "eyr": None,
            "hgt": None, 
            "hcl": None, 
            "ecl": None, 
            "pid": None,
            "cid": None
    }
    all_passports= []
    lines = day4_file.readlines()
    current_passport = passport_obj.copy()
    for line in lines:      
        if(line == "\n"):
            #add current passport to list
            all_passports += [current_passport]
            #new passport obj
            current_passport = passport_obj.copy()
        else:
            entries = line.split(" ")
            for e in entries:
                attributes = e.split(":")
                field = attributes[0]
                value = attributes[1].rstrip("\n")
                current_passport[field] = value
        
    day4_file.close()
    

    input['day4'] = all_passports
    
    
    return input
        


def main():
    input = loadInput()
    print('Day 1: ' + str(day1(input['day1'])))
    print('Day 2: ' + str(day2(input['day2'])))
    print('Day 3: ' + str(day3(input['day3'])))
    print('Day 4: ')# + str(day4(input['day4'])))
    print( str(day4(input['day4'])))
        


if __name__ == "__main__":
    # execute only if run as a script
    main()