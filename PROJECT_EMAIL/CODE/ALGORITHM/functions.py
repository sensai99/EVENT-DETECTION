import numpy as np
import time, sys, os
# import count_min_sketch as cms

class cluster:

	def __init__(self):
		self.create_new_cluster()

	def nodes(self):
		return self.nodes

	def node_frequencies(self):
		return self.node_frequencies

	def words(self):
		# print(self.words)
		return self.words

	# def count_min_sketch(self) :
	# 	return self.object

	def word_frequencies(self):
		return self.word_frequencies

	def create_new_cluster(self):
		self.nodes, self.node_frequencies = [], []
		self.words, self.word_frequencies = [], {}
		# self.object = cms.CountMinSketch(2, 16369, [3,1]) 
		return 


	def add_stream(self,stream):

		for node in stream['nodes']:
			if node in self.nodes:
				self.node_frequencies[self.nodes.index(node)] = self.node_frequencies[self.nodes.index(node)] + 1
			else:
				self.nodes.append(node)
				self.node_frequencies.append(1)
			# self.object.increment(node)

		for i,word in enumerate(stream['words']):
			if word in self.words:
				self.word_frequencies[word] = int(self.word_frequencies[word]) + int(stream['word_frequencies'][i])
			else:
				self.words.append(word)
				self.word_frequencies[word] = stream['word_frequencies'][i]
		return 

