import numpy as np
import csv
import functions as fn
import main as mn

# Reading the tweet text
with open("final.csv","r") as file :
	reader = csv.reader(file, delimiter = ";")
	for i, line in enumerate(reader) :
		mn.