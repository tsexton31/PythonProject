import urllib.request
import os.path
from os import path

dates = [] #list of all dates in raw format
dates_clean = [] #list of all dates in day/month/year format
dates_clean_ints = [] 

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



print(dates_clean)

#total number of rows
print(f"Total requests in time period of log is {len(dates)} ")
#ends October 11 1995
