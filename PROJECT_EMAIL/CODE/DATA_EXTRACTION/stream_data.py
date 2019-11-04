import pandas as pd
import pre_processing as pp
from collections import Counter
import csv

emails = pd.read_csv('/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/emails.csv')

print(emails.shape)

def extract_data(message) :

	message_body = ""
	sender = ""
	subject = ""
	receiver = []
	a, b, c, d = (0, 0, 0, 0)
	flag = False

	lines = message.split('\n')

	for line in lines :

		# Body
		if ':' not in line :

			# If calendar in message body then discard the email
			if "calendar" in line or "Calendar" in line :
				flag = True
				break

			if message_body != "" :
				message_body = message_body + " " + line

			else :
				message_body += line

		# Time
		elif "Date: " in line and a == 0:
			message_timestamp = line.split("Date: ")[1].split("\n")[0]
			a = 1

		# Subject
		elif "Subject:" in line and b == 0:

			subject = line.split("Subject:")[1].split("\n")[0]

			if "calendar" in subject or "Calendar" in subject :
				flag = True
				break

			if "Re:" in subject:
				subject = subject.split("Re:")[1].split("\n")[0]
				
			b = 1

		# Sender
		elif "From: " in line and c == 0 :

			if "@enron.com" not in line :
				flag = True
				break

			sender = line.split("From: ")[1].split("@")[0]

			if sender == "user" :
				flag =  True
				break
			c = 1

		# Receiver
		elif "To: " in line and d == 0:

			if "@enron.com" not in line :
				flag = True
				break

			list_ = line.split("To: ")[1].split(',')
			for i in list_ :
				rec = i.split("@")[0]
				if rec != "no_address" :
					receiver.append(i.split("@")[0])
			d = 1

		# # Folder
		# elif "X-Folder:" in  line and e == 0:

		# 	folder = line.split("\\")[1].split("\\")[1].split("\\")[1]

		# 	if "Calendar" in line or "calendar" in line :
		# 		flag =  True
		# 		break

	receiver.insert(0, sender)
	return message_body, message_timestamp, receiver, subject, flag


prev_message_body = []
prev_message_user = []

for i in range(1, emails.shape[0] + 1) :

	print(i)

	message_body, message_timestamp, message_user, subject, flag = extract_data(emails['message'][i])

	if flag == False :
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

		if len(message_user) >= 2 and len(message_body) != 0:

			if message_body != prev_message_body[:len(prev_message_body) - 1] or message_user != prev_message_user[:len(prev_message_user) - 1] :

				prev_message_user  =  message_user
				prev_message_body = message_body

				message_body.append(message_timestamp)
				message_user.append(message_timestamp)

				Subject = []
				Subject.append(subject)
				Subject.append(message_timestamp)

				with open("/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/email_data.csv", "a") as fp:
					wr = csv.writer(fp, dialect='excel')
					# if message_body != "" :
					wr.writerow(message_body)

				with open("/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/email_user_data.csv", "a") as fp:
					wr = csv.writer(fp, dialect='excel')
					# if message_user != "" :
					wr.writerow(message_user)

				with open("/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/email_subject_data.csv", "a") as fp:
					wr = csv.writer(fp, dialect='excel')
					# if message_user != "" :
					wr.writerow(Subject)


# with open('filename', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(mylist)