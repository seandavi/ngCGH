from setuptools import setup, find_packages
import sys, os

version = '0.2.0'

setup(name='ngCGH',
      version=version,
      description="Pseudo-cgh of next-generation sequencing data",
      long_description="""
Overview
============
Next-generation sequencing of tumor/normal pairs provides a good opportunity to examine large-scale copy number variation in the tumor relative to the normal sample.  In practice, this concept seems to extend even to exome-capture sequencing of pairs of tumor and normal.  This library consists of a single script, ngCGH, that computes a pseudo-CGH using simple coverage counting on the tumor relative to the normal.

I have chosen to use a fixed number of reads in the normal sample as the "windowing" approach.  This has the advantage of producing copy number estimates that should have similar variance at each location.  The algorithm will adaptively deal with inhomogeneities across the genome such as those associated with exome-capture technologies (to the extent that the capture was similar in both tumor and normal).  The disadvantage is that the pseudo-probes will be at different locations for every "normal control" sample. 
 

Installation
=============
There are several possible ways to install ngCGH.  

github
-------
If you are a git user, then simply cloning the repository will get you the latest code.

::

  git clone git://github.com/seandavi/ngCGH.git

Alternatively, click the ``Download`` button and get the tarball or zip file.

In either case, change into the resulting directory and::

  cd ngCGH
  python setup.py install

From PyPi
-------------------
If you have easy_install in place, this should suffice for installation:

::

  easy_install ngCGH




Usage
=====
Usage is very simple:

::

    $ ngCGH -h
    usage: ngCGH [-h] [-w WINDOWSIZE] [-o OUTFILE] [-l LOGLEVEL] [-r REGIONS]
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
    -r REGIONS, --regions REGIONS
                        regions to which analysis should be restricted, either
                        a bed file name or a single region in format chrN:XXX-
                        YYY


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


Convert from ngCGH to Biodiscovery Nexus
----------------------------------------
Included in the release is a script, convert2nexus, that takes as input the filename of a file created by ngCGH and converts it into a file that the Nexus CGH software from BioDiscovery can load for further analysis.  The format looks like this:

::

  Name    Chromosome      Start   End     PALZGU.cgh
  chr1_10004      chr1    10004   15735   -2.087921
  chr1_15736      chr1    15736   69385   -2.670936
  chr1_69386      chr1    69386   521687  -0.428244
  chr1_523537     chr1    523537  726959  0.080269
  chr1_726959     chr1    726959  808542  0.223047
  chr1_808546     chr1    808546  809138  -1.186761


Convert from Complete Genomics to Biodiscovery Nexus
----------------------------------------------------
There is now plenty of Complete Genomics data floating around.  We are often interested in visualizing the somatic CNV data in Biodiscovery nexus.  There is a script, cgi2nexus that takes a file typically named as "SomaticCnvDetailsDiploidBeta*" and converts to the file format noted above.  Bzip2 (typical from CGI) are uncompressed on-the-fly.

Segmenting output
-------------------------
The cgh2seg script uses some sane defaults (at least for exomes) to the Circular Binary Segmentation algorithm as implemented in the DNAcopy Bioconductor package.  The segmented results are centered around the mode of the density of the segmented values on a per-probe basis.  The script will write the "Centrality parameter" to stderr when it completes.

The file format is:

:: 

  ID      chrom   loc.start       loc.end num.mark        seg.mean
  09      chr1    367695  82438842        2279    0.546541374526925
  09      chr1    82778033        93082545        206     0.077841374526925
  09      chr1    93205647        103965955       188     -0.913458625473075
  09      chr1    104000621       104166584       4       -0.216558625473075
  09      chr1    104342470       110014374       109     -0.948958625473075
  09      chr1    110024223       110058480       4       -1.38295862547308


Methods
============
The pseudo-cgh algorithm employed by ngCGH takes as input two appropriately matched BAM files, typically from a tumor and a matched normal.  Genomic windows are defined by reading blocks of a fixed number of reads (default 1000 reads) in the normal sample.  Within each defined genomic window, the number of reads in the tumor is quantified.  For each genomic window, a ratio is made between the number of reads in the tumor and the number of reads in the normal.  Finally, a log2 transformation is applied to each ratio and the entire vector of the results is then centered by subtracting the median.
""",
      classifiers=["Topic :: Scientific/Engineering :: Bio-Informatics"], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Sean Davis and Josh Waterfall',
      author_email='sdavis2@mail.nih.gov',
      url='http://github.com/seandavi/ngCGH',
      license='GPL-2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'pysam>=0.3.0'
      ],
      scripts = ['scripts/ngCGH',
                 'scripts/convert2nexus',
                 'scripts/cgh2seg'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
