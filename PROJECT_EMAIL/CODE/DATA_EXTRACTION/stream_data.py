import pandas as pd
import pre_processing as pp
from collections import Counter
import csv

emails = pd.read_csv('/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/emails.csv')

print(emails.shape)

def extract_data(message) :

	message_body = ""
	a, b, c = (0, 0, 0)

	lines = message.split('\n')

	for line in lines :

		# Body
		if ':' not in line :
			if message_body != "" :
				message_body = message_body + " " + line
			else :
				message_body += line

		# Time
		elif "Date: " in line and a == 0:
			message_timestamp = line.split("Date: ")[1].split("\n")[0]
			a = 1

		# Sender
		elif "From: " in line and b == 0:
			sender = line.split("From: ")[1].split("@")[0]
			b = 1

		# Receiver
		elif "To: " in line and c == 0:
			list_ = line.split("To: ")[1].split(',')
			receiver = []
			for i in list_ :
				receiver.append(i.split("@")[0])
			c = 1

	receiver.insert(0, sender)
	return message_body, message_timestamp, receiver



for i in range(1, emails.shape[0]) :

	print(i)
	message_body, message_timestamp, message_user = extract_data(emails['message'][i])
	# print(nodes)

	# Creating Object
	obj = pp.pre_processing()
	message_body = obj.pos_tagging(message_body)
	message_body = obj.remove_waste(message_body)
	message_body = ' '.join([str(elem) for elem in message_body])
	message_body = obj.remove_urls(message_body)
	message_body = obj.to_lower(message_body)
	message_body = obj.remove_numbers(message_body)
	message_body = obj.remove_punctuation(message_body)
	message_body = obj.remove_whitespaces(message_body)
	message_body = obj.remove_stopwords(message_body)

	# message_body may be null handle the case when finding the content similarity
	# print(message_body)

	list_ = Counter(message_body)
	message_body = []
	for key, value in list_.items():
		message_body.append(key)
		message_body.append(value)
	message_body.append(message_timestamp)

	with open("/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/email_data.csv", "a") as fp:
		wr = csv.writer(fp, dialect='excel')
		# if message_body != "" :
		wr.writerow(message_body)

	with open("/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/email_user_data.csv", "a") as fp:
		wr = csv.writer(fp, dialect='excel')
		# if message_user != "" :
		wr.writerow(message_user)


# with open('filename', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(mylist)