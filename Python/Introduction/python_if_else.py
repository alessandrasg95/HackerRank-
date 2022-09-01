import math
import os
import random 
import re
import sys


if __name__ == '__main__':
    n = int(input().strip()) #INPUT FORMAT: this is needed
#strip removes the whitespaces
if n%2!=0: #n is odd 
    print("Weird")
elif n%2==0 and n>=2 and n<=5: #n is even and in the inclusive range of 2 to 5
    print("Not Weird")
elif n%2==0 and n>=6 and n<=20: #n is even and n the inclusive range of 6 to 20
    print("Weird")
else: #n is even and greater than 20
    print("Not Weird")
