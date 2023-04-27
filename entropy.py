import os
import csv
import math

def entropy(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        if not data:
            return 0
        entropy = 0
        for x in range(256):
            p_x = float(data.count(x))/len(data)
            if p_x > 0:
                entropy += - p_x * math.log(p_x, 2)
        return entropy

# read file paths from a text file
with open('paths.txt', 'r') as f:
    file_paths = [line.strip() for line in f]

# calculate entropy for each file
results = []
for file_path in file_paths:
    if os.path.isfile(file_path):
        e = entropy(file_path)
        if e > 7:
            results.append((file_path, 1))
        else:
            results.append((file_path, 0))

# save results to a CSV file
with open('entropy1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['File Name', 'Entropy > 7'])
    for file_path, e in results:
        file_name = os.path.basename(file_path)
        writer.writerow([file_name, e])
