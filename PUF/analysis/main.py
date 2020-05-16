import csv
import numpy as np

filename = "log.txt"

csvfile = open(filename)
reader = csv.reader(csvfile, delimiter="|")

challenges = []
output = []

for line in reader:
    c = line[0].strip('()').split(',')
    challenges.append(np.array(c))

    output.append(line[1])

challenges = np.array(challenges)
output = np.array(output)

print(challenges)
print(output)
