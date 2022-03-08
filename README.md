# Program to get the functional annotation of protein sequence in fasta format

This program use [interproscan 5](https://interproscan-docs.readthedocs.io/en/latest/Introduction.html), you must install it.

## Download the program

1. Clone git repository

> HTTPS link

```
git clone https://github.com/Dylkln/functional_annotation.git
```

> SSH link

```
git clone git@github.com:Dylkln/functional_annotation.git
```

## How to use the program

```
python get_annotation.py -i <INTERPROSCAN LAUNCHER PATH> -p <PATH TO PROTEIN SEQUENCES DIRECTORY> -a <PATH TO OUTPUT>
```
The program will call interproscan for every file contained in you protein directory and redirect the output to your *-a* argument.
