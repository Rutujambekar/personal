import random 
import math
import os

#if__name__=='__main__':
n = int(input().strip())
if(n%2!=0) or (n>=6 and n<=20):
    print("weird")
else:
    print("not weird")    
