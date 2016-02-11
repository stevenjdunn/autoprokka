#!/usr/bin/env python
import os
import subprocess
import glob

directory = raw_input("Path containing FASTA assemblies: ")
outputraw = raw_input("Path to output annotation directoies: ")
if not os.path.exists(outputraw):
    os.makedirs(outputraw)
fasta = list(glob.glob(os.path.join(directory,'*.fasta')))
output = [x.replace(directory, outputraw).replace('.fasta', '/') for x in fasta]
prefixis = [x.replace(directory, '').replace('.fasta', '') for x in fasta]

print ''
print ''
print 'Do you want to copy .gff into a single directory?'
print ''
choice = raw_input("Y/N? :").lower()
positive = set(['yes', 'ye', 'y', 'ys', ''])
if choice in positive:
    print ''
    print 'Which directory shall I place them in?',
    print ''
    outputgff = raw_input('Path to directory:')
    if not os.path.exists(outputgff):
        os.makedirs(outputgff)

for fastain, fastaout, pre in zip(fasta, output, prefixis):
        subprocess.call(['prokka', fastain, '-o', fastaout, '--prefix', pre])

if choice in positive:
    gffnames = [x.replace(directory, '').replace('.fasta', '.gff') for x in fasta]
    gfflocations = [''.join(x) for x in zip(output, gffnames)]
    gffoutput = [outputgff + x for x in gffnames]
    for gffin, gffout in zip(gfflocations, gffoutput):
        subprocess.call(['cp', gffin, gffout])


print ''
print 'Author: Steven Dunn'
print 'www.stevendunn.co.uk'
print ''
print ''
print '########'
print 'Finished'
print '########'
