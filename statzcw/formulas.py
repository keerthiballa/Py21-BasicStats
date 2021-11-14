import math
import statistics
from collections import Counter

import numpy
from scipy.stats import sem
import numpy as np
import pandas as pd


def zcount(list1: list) -> float:
    """
    This function takes in a list and counts the number of entries in the list
    :param list: 
    :return: 
    """
    return len(list1)

#print(zcount([1,2,3,4,5,6]))

def zmean(list1:list) -> float:
    """
    This function takes in a list and returns the mean/average
    :param list:
    :return:
    """
    return sum(list1)/len(list1)

#print(zmean([1,2,3,4,5,6]))
#print(statistics.mean(([1,2,3,4,5,6])))

def zmedian(list1:list) -> float:
    """
    This function takes in a list and returns the median of the list
    :param list:
    :return:
    """

    count_list = zcount(list1)

    list1.sort()

    if count_list % 2 == 1:
        return list1[count_list//2]
    else:
        return (list1[count_list//2 - 1] + list1[count_list//2])/2

#print(zmedian([1,2,3,4,5,6]))
#print(zmedian([1,2,3,4,5,6,7]))

#print(statistics.median([1,2,3,4,5,6]))
#print(statistics.median([1,2,3,4,5,6,7]))

def zmode (list1:list) -> float:
    """
    This function takes in a list and returns the mode of the list
    :param list1:
    :return:
    """
    count_list = zcount(list1)

    data = Counter(list1)
    get_mode = dict(data)
    mode = [k for k,v in get_mode.items() if v== max(list(data.values()))]

    if len(mode) == count_list:
        return None
    else:
        return float(mode[0])


#print(zmode([1,2,3,4,5.,5.,5.,6,6]))
#print(zmode([1,2,3,4,5,5,5,6,6,7]))

#print(statistics.mode([1,2,3,4,5.,5.,5.,6,6]))
#print(statistics.mode([1,2,3,4,5,5,5,6,6,7]))

def zvariance(list1:list) -> float:
    """
    This function takes in a list and returns sample variance of the list
    :param list1:
    :return:
    """
    n=zcount(list1)-1
    mean = sum(list1)/zcount(list1)
    variance_sample = sum([abs(x-mean)**2 for x in list1])/n
    return float(variance_sample)

#print(zvariance([1,2,3,4,5,6]))
#print(zvariance([1,2,3,4,5,6,7]))

#print(statistics.variance([1,2,3,4,5,6]))
#print(statistics.variance([1,2,3,4,5,6,7]))

def zstddev(list1:list) -> float:
    """
    this function takes in a list and returns sample standard deviation of the list
    :param list1:
    :return:
    """
    return math.sqrt(zvariance(list1))

#print(zstddev([1,2,3,4,5,6]))
#print(zstddev([1,2,3,4,5,6,7]))

#print(statistics.stdev([1,2,3,4,5,6]))
#print(statistics.stdev([1,2,3,4,5,6,7]))

def zstderr(list1:list) -> float:
    """
    This function takes in a list and returns standard error of the mean of the list
    :param list1:
    :return:
    """
    return zstddev(list1)/math.sqrt(zcount(list1))

#print(zstderr([1,2,3,4,5,6]))
#print(zstderr([1,2,3,4,5,6,7]))

#print(sem([1,2,3,4,5,6]))
#print(sem([1,2,3,4,5,6,7]))

def zcorr(listx:list, listy: list) -> float:
    """
    This function takes in two lists and returns correlation between the two lists
    :param listx:
    :param listy:
    :return:
    """
    sum = 0

    sub_x = [i - zmean(listx) for i in listx]
    sub_y = [i - zmean(listy) for i in listy]
    lengthx = zcount(listx)
    lengthy= zcount(listy)

    num_list = [sub_x[i]*sub_y[i] for i in range(lengthx)]
    num=0
    for i in num_list:
        num=num+ i
    den = lengthx-1
    cov=num/den

    if lengthx == lengthy:
        return cov/(zstddev(listx)*zstddev(listy))

    else:
        return cov

print(zcorr([1, 2, 3], [7, 8, 9]))
print(zcorr([1,2,3],[1,2,3]))
print(zcorr([1,2,3],[3,2,1]))


    #for i in range(0, zcount(listx)):
    #    sum += ((listx[i] - zmean(listx)) * (listy[i] - zmean(listy)))
    #cov= sum / (zcount(listx) - 1)
    #return cov / (zstddev((listx)) * zstddev(listy))


#print(zcorr([1,2,3,4,5,6,7],[8,9,10,11]))
#print(zcorr(([1,2,3],[1,2,3]), ([1,2,3],[3,2,1])))


#print(pd.Series[1,2,3,4,5,6].corr(pd.Series[7,8,9,10,11,12]))
#print(df.corr([1,2,3,4,5,6,7],[8,9,10,11]))