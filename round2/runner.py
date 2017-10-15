import os
import sys
import pickle

_, pyfile, infile, outdir = sys.argv
execfile(pyfile)
try:
    result = function(infile)  # defined in pyfile
except:
    result = {}
filename = os.path.basename(os.path.normpath(infile))
path = os.path.join(outdir, filename)
with open(path, 'wb') as f:
    pickle.dump(result, f, protocol=2)
