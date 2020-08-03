#write a Python program to print the date of all the Sundays of a specified year.

year=int(input("Enter year:"))
import datetime
def firstsun(n):
    x = datetime.datetime(n, 1, 1)
    de=datetime.timedelta(days=1)
    for i in range(7):
        if int(x.strftime("%w"))==0:
            return x
        x=x+de

s1=firstsun(year)
while(s1.year==year):
    print(s1.date())
    s1=s1+datetime.timedelta(days=7)
