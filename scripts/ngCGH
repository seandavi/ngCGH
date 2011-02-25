#!/usr/bin/env python
import optparse
import logging
import sys

import pysam
import ngs.regions

class Counter:
    mCounts = 0
    def __call__(self, alignment):
        self.mCounts += 1

class RegionalCount(ngs.regions.Region):
    def __init__(self,chromosome,rbeg,rend,count):
        ngs.regions.Region.__init__(self,chromosome,rbeg,rend)
        self._count=count

    def __str__(self):
        return("%s:%d-%d <%d>" % (self.chromosome,self.rbeg,self.rend,self._count))

def doNormalComparisonCGH(opts,args):
    tfile = pysam.Samfile(args[0],'rb')
    nfile = pysam.Samfile(opts.normalbam,'rb')
    lengths=nfile.lengths
    refnames=nfile.references
    outfile=sys.stdout
    if(opts.outfile is not None):
        outfile=open(opts.outfile,'w')
    for refidx in xrange(tfile.nreferences):
        n=0
        tfileiterator=tfile.fetch(refnames[refidx],0,lengths[refidx])
        tread=tfileiterator.next()
        for nread in nfile.fetch(refnames[refidx],0,lengths[refidx]):
            if(nread.is_duplicate): continue
            if(n==0):
                startloc = nread.pos
            n+=1
            if(n==1000):
                j=0
                while((tread.pos<nread.pos) & (tread.rname==nread.rname)):
                    tread=tfileiterator.next()
                    if(tread.is_duplicate): continue
                    j+=1
                outfile.write("%s\t%d\t%d\t%d\t%d\n" % (refnames[refidx],
                                              startloc,
                                              nread.pos,
                                              1000,
                                              j))
                n=0

def median(vect):
    vect.sort()
    x = len(vect)
    if(x%2):
        return((vect[x/2]+vect[(x/2)+1])/2)
    else:
        return(vect[x/2])
            

def main():
    logging.basicConfig(level=10)
    logger = logging.getLogger('CGH')
    parser = optparse.OptionParser(usage="usage: %prog [options] bamfileName")
    parser.add_option('-w','--windowsize',dest='windowsize',type="int",
                      help='Windowsize (bp) for calculation of copy number')
    parser.add_option('-n','--normalbam',dest='normalbam',
                      help='The name of the bamfile for the normal comparison')
    parser.add_option('-o','--outfile',dest='outfile',type="string",
                      help='Output filename, default <stdout>')
    parser.add_option('-l','--loglevel',dest='loglevel',type="int",
                      help='Logging Level, 1-15 with 1 being minimal logging and 15 being everything [10]')
    (opts,args) = parser.parse_args()
    if(opts.loglevel is not None):
        logger.setLevel(opts.loglevel)
    if(opts.normalbam is not None):
        doNormalComparisonCGH(opts,args)
        exit()
    samfile = pysam.Samfile(args[0],'rb')

    lengths = samfile.lengths
    regioncounts = []
    refnames = samfile.references
    outfile=None
    if(opts.outfile is not None):
        outfile=open(opts.outfile,'w')
    else:
        outfile=sys.stdout
    totreads=0
    for ref in xrange(samfile.nreferences):
        for start in xrange(0,lengths[ref],opts.windowsize):
            c=Counter()
            samfile.fetch(refnames[ref],start,start+opts.windowsize,callback=c)
            regcount=RegionalCount(samfile.references[ref],
                                   start,start+opts.windowsize,
                                   c.mCounts)
            regioncounts.append(regcount)
            totreads+=regcount._count
            logger.info(regcount)
            outfile.write("%s\t%d\t%d\t%d\n" % (regcount.chromosome,
                                                  regcount.rbeg,
                                                  regcount.rend,
                                                  regcount._count))
    samfile.close()
    logger.info('Total Reads: %d',totreads)
    
main()
