"""
ECE 241 - Fall 2024, Homework 2 question3.
"""

def condition_higher_than_65(temp):
    return temp > 65

def condition_lower_than_75(temp):
    return temp < 75



def nth_highest(alist, n):
    alist= alist.sort()
    alist.reverse()
    if n<len(alist):
        return alist[n-1]
    else:
        return None

def nth_lowest(alist, n):
    alist= alist.sort()
    if n<len(alist):
        return alist[n-1]
    else:
        return None


def average_if(alist, condition):
    newlst= []
    for i in alst:
        if i is condition:
            newlst.append(i)
            x= sum(newlst)/len(newlst)
            return x
        else:
            return 0

def range_if(alist, condition):
    newlst= []
    for i in alst:
        if i is condition:
            newlst.append(i)
            x= max(newlst)
            y= min (newlst)
            return x-y
        else:
            return 0

if __name__ == '__main__':
    N = 3
    temperatures = [72.4, 65.1, 58.6, 81.3, 44.8, 90.2, 68.9, 79.5, 53.7, 87.1]

    highest = nth_highest(temperatures, N)
    lowest = nth_lowest(temperatures, N)
    average = average_if(temperatures, condition_higher_than_65)
    temperature_range = range_if(temperatures, condition_lower_than_75)

    print("The " + str(N) + "th highest temperature is: " + str(highest))
    print("The " + str(N) + "th lowest temperature is: " + str(lowest))
    print("The average temperatures (given the temperature is higher than 65) is: " + str(average))
    print("The range of temperatures (given the temperature is lower than 75) is: " + str(temperature_range))

