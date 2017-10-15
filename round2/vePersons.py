import csv
import gzip
import collections

fields = [
    'DATE', 'NUMARTS', 'COUNTS',
    'THEMES', 'LOCATIONS', 'PERSONS', 'ORGANIZATIONS',
    'TONE', 'CAMEOEVENTIDS', 'SOURCES', 'SOURCEURLS']


def function(infile):
    result = collections.Counter()
    with gzip.open(infile, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            locations = line[fields.index('LOCATIONS')].lower()
            if not 'venezuela' in locations:
                continue
            persons = line[fields.index('PERSONS')].split(';')
            result.update(persons)
    return dict(result.items())
