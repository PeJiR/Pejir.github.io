#!/usr/bin/env python3

import sys

def file_count(filename):
    lines = 0
    words = 0
    chars = 0
    
    with open(filename, "r") as file:
        # loop through each line and start counting 
        for line in file:
            lines += 1
            words += len(line.split())
            chars += len(line)     
    
    
    return (lines, words, chars)

def main():
    pass

if __name__ == "__main__":
    main()
