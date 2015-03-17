import os
import sys
import csv
import numpy 

if len(sys.argv) < 2:
    in_file = '../../data/sample.csv'
else:
    in_file = sys.argv[1]
    out_file = "normalized" + in_file.split("/")[-1]

## specify ID column:
id_col = 0

## specify feature columns:
feature_cols = range(1,181)

def probability_normalize(feature, id = id_col, id_start = feature_cols[0], id_end = feature_cols[-1]):
	feature_float = numpy.array(map(float,feature[id_start: id_end+1]))
	normalization_const = sum(feature_float)
	return (feature[id], feature_float/normalization_const)

def max_normalize(feature, id = id_col, id_start = feature_cols[0], id_end = feature_cols[-1]):
	feature_float = map(float, feature[id_start: id_end+1])
	normalization_const = max(feature_float)
	feature_normalized = [f/normalization_const for f in feature_float]
	return (feature[id], feature_normalized)

csv_f = csv.reader(open(in_file))

normalized_features = []
for row in csv_f:
  normalized_features.append(probability_normalize(row))

f = open(out_file, 'wt')

try:
    writer = csv.writer(f)
    for normalized_feature in normalized_features:
    	row = [normalized_feature[0]]
    	row.extend(normalized_feature[1])
        writer.writerow(row)
finally:
    f.close()