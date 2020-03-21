#https://www.hackerrank.com/challenges/extra-long-factorials/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    kq=1
    for i in range(1,n+1):
      kq=kq*i  
    print(kq)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)