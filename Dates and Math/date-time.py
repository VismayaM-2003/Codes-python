#Python Dates
#Import the datetime module and display the current date:
import datetime

today = datetime.datetime.now()   #2023-10-13 18:17:18.953099
print(today)


print("******************************")

#Date output.
#The date contains year, month, day, hour, minute, second, and microsecond.

#The datetime module has many methods to return information about the date object.
import datetime
 
result = datetime.datetime.now()

print(result.hour)      #returns the hour
print(result.year)      #returns the year
print(result.day)       #returns the day
print(result.month)     #returns the month
print(result.strftime("%A"))    #returns the weekday

print("***************************************")

#Creating Date object

#To create a date, use the datetime() class (constructor) of the datetime module.
#The datetime() class requires three parameters to create a date: year, month, day.
import datetime

pack = datetime.datetime(2023, 10, 13)

print(pack)
#The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), 
#but they are optional, and has a default value of 0, (None for timezone).
#00:00:00
print("****************************************")

#The strftime() method-The datetime object has a strftime() method for formatting date objects into readable strings.
#it takes one parameter, format, to specify the format of the returned string:
import datetime

my_result = datetime.datetime(2023, 10, 13)

print(my_result.strftime("%B"))   #display the name of the month

print("*****************************")

#strftime()
import datetime

my_result = datetime.datetime.now()

print(my_result.strftime("%a"))       #	Weekday, short version	(Wed)
print(my_result.strftime("%A"))       #	Weekday, full version	(Wednesday)
print(my_result.strftime("%w"))       # Weekday as a number 0-6, 0 is Sunday	(3)
print(my_result.strftime("%d"))       #	Day of month 01-31	(31)
print(my_result.strftime("%b"))       # Month name, short version	(Dec)
print(my_result.strftime("%B"))       # Month name, full version	December
print(my_result.strftime("%m"))       # Month as a number 01-12	(12)
print(my_result.strftime("%y"))       # Year, short version, without century (18)
print(my_result.strftime("%Y"))       # Year, full version	(2018)
print(my_result.strftime("%H"))       #	Hour 00-23	(17)
print(my_result.strftime("%I"))       #	Hour 00-12	(05)
print(my_result.strftime("%p"))       # AM/PM	(PM)
print(my_result.strftime("%M"))       # Minute 00-59	(41)
print(my_result.strftime("%S"))       # Second 00-59	(08)
print(my_result.strftime("%f"))       #	Microsecond 000000-999999 (548513)
print(my_result.strftime("%z"))       #	UTC offset	(+0100)
print(my_result.strftime("%Z"))       # Timezone	(CST)
print(my_result.strftime("%j"))       # Day number of year 001-366	(365)
print(my_result.strftime("%U"))       # Week number of year, Sunday as the first day of week, 00-53 (52)   
print(my_result.strftime("%W"))       #	Week number of year, Monday as the first day of week, 00-53	52
print(my_result.strftime("%c"))       # Local version of date and time	(Mon Dec 31 17:41:00 2018)
print(my_result.strftime("%C"))       # Century	(20)
print(my_result.strftime("%x"))       #	Local version of date	(12/31/18)
print(my_result.strftime("%X"))       # Local version of time	(17:41:00)
print(my_result.strftime("%%"))       #	A % character	(%)
print(my_result.strftime("%G"))       #	ISO 8601 year	(2018)
print(my_result.strftime("%u"))       # ISO 8601 weekday (1-7)	(1)
print(my_result.strftime("%V"))       #	ISO 8601 weeknumber (01-53)	(01)
