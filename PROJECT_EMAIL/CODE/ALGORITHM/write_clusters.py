import csv

def write_cluster(path, cluster_id, tweet_id, new = False) :
	with open(path + str(cluster_id) +".csv", "a") as fp:
		wr = csv.writer(fp, dialect='excel')
		if new:
			wr.writerow([])
			wr.writerow(["Novel Event"])
			# print(tweet_id)
			wr.writerow(tweet_id)
		else:
			wr.writerow(tweet_id)