#Write a program to generate a random date and time from the given start and end dates.
import random
import time

def randomtime(startDate,endDate):
    print('We are printing the random date and time between ,',startDate , 'and',endDate)
    num = random.random()
    dateformat='%m/%Y/%d'
    starttime = time.mktime(time.strptime(startDate,dateformat))
    endtime = time.mktime(time.strptime(endDate,dateformat))
    randomtime = starttime + num*(endtime-starttime)
    randomdate = time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print('The random date is:',randomtime('1/2024/1','12/2024/31'))