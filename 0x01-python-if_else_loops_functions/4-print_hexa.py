#!/usr/bin/python3
for i in range(0, 98):
    if (i != 101 and i != 113):
        print("{:d} = 0x{:x}" .format(i, i), end="\n")
