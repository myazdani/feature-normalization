import os
import sys
import csv
import numpy 
import pandas
from sklearn.preprocessing import normalize

if len(sys.argv) < 2:
    in_file = '../../data/sample.csv'
else:
	in_file = sys.argv[1]
	out_file = "normalized" + in_file.split("/")[-1]

## specify ID column:
id_col = 0

## specify feature columns:
feature_cols = range(1,181)

data = pandas.read_csv(in_file, sep = ",", header = None)

features = numpy.array(data.ix[:,feature_cols])
normalized_features = normalize(features, norm = "l1", axis = 1)

f = open(out_file, 'wt')

try:
    writer = csv.writer(f)
    for i, normalized_feature in enumerate(normalized_features):
    	row = [data.ix[i,id_col]]
    	row.extend(normalized_feature)
        writer.writerow(row)
finally:
    f.close()