import urllib.request
import os.path
from os import path

dates = [] #list of all dates in raw format
dates_clean = [] #list of all dates in day/month/year format
last365days = []
oct_ints = []
entriesIn1995 = []

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
	if(len(splitrow[3]) > 14): #cleans up dirty input data
		dates.append(splitrow[3]) #dates is a list of every date
for date in dates:
	dates_clean.append(date[1:12])

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

print()
print(f"Total requests in 1995 is {len(entriesIn1995)}")
print()
print(f"Total requests in last 365 days is {len(last365days)}") #just realized the last 365 days is the whole log
#total number of rows
print(f"Total requests in time period of log is {len(dates)}")

#ends October 11 1995
