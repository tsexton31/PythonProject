import urllib.request
import os.path
from os import path

dates = [] #list of all dates in raw format
dates_clean = [] #list of all dates in day/month/year format
dates_clean_day = [] #This is a list of every day of the month
last365days = []
oct_ints = []
entriesIn1995 = []
DaysOfMonth = {}
code = [] #contains a list of every error code
redirects = 0 #counts the times 3xx code appears
notsuccess = 0 #counts the times 4xx comes up
if path.isfile('log.txt') == False:

	print('Beginning file download with urllib...')
	url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
	urllib.request.urlretrieve (url, "log.txt")
	print('Download finished')

else:
	print('You already have the log file.')



logfile = open('log.txt', 'r')

for row in logfile:
	splitrow = row.split(' ')
	if(len(splitrow) > 8):
		code.append(splitrow[8])
	if(len(splitrow[3]) > 14): #cleans up dirty input data
		dates.append(splitrow[3]) #dates is a list of every date


for date in dates:
	dates_clean.append(date[1:12])
	dates_clean_day.append(date[1:3])

for day in dates_clean_day:
	if(day in DaysOfMonth):
		DaysOfMonth[day] += 1
	else:
		DaysOfMonth[day] = 1
#print(DaysOfMonth)

for date in dates_clean:

	if(date[7:] == '1995'):
		last365days.append(date)
		entriesIn1995.append(date)
	elif(date[7:] == '1994' and (date [3:6] == 'Nov' or 'Dec')):
		last365days.append(date)
	elif(date[7:] == '1994' and (date[3:6] == 'Oct')): #this is a list of all the ints past the 10th day in october
		oct_ints.append(int(date[:2]))

for integer in oct_ints:
	if integer >= 11:
		integer.append(last365days)



#Error code section looking for percent of cudes that are 4xx and 3xx
for numbers in code:
#	print(numbers)
	if(numbers[0] == '3'):
		redirects = redirects + 1
	if(numbers[0] == '4'):
		notsuccess = notsuccess + 1

#outputs
print()

print("Day: Number of Requests")
for key, value in sorted(DaysOfMonth.items()):
	print(f"{key} : {value}")
print()
print(f"The percent of not successful requests is {(notsuccess/len(dates))*100}%")
print(f"The percent of redirected requests is {(redirects/len(dates))*100}%")
print()
print(f"Total requests in 1995 is {len(entriesIn1995)}")
print()
print(f"Total requests in last 365 days is {len(last365days)}") #just realized the last 365 days is the whole log
#total number of rows
print(f"Total requests in time period of log is {len(dates)}")

#ends October 11 1995
