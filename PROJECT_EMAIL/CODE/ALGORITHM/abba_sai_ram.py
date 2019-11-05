import csv
import sort_timestamps as srt

emails_order, time = srt.main()
print(len(emails_order))

path_unsorted = "/home/dheerajracha/BTech/SEM 5/Data_mining/Project/PROJECT_EMAIL/DATA/final_email_user_data.csv"
path = "sorted_data.csv"
with open(path_unsorted,"r") as file :
		reader = csv.reader(file, delimiter = "\n")
		lines = list(reader)
		for i in emails_order:
			line = lines[i]
			with open(path, "a") as fp:
				wr = csv.writer(fp, dialect='excel')
				wr.writerow(line)
