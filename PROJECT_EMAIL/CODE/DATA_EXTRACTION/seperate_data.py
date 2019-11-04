import csv
reader = csv.reader(open("final.csv"))

itr = 0
for row in reader :

	# Iteration
	print(itr + 1)

	itr  = itr + 1
	for i, word in enumerate(row):
		if word == '++' :
			list1 = row[:i]
			list2 = row[i+1:]
			break

	with open("/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/final_email_data.csv", "a") as fp:
		wr = csv.writer(fp, dialect='excel')
		# if message_body != "" :
		wr.writerow(list1)

	with open("/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/final_email_user_data.csv", "a") as fp:
		wr = csv.writer(fp, dialect='excel')
		# if message_user != "" :
		wr.writerow(list2)
