#!/bin/python3

import math
import os
import random
import re
import sys
import time

def climbingLeaderboard(scores, alice):
    kq=[]
    scores_r=[1]*len(scores)
    for i in range(1,len(scores)):
        if(scores[i]==scores[i-1]):
            scores_r[i]=scores_r[i-1]
        else:
            scores_r[i]=scores_r[i-1]+1
    # print('scores_r',scores_r)
    for alice_score in alice:
        if alice_score<scores[-1]:
            # print('rank',scores_r[-1]+1)
            kq.append(scores_r[-1]+1)
        elif alice_score==scores[-1]:
            kq.append(scores_r[-1])
        elif alice_score>=scores[0]:
            # print('rank',1)
            kq.append(1)
        else:
            index=binary_search(scores,alice_score)
            # print('rank',scores_r[index])
            kq.append(scores_r[index])
    return kq
def binary_search(L,key):
    lo=0
    hi=len(L)-1
    while(lo<=hi):
        mid=lo+(hi-lo)//2
        if(L[mid]==key):
            return mid
        elif(L[mid]<key):
            hi=mid
        else:
            lo=mid
        
        if hi-lo==1:
            return hi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
