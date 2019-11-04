import numpy as np
import csv
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag

stop_words = set(stopwords.words('english'))

class pre_processing :

	def __init__(self) :
		return

	# Convert text to lowercase
	def to_lower(self, text) :
		return text.lower()

	# Remove urls
	def remove_urls(self, text) :
		return re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', text)

	# Remove numbers
	def remove_numbers(self, text) :
		return re.sub(r'\d+', '', text)

	# Remove numbers
	def remove_s(self, text) :
		return re.sub(r'@[" "]*[^" "]+', '', text)
		# return re.sub(r"@.*[\t]", '', text)

	#  Remove punctuation
	def remove_punctuation(self, text) :
		return text.translate(str.maketrans("","", string.punctuation))

	#  Remove whitespaces
	def remove_whitespaces(self, text) :
		return text.strip()

	#  Remove stopwords
	def remove_stopwords(self, text) : 
		tokens = word_tokenize(text)
		return [i for i in tokens if not i in stop_words]

	# Stemming 
	def stem_text(self, text) :
		stemmer = PorterStemmer()
		return [stemmer.stem(item) for item in text]

	# Extracting the nouns
	def pos_tagging(self, text) :
		text = word_tokenize(text)
		 # and not pos.startswith('NNP')
		return [token for token, pos in pos_tag(text) if pos.startswith('N') and pos != 'NNP']

	# Remove
	def remove_waste(self, text) :
		return [i for i in text if not ".com" in i and len(i) != 1]



# # Reading the tweet text
# with open("/home/sai/Music/pulwama.csv","r") as file :
# 	reader = csv.reader(file, delimiter = ";")
# 	for i, line in enumerate(reader) :
# 		tweet_text = line[4]
# 		# Creating Object
# 		if  i == 1 :
# 			obj = pre_processing()
# 			print(tweet_text)
# 			tweet_text = obj.to_lower(tweet_text)
# 			tweet_text = obj.remove_urls(tweet_text)
# 			tweet_text = obj.remove_numbers(tweet_text)
# 			tweet_text = obj.remove_punctuation(tweet_text)
# 			tweet_text = obj.remove_whitespaces(tweet_text)
# 			tweet_text = obj.remove_stopwords(tweet_text)
# 			tweet_text = obj.stem_text(tweet_text)
# 			tweet_text = obj.remove_waste(tweet_text)
# 			tweet_text = obj.pos_tagging(tweet_text)
# 			print(tweet_text)
# 			print(type(tweet_text))
