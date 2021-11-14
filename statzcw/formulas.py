import math
from collections import Counter

def zcount(list1: list) -> float:
    """
    This function takes in a list and counts the number of entries in the list
    :param list: 
    :return: 
    """
    return len(list1)

def zmean(list1:list) -> float:
    """
    This function takes in a list and returns the mean/average
    :param list:
    :return:
    """
    return sum(list1)/len(list1)

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

def zstddev(list1:list) -> float:
    """
    this function takes in a list and returns sample standard deviation of the list
    :param list1:
    :return:
    """
    return math.sqrt(zvariance(list1))

def zstderr(list1:list) -> float:
    """
    This function takes in a list and returns standard error of the mean of the list
    :param list1:
    :return:
    """
    return zstddev(list1)/math.sqrt(zcount(list1))

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
