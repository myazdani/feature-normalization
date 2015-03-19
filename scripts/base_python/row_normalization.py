import os
import sys
import csv
import glob
if len(sys.argv) < 2:
    in_file_1 = '../../data/'
    in_file_2 = "../../filenames.csv"
    out_file = "../../results.csv"
else:
    in_file_1 = sys.argv[1]
    in_file_2 = sys.argv[2]
    out_file = sys.argv[3]

## specify ID column:
id_col = 0

## specify feature columns:
feature_cols = range(1,181)

def probability_normalize(feature, id = id_col, id_start = feature_cols[0], id_end = feature_cols[-1]):
	feature_float = map(float, feature[id_start: id_end+1])
	normalization_const = sum(feature_float)
	feature_normalized = [f/normalization_const for f in feature_float]
	return (feature[id], feature_normalized)

def max_normalize(feature, id = id_col, id_start = feature_cols[0], id_end = feature_cols[-1]):
	feature_float = map(float, feature[id_start: id_end+1])
	normalization_const = max(feature_float)
	feature_normalized = [f/normalization_const for f in feature_float]
	return (feature[id], feature_normalized)

csv_images = csv.reader(open(in_file_2))
images = []
for row in csv_images:
    images.extend(row)
images.pop(0)

normalized_features = []

in_files = glob.glob(in_file_1 + "*")
for in_file in in_files:
    csv_f = csv.reader(open(in_file))
    for row in csv_f:
        if row[0] in images: normalized_features.append(probability_normalize(row))

f = open(out_file, 'wt')

try:
    writer = csv.writer(f)
    for normalized_feature in normalized_features:
    	row = [normalized_feature[0]]
    	row.extend(normalized_feature[1])
        writer.writerow(row)
finally:
    f.close()