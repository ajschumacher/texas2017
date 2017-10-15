import sys
import glob
import time
import pickle
import tempfile
import subprocess

_, runner, pyfile, indir, workers = sys.argv
workers = int(workers)
outdir = tempfile.mkdtemp()

infiles = glob.glob(indir + '/*')
outfiles = glob.glob(outdir + '/*')

for i, infile in enumerate(infiles):
    while len(outfiles) < i - workers:
        time.sleep(2)
        outfiles = glob.glob(outdir + '/*')
    print outdir, infile
    subprocess.Popen(['python', runner, pyfile, infile, outdir])

while len(outfiles) < len(infiles):
    time.sleep(2)
    outfiles = glob.glob(outdir + '/*')

result = dict()
for outfile in outfiles:
    with open(outfile, 'rb') as f:
        this_result = pickle.load(f)
    for key, value in this_result.iteritems():
        if key not in result:
            result[key] = value
        else:
            result[key] += value

with open(pyfile + '.pkl', 'wb') as f:
    pickle.dump(result, f, protocol=2)
