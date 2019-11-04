import datetime
import time
import collections
import csv

reader = csv.reader(open('/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/final_email_data.csv'))

def convertToUnix(arr):
	timestampList = {}
	i = 0
	for t in arr :
		dt = datetime.datetime(t[0],t[1],t[2],t[3],t[4],t[5])
		unix_time = time.mktime(dt.timetuple())
		timestampList[unix_time] = i
		i = i+1

	return timestampList

def sortDict(timestampList) :
	l = []
	timestamps = []
	for key in sorted(timestampList):
		l.append(timestampList[key])
		timestamps.append(key)
	return l,timestamps

def preprocess(stringTimestamps) :
	arr = []

	months = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}

	for s in stringTimestamps :

		s1 = s.split(",")
		s2 = s1[1].split(" ")

		year = int(s2[3])
		month = months[s2[2]]
		day = int(s2[1])
		s3 = s2[4].split(":")
		hr = int(s3[0])
		minutes = int(s3[1])
		sec = int(s3[2])

		x = s.index('(')
		y = s.index(')')

		tz = s[x+1:y]

		if tz == "PDT" :
			hr = (hr + 7)%24

		elif tz == "PST" or tz == "PT" :
			hr = (hr + 8)%24

		else :
			hr = (hr + 8)%24

		t = [year,month,day,hr,minutes,sec]
		arr.append(t)

	return arr


# use this fuction
# pass a list of timestamps in the order read from the file
def getOrder(stringTimestamps):
	arr = preprocess(stringTimestamps)
	dictionary = convertToUnix(arr)
	l = sortDict(dictionary)
	return l


def main():
	# Reading timestamps
	timestamps_list = []
	for line in reader :
		timestamps_list.append(line[-1])

	# sample execution working correctly
	return getOrder(timestamps_list)

#["Fri, 4 May 2001 13:51:00 -0700 (PDT)","Fri, 3 May 2001 13:51:01 -0700 (PDT)"]