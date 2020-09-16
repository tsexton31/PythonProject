import urllib.request
import csv
import os.path
from os import path

if path.isfile('log.csv') == False:

	print('Beginning file download with urllib...')
	url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
	urllib.request.urlretrieve (url, "log.csv")
	print('Download finished')

else:
	print('You already have the log file.')


#log = open('ApacheLog.csv', 'w')
#print('https://s3.amazonaws.com/tcmg476/http_access_log')
