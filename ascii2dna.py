#!/usr/bin/env python

import begin
import itertools

def grouper(n, iterable):
    it = iter(iterable)
    while True:
       chunk = tuple(itertools.islice(it, n))
       if not chunk:
           return
       yield chunk

@begin.start
def main(inputs: 'ascii string or dna string',
         invert: 'if it\'s set convert dna to ascii' = False):

    bases = ['A', 'C', 'T', 'G']
    ascii2bases = dict()

    for indice, kmer in enumerate(itertools.product(bases, repeat=4)):
        if invert:
            ascii2bases["".join(kmer)] = indice
        else:
            ascii2bases[indice] = "".join(kmer)

    out = str()
    if invert:
        for kmer in grouper(4, inputs):
            out += chr(ascii2bases["".join(kmer)])
    else:
        for char in inputs:
            out += ascii2bases[ord(char)]

    print(out)
