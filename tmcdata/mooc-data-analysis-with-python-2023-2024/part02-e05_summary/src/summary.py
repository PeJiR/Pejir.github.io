#!/usr/bin/env python3

import sys
import re
import math

def summary(filename):
    with open(filename, "r") as file:
        summary_file = file.read()
        
        # Find the numeric values into a file
        regex = re.findall(r"([+|-]*\d+.?\d*)", summary_file)
        
        # Convert to floats to calculate the total, average and standard deviation
        
        
    
    
    return (0,0,0)

def main():
    pass

if __name__ == "__main__":
    main()
