#!/usr/bin/env python3

def detect_ranges(L):
    L_sorted = sorted(L)
    result = []
    i=0
    while L_sorted:
        if len(L_sorted) ==1:
            result.append(L_sorted[0])
            L_sorted.pop(0)
        elif L_sorted[i+1] == L_sorted[i]+1:
            i+=1
            if i == len(L_sorted)-1:
                temp = (L_sorted[0],L_sorted[i]+1)
                L_sorted = []
                result.append(temp)
        else:
            if i == 0:
                result.append(L_sorted[0])
                L_sorted.pop(0)
            else:
                temp = (L_sorted[0], L_sorted[i]+1)
                del L_sorted[:i+1]
                result.append(temp)
                i =0
        return result
                          
    
    
    
    
    
    

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
