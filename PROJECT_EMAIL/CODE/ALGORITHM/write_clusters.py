import csv

def write_cluster(email_body, cluster_id) :
	with open("/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/cluster" + str(cluster_id) +".csv", "a") as fp:
		wr = csv.writer(fp, dialect='excel')
		# if message_body != "" :
		wr.writerow(email_body)