# Python Program for SPOJ Problem Number 6.
# Code started on 17/07/2017
# Last Edit on 14/07/2017
# Code by Nabeel Ahmad Khan

import math
import re

x=raw_input ("Enter the string")
print x 

first, second = re.split('[+,-,*,/]',x)

print first, " = first"
print second, " = second"

first = int(first)
second = int(second)

print first, " = first - int"
print second, " = second - int"

