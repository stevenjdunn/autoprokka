# autoprokka
A script that automatically invokes prokka on a directory of FASTA genomes and neatly organises the output.

Simply place genome assemblies in the .fasta file format into a single directory, and invoke the autoprokka.py script.

You will be prompted to enter the path containing your assemblies; this must be a complete path (i.e /home/user/directory).

The script invokes prokka and outputs the files to subdirectories named after the file; you will be prompted to specify a parent output directory - use ./ for pwd.

You can also specify whether you want the .gff annotation files to be placed into a single location; this will non-destructively copy the .gff file from each respective subdirectory to a path of your choice.

www.stevendunn.co.uk/autoprokka
