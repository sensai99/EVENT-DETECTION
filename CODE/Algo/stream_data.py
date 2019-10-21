import pre_processing as pp
import csv

# Reading the tweet text
with open("/home/sai/Music/pulwama.csv","r") as file :
	reader = csv.reader(file, delimiter = ";")
	for i, line in enumerate(reader) :
		tweet_text = line[4]
		tweet_timestamp = line[1]
		# Creating Object
		obj = pp.pre_processing()
		tweet_text = obj.to_lower(tweet_text)
		tweet_text = obj.remove_urls(tweet_text)
		tweet_text = obj.remove_numbers(tweet_text)
		tweet_text = obj.remove_punctuation(tweet_text)
		tweet_text = obj.remove_whitespaces(tweet_text)
		tweet_text = obj.remove_stopwords(tweet_text)
		tweet_text = obj.stem_text(tweet_text)
		tweet_text = obj.remove_waste(tweet_text)
		tweet_text = obj.pos_tagging(tweet_text)
		tweet_text.append(tweet_timestamp)
		with open("stream_data.csv", "a") as fp:
		    wr = csv.writer(fp, dialect='excel')
		    wr.writerow(tweet_text)


# with open('filename', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(mylist)