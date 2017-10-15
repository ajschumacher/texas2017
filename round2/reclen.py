import csv
import gzip
import collections


def function(infile):
    with gzip.open(infile, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        gdelt = [len(line) for line in reader]
    c = collections.Counter(gdelt)
    return dict(c.items())
