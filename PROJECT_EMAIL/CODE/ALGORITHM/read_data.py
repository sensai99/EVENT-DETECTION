import numpy as np
import csv
import pandas as pd
import sort_timestamps as srt

emails_order, time = srt.main()
print(len(emails_order))

def read_words(path):
	data = {}
	with open(path,"r") as file :
		reader = csv.reader(file, delimiter = "\n")
		# lines = list(reader)
		# for i in emails_order:
		# 	line = lines[i]
		for i, line in enumerate(reader) :
			data['words'] = []
			data['word_frequencies'] = []
			l = line[0].split(',')

			# Reading tweet words and their frequencies
			for i in range(0,len(l)-2,2):
				data['words'].append(l[i])
				data['word_frequencies'].append(l[i+1])

			# Reading the timestamp of the tweet
			data['time_stamp'] = l[-1].split('"')[0]
			yield data

def read_nodes(path):
	data = {}
	with open(path,"r") as file :
		reader = csv.reader(file, delimiter = "\n")
		# lines = list(reader)
		# for i in emails_order:
		# 	line = lines[i]
		for i, line in enumerate(reader) :
			data['nodes'] = []
			l = line[0].split(',')

			# Reading the user and follower names
			for i in range(len(l) - 2):
				data['nodes'].append(l[i])
			yield data

def read_tweets(reader_words, reader_nodes) :
	A,B = next(reader_words), next(reader_nodes)
	tweet = {}
	tweet['words'] = A['words']
	tweet['word_frequencies'] = A['word_frequencies']
	tweet['time_stamp'] = A['time_stamp']
	tweet['nodes'] = B['nodes']
	tweet['tf_idf'] = []
	return tweet