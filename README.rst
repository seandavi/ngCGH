Overview
============
Next-generation sequencing of tumor/normal pairs provides a good opportunity to examine large-scale copy number variation in the tumor relative to the normal sample.  In practice, this concept seems to extend even to exome-capture sequencing of pairs of tumor and normal.  This library consists of a single script, ngCGH, that computes a pseudo-CGH using simple coverage counting on the tumor relative to the normal.

I have chosen to use a fixed number of reads in the normal sample as the "windowing" approach.  This has the advantage of producing copy number estimates that should have similar variance at each location.  The algorithm will adaptively deal with inhomogeneities across the genome such as those associated with exome-capture technologies (to the extent that the capture was similar in both tumor and normal).  The disadvantage is that the pseudo-probes will be at different locations for every "normal control" sample.  

Installation
=============
There are several possible ways to install ngCGH.  


Usage
=====
Usage is very basic:

::

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


Output
======
The output format is also very simple:

::

  chr1    4851    52735   1000    854     -0.025120
  chr1    52736   59251   1000    812     -0.097876
  chr1    59251   119119  1000    876     0.011575
  chr1    119120  707038  1000    1087    0.322924
  chr1    707040  711128  1000    1016    0.225472
  chr1    711128  711375  1000    1059    0.285275
  chr1    711375  735366  1000    919     0.080709
  chr1    735368  798455  1000    972     0.161600

Columns 1-3 describe the chromosome, start, and end for each pseudo-probe.  The fourth column is the number of reads in the normal sample in the window while the fifth column represents the reads *in the same genomic window* from the tumor.  The last column contains the median-centered log2 ratio between tumor and normal.

