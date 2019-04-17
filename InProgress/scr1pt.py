#!/usr/bin/env python
import sys

f = open("TLVInput", "w")
f.write("A" * 4) #this will fill tag
f.write("\x40\x00\x00\x00") #this will fill length
f.write("C" * 64) #fill value
f.close()


