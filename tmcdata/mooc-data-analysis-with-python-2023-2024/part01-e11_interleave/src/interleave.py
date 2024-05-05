#!/usr/bin/env python3

def interleave(*lists):
    interleave_list = []
    for x in zip(*lists):
        interleave_list.extend(x)
           
    return interleave_list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
