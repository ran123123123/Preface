#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Author: Mack
# @Time: 28/9/2022 PM 6:19 
# @File: rex.py
# @Software: PyCharm


import re

from_file = open(r"D:\Extreme Vision\Mack\Code\Preface\words")
print(from_file.read())


# open & read in_file
in_file = open(from_file)
indata = in_file.read()

# create & open & write to_file
out_file = open(to_file, 'w')
out_file.write(indata)

# print result
print("Alright, all done.")
# close out_file in_file
out_file.close()
in_file.close()
