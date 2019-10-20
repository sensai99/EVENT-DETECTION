import numpy as np
import time, sys, os
import argparse
from functions

def FLAGS(args=sys.argv[1:]):
	parser = argparse.ArgumentParser()
	parser.add_argument("-alpha", default=0, type=float, help="Fractional Cluster Presence.")
	parser.add_argument("-delta", default=0, type=float, help="Count-Min Sketch.")
	parser.add_argument("-epsilon", default=0, type=float, help="Count-Min Sketch.")
	parser.add_argument("-num_clusters", default=5, type=int, help="Number of Clusters.")
	flags = parser.parse_args(args)
	return flags

class Event_Detection:

	def __init__(self, flags):
		self.flags = flags
		self.variance = 0
		self.mean = 0
		self.initialize_clusters()
		return

	def initialize_clusters(slef):
		self.clusters = [functions.cluster() for _ in range(self.flags.num_clusters)]
		return

	def structural_similarity(self, stream):
		similarities = []
		for cluster in self.clusters:

			B = np.zeros(len(cluster.nodes))
			for i,node in enumerate(cluster.nodes):
				if node in stream['nodes']:
					B[i] = 1
			sim = np.sum(np.multiply(B,cluster.node_frequencies))/(np.sqrt(np.sum(stream['nodes'])+1)*np.sum(cluster.node_frequencies))
			similarities.append(sim)
		return similarities

	def content_similarity(self):
		similarities = []

		return similarities

	def assign_to_cluster(self, stream, structural_similarity, content_similarity):
		similarity = max(self.Lambda*structural_similarity + (1-self.Lambda)*content_similarity)
		index = similarity.index(max(similarity))
		if similarity > (self.mean - 3*self.variance):
			self.clusters[index].add_stream(stream)
		self.update_moments()

	def update_moments(self):

		return

	def monitoring(self):
		return


if __name__ == "__main__":

	flags = FLAGS()