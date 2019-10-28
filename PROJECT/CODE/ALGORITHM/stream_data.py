import pre_processing as pp
import csv
from collections import Counter

# Reading the tweet text
with open("/home/sai/Documents/DATA MINING/PROJECT/CODE/DATA_EXTRACTION/GetOldTweets-python-master/data.csv","r") as file :
	reader = csv.reader(file, delimiter = ";")
	for i, line in enumerate(reader) :
		if i > 628570:
			tweet_text = line[4]
			tweet_timestamp  = line[1]
			# Creating Object
			obj = pp.pre_processing()
			tweet_text = obj.remove_s(tweet_text)
			tweet_text = obj.remove_urls(tweet_text)
			tweet_text = obj.to_lower(tweet_text)
			tweet_text = obj.remove_numbers(tweet_text)
			tweet_text = obj.remove_punctuation(tweet_text)
			tweet_text = obj.remove_whitespaces(tweet_text)
			tweet_text = obj.pos_tagging(tweet_text)
			tweet_text = obj.remove_stopwords(tweet_text)
			# tweet_text = obj.stem_text(tweet_text)
			tweet_text = obj.remove_waste(tweet_text)
			list_ = Counter(tweet_text)
			tweet_text = []
			for key, value in list_.items():
			    tweet_text.append(key)
			    tweet_text.append(value)
			tweet_text.append(tweet_timestamp)
			with open("/home/sai/Documents/DATA MINING/PROJECT/CODE/ALGORITHM/stream_data3.csv", "a") as fp:
			    wr = csv.writer(fp, dialect='excel')
			    if tweet_text != "" :
			    	wr.writerow(tweet_text)


# with open('filename', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(mylist)