import numpy as np
import time, sys, os, csv
import argparse
import functions, read_data
from sklearn.metrics.pairwise import cosine_similarity
import write_clusters as wc

def FLAGS(args=sys.argv[1:]):
	parser = argparse.ArgumentParser()
	parser.add_argument("-alpha", default=0, type=float, help="Fractional Cluster Presence.")
	parser.add_argument("-delta", default=0, type=float, help="Count-Min Sketch.")
	parser.add_argument("-epsilon", default=0, type=float, help="Count-Min Sketch.")
	parser.add_argument("-num_clusters", default=500, type=int, help="Number of Clusters.")
	parser.add_argument("-Lambda", default=0.75, type=float, help="combining both sims")
	parser.add_argument("-path_words", default="/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/final_email_data.csv", type=str, help="--")
	parser.add_argument("-path_nodes", default="/home/sai/Documents/DATA MINING/PROJECT_EMAIL/DATA/final_email_user_data.csv", type=str, help="--")
	flags = parser.parse_args(args)
	return flags

class Event_Detection:

	def __init__(self, flags):
		self.flags = flags
		self.reader_words = read_data.read_words(self.flags.path_words)
		self.reader_nodes = read_data.read_nodes(self.flags.path_nodes)
		self.curr_num_clusters = 0
		self.tweet_counter = 1

		self.mean = 0.0
		self.standard_deviation = 0.0
		self.moments = np.zeros(3)
		# self.moments[0] = total count, self.moments[1] = total sum, self.moments[2] = square sum 

		self.initialize_clusters()
		return

	def initialize_clusters(self):
		self.clusters = [functions.cluster() for _ in range(self.flags.num_clusters)]
		return

	def update_moments(self, similarity):
		self.moments[0] = self.moments[0] + 1
		self.moments[1] = self.moments[1] + similarity
		self.moments[2] = self.moments[2] + similarity*similarity
		self.mean = self.moments[1]/self.moments[0]
		variance = (self.moments[2]/self.moments[0]) - self.mean**2
		self.standard_deviation = np.sqrt(variance)
		return

	def idf(self, word = None) :
		count = 0
		tf_count = np.zeros(self.curr_num_clusters)
		flag = np.zeros(self.curr_num_clusters)
		for index,cluster in enumerate(self.clusters):
			if word in cluster.words:
				## Assuming cluster word frequency is a dict
				# if self.tweet_counter == 1556 :
					# print(word, cluster.word_frequencies[word])
				tf_count[index] = cluster.word_frequencies[word] #check type of word
				count = count + 1
				flag[index] = 1

		idf = np.log((self.curr_num_clusters + 1.0)/(count + 1))
		# if self.tweet_counter == 1556 :
			# print(tf_count)
		return idf, tf_count, flag

	def content_similarity(self, stream):
		if self.curr_num_clusters == 0 :
			return
		else:
			similarities = []
			tf_idf_clusters = []
			idf_of_words = []
			for i in range(len(stream['words'])) :				
				idf, vector, x = self.idf(stream['words'][i])
				stream['tf_idf'].append(int(stream['word_frequencies'][i])*idf)
				tf_idf_clusters.append(vector)
				idf_of_words.append(idf)

			# if self.tweet_counter == 1556 :
				# print(idf_of_words)

			for i in range(len(tf_idf_clusters)):
				tf_idf_clusters[i] = np.multiply(tf_idf_clusters[i], idf_of_words[i])

			tf_idf_clusters = np.array(tf_idf_clusters).T
			# print(stream['tf_idf'])
			for i in range(self.curr_num_clusters) :
				den = np.linalg.norm(np.array(stream['tf_idf']))*np.linalg.norm(tf_idf_clusters[i])
				if den != 0:
					similarities.append( np.matmul( np.array(stream['tf_idf']), tf_idf_clusters[i].T)/den)
				else:
					similarities.append(0)
			return similarities

	def structural_similarity(self, stream):
		if self.curr_num_clusters == 0 :
			return
		else:
			similarities = []
			for i in range(self.curr_num_clusters):
				cluster = self.clusters[i]
				B = np.zeros(len(cluster.nodes)) # Optimizable :)
				for i,node in enumerate(cluster.nodes):
					if node in stream['nodes']:
						B[i] = 1
				sim = np.sum(np.multiply(B,cluster.node_frequencies))/(np.sqrt(len(stream['nodes'])+1)*np.sum(cluster.node_frequencies))
				similarities.append(sim)
			return similarities

	def assign_to_cluster(self, stream, structural_similarity, content_similarity):
		if self.curr_num_clusters == 0:
			self.clusters[0].add_stream(stream)
			wc.write_cluster(stream['words'], 0)
			self.curr_num_clusters = self.curr_num_clusters + 1
			print("\t New ","0")
			return
		else:
			SIM = list( self.flags.Lambda*np.array(structural_similarity) + (1-self.flags.Lambda)*np.array(content_similarity) )
			similarity = max(SIM)

			index = SIM.index(similarity)
			# print("\t",similarity, self.mean- 3*self.standard_deviation)
			threshold = (self.mean - 3*self.standard_deviation)
			if threshold <= 0:
				threshold = self.mean
			if similarity > threshold :
				self.clusters[index].add_stream(stream)
				wc.write_cluster(stream['words'], index)
				print("\t",index)
			else:
				if self.curr_num_clusters < self.flags.num_clusters:
					self.clusters[self.curr_num_clusters].add_stream(stream)
					wc.write_cluster(stream['words'], self.curr_num_clusters)
					print("\t New ",self.curr_num_clusters)
					self.curr_num_clusters = self.curr_num_clusters + 1
				else:
					print("Error")
					# a = 1
			self.update_moments(similarity)
			return

	def monitoring(self):
		while True:
			print("Incomming Tweet No. :",self.tweet_counter, self.curr_num_clusters,self.mean,self.standard_deviation)
			# print("Moments[0]: ", self.moments[0], "Moments[1]: ", self.moments[1], "Moments[2]: ", self.moments[2])
			tweet = read_data.read_tweets(self.reader_words, self.reader_nodes)
			if tweet is None:
				break
			elif len(tweet['words']) is 0:
				continue
			else :
				# if self.tweet_counter == 1556 :
					# print(tweet)
				c_s = self.content_similarity(tweet)
				s_s = self.structural_similarity(tweet)
				# if 1 :
					# print(tweet)
					# print("\t",self.curr_num_clusters,c_s,s_s)
				self.assign_to_cluster(tweet, s_s, c_s)
			# print("\n=====================")
			# for i_ in range(self.curr_num_clusters):
			# 	cluster = self.clusters[i_]
			# 	print("\t",cluster.word_frequencies)
			# print("=====================\n")
			# if self.tweet_counter >12:
			# 	break

			self.tweet_counter = self.tweet_counter + 1

		return

if __name__ == "__main__":

	flags = FLAGS()
	obj = Event_Detection(flags)
	obj.monitoring()
