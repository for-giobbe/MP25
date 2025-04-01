#!/usr/bin/env python3
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
import requests

RECODING_SCHEMES = {
    'dayhoff6': {
        'C': '0',
        'G': '1', 'A': '1', 'S': '1', 'T': '1', 'P': '1',
        'D': '2', 'E': '2', 'N': '2', 'Q': '2',
        'R': '3', 'K': '3', 'H': '3',
        'M': '4', 'I': '4', 'L': '4', 'V': '4',
        'F': '5', 'Y': '5', 'W': '5'
    },
	'RS4': {
	'A': 'A', 
	'C': 'C',	
	'F': 'T', 
	'I': 'T', 
	'L': 'T', 
	'M': 'T',
	'V': 'T', 
	'W': 'C', 
	'Y': 'C',
	'D': 'G',
	'E': 'G',	
	'K': 'G',
	'R': 'G',
	'H': 'C',
	'N': 'A',
	'Q': 'G', 
	'S': 'A', 
	'T': 'A', 
	'G': 'A', 
	'P': 'A' 
}
}

def recode_sequence(seq, scheme):
    return ''.join(scheme.get(aa, 'X') for aa in seq)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recodes a protein sequence alignment using specified recoding schemes.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input FASTA file containing the protein alignment.")
    parser.add_argument("-o", "--output", required=True, help="Path to the output FASTA file to save the recoded alignment.")
    parser.add_argument("-s", "--scheme", required=True, choices=RECODING_SCHEMES.keys(), help="Recoding scheme to use.")
    parser.add_argument("-u", "--url", help="URL to download the input FASTA file.")
    return parser.parse_args()

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def main():
    args = parse_arguments()
    input_file = args.input

    if args.url:
        input_file = download_file(args.url, args.input)

    scheme = RECODING_SCHEMES[args.scheme]

    with open(input_file, "r") as infile, open(args.output, "w") as outfile:
        for record in SeqIO.parse(infile, "fasta"):
            recoded_seq = recode_sequence(str(record.seq), scheme)
            record.seq = Seq(recoded_seq)
            SeqIO.write(record, outfile, "fasta")

if __name__ == "__main__":
    main()
