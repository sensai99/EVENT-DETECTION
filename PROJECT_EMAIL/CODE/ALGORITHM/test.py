import numpy as np
import mmh3

class CountMinSketch(object):
    ''' Class for a CountMinSketch data structure
    '''
    def __init__(self, width, depth, seeds):
        ''' Method to initialize the data structure
        @param width int: Width of the table
        @param depth int: Depth of the table (num of hash func)
        @param seeds list: Random seed list
        '''
        self.width = width
        self.depth = depth
        self.table = np.zeros([depth, width])  # Create empty table
        self.seed = seeds # np.random.randint(w, size = d) // create some seeds

    def sketch_table(self):
    	return self.table

    def increment(self, key):
        ''' Method to add a key to the CMS
        @param key str: A string to add to the CMS
        '''
        for i in range(0, self.depth):
            index = mmh3.hash(key, self.seed[i]) % self.width
            print(index)
            self.table[i, index] = self.table[i, index]+1

    def get_hashvalues(self, key) :

    	index_list = []
    	for i in range(0, self.depth):
    		index = mmh3.hash(key, self.seed[i]) % self.width
    		index_list.append(index)

    	return index_list

    def estimate(self, key):
        ''' Method to estimate if a key is in a CMS
        @param key str: A string to check
        '''
        min_est = self.width
        for i in range(0, self.depth):
            index = mmh3.hash(key, self.seed[i]) % self.width
            if self.table[i, index] < min_est:
                min_est = self.table[i, index]
        return min_est

    def merge(self, new_cms):
        ''' Method to combine two count min sketches
        @param new_cms CountMinSketch: Another CMS object
        '''
        return self.table + new_cms


cms = CountMinSketch(16369,2,[3,1])
cms.increment("sai")
cms.increment("sai")
cms.increment("sree")
cms.increment("sreee")
list_ = cms.get_hashvalues("sai")
print(list_)
table = cms.sketch_table()
print(table[0, list_[0]])
print(table[1, list_[1]])
print(cms.estimate("sre"))