import urllib.request
import os.path
from os import path

#Variables
dates = [] #list of all dates in raw format
dates_clean = [] #list of all dates in day/month/year format
dates_clean_day = [] #This is a list of every day of the month
last365days = []
oct_ints = []
entriesIn1995 = []
DaysOfMonth = {}
Files = {}
Files_list = [] #list of all file names
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

Oct94 = open("Oct94.txt", "w")
Nov94 = open("Nov94.txt", "w")
Dec94 = open("Dec94.txt", "w")
Jan = open("Jan.txt", "w")
Feb = open("Feb.txt", "w")
Mar = open("Mar.txt", "w")
Apr = open("Apr.txt", "w")
May = open("May.txt", "w")
Jun = open("Jun.txt", "w")
Jul = open("Jul.txt", "w")
Aug = open("Aug.txt", "w")
Sep = open("Sep.txt", "w")
Oct95 = open("Oct95.txt", "w")

for row in logfile:
#	print(row)
	splitrow = row.split(' ')
	if(len(splitrow) > 8):
		code.append(splitrow[8]) #adds the error code to a list
		Files_list.append(splitrow[6]) #addes the file name to a list
	if(len(splitrow[3]) > 14): #cleans up dirty input data
		dates.append(splitrow[3]) #dates is a list of every date
#addin Oct94

	if(splitrow[3][4:7] == "Oct" and splitrow[3][8:12] == '1994'):
		Oct94.write(row)

	if(splitrow[3][4:7] == "Nov" and splitrow[3][8:12] == '1994'):
		Nov94.write(row)

	if(splitrow[3][4:7] == "Dec" and splitrow[3][8:12] == '1994'):
		Dec94.write(row)
	if(splitrow[3][4:7] == "Jan" and splitrow[3][8:12] == '1995'):
		Jan.write(row)
	if(splitrow[3][4:7] == "Feb" and splitrow[3][8:12] == '1995'):
		Feb.write(row)
	if(splitrow[3][4:7] == "Mar" and splitrow[3][8:12] == '1995'):
		Mar.write(row)
	if(splitrow[3][4:7] == "Apr" and splitrow[3][8:12] == '1995'):
		Apr.write(row)
	if(splitrow[3][4:7] == "May" and splitrow[3][8:12] == '1995'):
		May.write(row)
	if(splitrow[3][4:7] == "Jun" and splitrow[3][8:12] == '1995'):
		Jun.write(row)
	if(splitrow[3][4:7] == "Jul" and splitrow[3][8:12] == '1995'):
		Jul.write(row)
	if(splitrow[3][4:7] == "Aug" and splitrow[3][8:12] == '1995'):
		Aug.write(row)
	if(splitrow[3][4:7] == "Sep" and splitrow[3][8:12] == '1995'):
		Sep.write(row)
	if(splitrow[3][4:7] == "Oct" and splitrow[3][8:12] == '1995'):
		Oct95.write(row)


for date in dates:
	dates_clean.append(date[1:12])
	dates_clean_day.append(date[1:3])

# Day Dict construction
for day in dates_clean_day:
	if(day in DaysOfMonth):
		DaysOfMonth[day] += 1
	else:
		DaysOfMonth[day] = 1
#print(DaysOfMonth)


for file in Files_list:
	if(file in Files):
		Files[file] += 1
	else:
		Files[file] = 1

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

print(f"The most requested file is {max(Files, key=Files.get)}")
print(f"The least requested file is {min(Files, key=Files.get)}")
#for key, value in sorted(Files.items()): #prints a dict of all the files and times they appear
#	print(f"{key} : {value}")

print()
print(f"Total requests in 1995 is {len(entriesIn1995)}")
print(f"Total requests in last 365 days is {len(last365days)}") #just realized the last 365 days is the whole log
#total number of rows
print(f"Total requests in time period of log is {len(dates)}")


#ends October 11 1995


