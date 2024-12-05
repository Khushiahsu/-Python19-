#Write a program to check the current date and time?
from datetime import date,time,datetime

today = date.today()
time = datetime.now()
print('Todays date is',today,'\n and the time currently is',time)


print('Date:',today.year)
print('Date:',today.month)
print('Date:',today.day)