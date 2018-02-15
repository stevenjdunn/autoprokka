#!/usr/bin/env python
import os
import subprocess
import glob
import shutil
import argparse
import sys
import re

# Argparse argument setup
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True, help="Path to directory containing assemblies to be annotated")
parser.add_argument("-o", "--output", required=True, help="Path to output destination.")
args = parser.parse_args()

# Colour set up
class colours:
    warning = '\033[93m'
    bold = '\033[1m'
    term = '\033[0m'

# Logger set up
ansi_rm = re.compile(r'\x1b\[[0-9;]*m')
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("autospades.log", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(re.sub(ansi_rm, '', message))

sys.stdout = Logger()

# Welcome Message# Welcome Message
print ''
print ''
print  colours.bold + '######################'
print 'Welcome to AutoPROKKA'
print '######################' + colours.term
print ''

# Check output path exists, try to write.
if not os.path.exists(args.output):
    try:
        os.makedirs(args.output)
        print 'Output directory created.'
        print ''
    except Exception:
        print colours.warning + 'Could not create output directory!'
        print ''
        print 'Check that the path is correct and that you have the required permissions.'
        print ''
        print ''
        print colours.bold + '#############'
        print 'Script Failed'
        print '#############' + colours.term
        print ''
        print 'Errors written to:' + os.getcwd() + '/' + 'autoprokka.log'
        print ''
        sys.exit(1)

# Directory orientation
invokedfrom = os.getcwd()
os.chdir(args.input)
directory = os.getcwd()
os.chdir(invokedfrom)
os.chdir(args.output)
outputraw = os.getcwd()
outputgff = outputraw

# List comprehension
fasta = list(glob.glob(os.path.join(directory,'*.fasta')))
output = [x.replace(directory, outputraw).replace('.fasta', '/') for x in fasta]
prefixis = [x.replace(directory, '').replace('.fasta', '') for x in fasta]

#Invoke Prokka
print ''
print 'Commencing annotation'
print ''
for fastain, fastaout, pre in zip(fasta, output, prefixis):
        subprocess.call(['prokka', fastain, '-o', fastaout, '--prefix', pre])
print ''
print 'Annotation complete!'
print ''

# Rename .gff and copy to output.
gffnames = [x.replace(directory, '').replace('.fasta', '.gff') for x in fasta]
gfflocations = [''.join(x) for x in zip(output, gffnames)]
gffoutput = [outputgff + x for x in gffnames]
for gffin, gffout in zip(gfflocations, gffoutput):
    try:
        shutil.copyfile(gffin, gffout)
    except IOError as e:
        print colours.warning + 'The following files were not found, indicating that prokka did not finish correctly.'
        print e
        print 'Please check FASTA input.' + colours.term
        sys.exit(1)
# End
print ''
print 'Output gff files renamed and stored in:',
print outputraw
print ''
print 'Author: www.github.com/stevenjdunn'
print ''
print ''
print colours.bold +'########'
print 'Finished'
print '########' + colours.term
print ''
