Overview
============
Next-generation sequencing of tumor/normal pairs provides a good opportunity to examine large-scale copy number variation in the tumor relative to the normal sample.  In practice, this concept seems to extend even to exome-capture sequencing of pairs of tumor and normal.  This library consists of a single script, ngCGH, that computes a pseudo-CGH using simple coverage counting on the tumor relative to the normal.

Usage is very basic::

  $ ngCGH -h
  usage: ngCGH [-h] [-w WINDOWSIZE] [-o OUTFILE] [-l LOGLEVEL]
               normalbam tumorbam

  positional arguments:
    normalbam             The name of the bamfile for the normal comparison
    tumorbam              The name of the tumor sample bamfile

  optional arguments:
  -h, --help            show this help message and exit
  -w WINDOWSIZE, --windowsize WINDOWSIZE
                        The number of reads captured from the normal sample
                        for calculation of copy number
  -o OUTFILE, --outfile OUTFILE
                        Output filename, default <stdout>
  -l LOGLEVEL, --loglevel LOGLEVEL
                        Logging Level, 1-15 with 1 being minimal logging and
                        15 being everything [10]

