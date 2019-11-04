import csv
reader1 = csv.reader(open("email_data.csv"))
reader2 = csv.reader(open("email_user_data.csv"))
f = open("combined.csv", "w")

writer = csv.writer(f)

for row1, row2 in zip(reader1, reader2) :
    writer.writerow(row1 + ["++"] + row2)

f.close()