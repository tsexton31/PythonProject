import urllib.request
import os.path
from os import path

dates = []

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
	dates.append(splitrow[3]) #dates is a list of every date


print(dates)

#total number of rows
print(f"Total requests in time period of log is {len(dates)} ")
#log = open('ApacheLog.csv', 'w')
#print('https://s3.amazonaws.com/tcmg476/http_access_log')
