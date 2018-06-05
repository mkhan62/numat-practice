"""Hi."""
import csv


data = []
count = 0

companies = {}
counts = 0
with open('Consumer_Complaints.csv') as file:
    for dat in csv.reader(file):
        if len(dat) > 7:
            print(dat[7])
            if dat[7] in companies:
                companies[dat[7]][1] += 1
            else:
                companies[dat[7]] = [dat[7], 1]

max = sorted(companies.values(), key=lambda x: x[1], reverse=True)
for i in range(1, 11):
    x, y = max[i]
    print(i, x, y)
