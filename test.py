from itertools import chain, combinations
import sys
import re
import random
import os
import math
k = 87
s = "61197933 56459859 319018589 271720536 358582070 849720202 481165658 675266245 541667092 615618805 129027583 755570852 437001718 86763458 791564527 163795318 981341013 516958303 592324531 611671866 157795445 718701842 773810960 72800260 281252802 404319361 757224413 682600363 606641861 986674925 176725535 256166138 827035972 124896145 37969090 136814243 274957936 980688849 293456190 141209943 346065260 550594766 132159011 491368651 3772767 131852400 633124868 148168785 339205816 705527969 551343090 824338597 241776176 286091680 919941899 728704934 37548669 513249437 888944501 239457900 977532594 140391002 260004333 911069927 586821751 113740158 370372870 97014913 28011421 489017248 492953261 73530695 27277034 570013262 81306939 519086053 993680429 599609256 639477062 677313848 950497430 672417749 266140123 601572332 273157042 777834449 123586826"
s = list(s.split(' '))

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def checkSubsetDivide(sub_set, k):
    #sub_set => (1,7,2,4)
    # k= 3
    for i in range(len(sub_set)):
        e1 = sub_set[i]
        for j in range(i+1, len(sub_set)):
            e2 = sub_set[j]
            if((e1+e2) % k == 0):
                return False
    return True


def nonDivisibleSubset(k, s):
    # Write your code here
    # ko chia het cho  k
    # s: array of input set
    # print(k)
    # print(s)
    # print(list(powerset(s)))
    list_sub_set = list(powerset(s))[::-1]
    # print(list_sub_set)
    for sub_set in list_sub_set:
        # print(sub_set)
        if(checkSubsetDivide(sub_set, k)):
            return len(sub_set)
        # print(checkSubsetDivide(sub_set,k))


print(nonDivisibleSubset(k,s))
