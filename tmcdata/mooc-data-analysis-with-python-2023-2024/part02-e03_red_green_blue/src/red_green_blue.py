#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    results = []
     
    with open(filename, "r") as file:
         lines = file.readlines()[1:]
         for line in lines:
            regex = (               
                r"(\s*\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.+)"
                 
            ) 
            
            regex_matches = re.match(regex, line)
            regex_matches = regex_matches.groups()     
            
            regex_matches = f"{regex_matches[0]}\t{regex_matches[1]}\t{regex_matches[2]}\t{regex_matches[3]}"

            results.append(regex_matches)         
        
               
    
    
    
    return results


def main():
    pass

if __name__ == "__main__":
    main()
