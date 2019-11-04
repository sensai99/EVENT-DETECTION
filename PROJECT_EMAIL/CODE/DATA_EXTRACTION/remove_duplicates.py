from more_itertools import unique_everseen

with open('combined.csv','r') as in_file, open('final.csv','w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)