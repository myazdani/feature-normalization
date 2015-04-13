import os
import sys
import csv
import numpy 
import pandas

if len(sys.argv) < 2:
	print "please provide infile and outfile !"
else:
	in_file = sys.argv[1]
	out_file = sys.argv[2]


## specify ID column:
id_col = 0

## specify feature columns:
hue_cols = range(1,181)
sat_cols = range(181,181+256)
val_cols = range(181+256, 181 + 2*256)


data = pandas.read_csv(in_file, sep = ",", header = None)

print "read data success"

hue_mode = numpy.argmax(numpy.array(data.ix[1:,hue_cols], dtype = float), axis = 1)
print "hue mode success"
sat_mode = numpy.argmax(numpy.array(data.ix[1:,sat_cols], dtype = float), axis = 1)
print "sat mode success"
val_mode = numpy.argmax(numpy.array(data.ix[1:,val_cols], dtype = float), axis = 1)
print "val mode success"

filenames = data.ix[1:,0]

f = open(out_file, 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('Filename', 'H.mode', 'S.mode', 'V.mode') )
    for i, filename in enumerate(filenames):
        writer.writerow( (filename, hue_mode[i], sat_mode[i], val_mode[i]) )
finally:
    f.close()