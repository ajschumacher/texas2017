import csv
import gzip


def function(infile):
    with gzip.open(infile, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        gdelt = [line for line in reader]
    return {'total': len(gdelt)}
