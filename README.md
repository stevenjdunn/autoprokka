![alt_text](https://i.imgur.com/g7aVcxo.png)

A script that automatically invokes prokka on a directory of FASTA genomes and neatly organises the output.

## Quick Start

autoprokka.py -i < path to directory containing assemblies > -o < path to output annotations and renamed .gff's >

## Usage

        usage: autoprokka.py [-h] -i INPUT -o OUTPUT [-gbk]

        optional arguments:
          -h, --help            show this help message and exit
          -i INPUT, --input INPUT
                                Path to directory containing assemblies to be
                                annotated
          -o OUTPUT, --output OUTPUT
                                Path to output destination.
          -gbk, --genbank       Also copies and renames genbank files into output
                                directory.
                                
### Requirements
* Python 3
* PROKKA
               
### What?
This script automatically invokes [PROKKA](https://github.com/tseemann/prokka) on a directory of prokaryotic genomes to obtain gene annotations with as little hands on time as necessary. 

The output contains subfolders and annotation files that are named according to the input .fasta filename. By default, autoPROKKA also gathers all .gff files and optionally all .gbk files for downstream use. 

### Why?
Time! This is easily my most used script on a day to day basis. Sure, a for loop would do it. But I find this neater and quicker for my usage. Want to quickly see how many genes are conserved amongst that clade of bacteria? autoprokka.py -i directory/ -o output/ && roary *.gff - 5 minutes later you have an answer.

### Adding flags to prokka
Edit line 82: 

        subprocess.call(['prokka', fastain, '-o', fastaout, '--prefix', pre])
        
To include your flags inside quotation marks followed by a comma, spaces should be replaced with a comma and another quoted field. For example to add the kingdom "Archaea" and run in fast mode, line 82 would be replaced with:

        subprocess.call(['prokka', fastain, '-o', fastaout, '--prefix', pre, '--kingdom', 'Archaea', '--fast'])

