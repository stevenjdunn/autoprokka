# autoprokka
A script that automatically invokes prokka on a directory of FASTA genomes and neatly organises the output.

Simply place genome assemblies in the .fasta file format into a single directory, and invoke the autoprokka.py script.

# Usage
autoprokka.py -i < path to directory containing assemblies > -o < path to output annotations and renamed .gff's >

# Adding flags to prokka
Edit line 82: 

        subprocess.call(['prokka', fastain, '-o', fastaout, '--prefix', pre])
        
To include your flags inside quotation marks followed by a comma, spaces should be replaced with a comma and another quoted field. For example to add the kingdom "Archaea" and run in fast mode, line 82 would be replaced with:

        subprocess.call(['prokka', fastain, '-o', fastaout, '--prefix', pre, '--kingdom', 'Archaea', '--fast'])

