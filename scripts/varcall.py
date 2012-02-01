import pysam
import heapq

class Locus(object):
    def __init__(self,pileupCol):
        self.pos=pileupCol.pos
        self.n=pileupCol.n
        counts = {}
        mapq=0
        for read in pileupCol.pileups:
            val = read.alignment.seq[read.qpos]
            if(counts.has_key(val)):
                counts[val]+=1
            else:
                counts[val]=1
            mapq += read.alignment.mapq
        self.mapq = float(mapq)/self.n
        self.counts=counts
        if(len(counts)>1):
            self.is_variant=True
        else:
            self.is_variant=False

    def __str__(self):
        return "%d %d %s" % (self.pos,self.n,self.counts)

tumorfile = pysam.Samfile('/data/sedavis/sequencing/TargetOsteosarcoma/fastq2/bam/PALFYN_Tumor.md.recal.realigned.bam','rb')
normalfile = pysam.Samfile('/data/sedavis/sequencing/TargetOsteosarcoma/fastq2/bam/PALFYN_Normal.md.recal.realigned.bam','rb')

pileup = normalfile.pileup()

class PairedPileup(object):
    def __init__(self,nfile,tfile):
        np = ((x.tid,x.pos,'n',Locus(x)) for x in nfile.pileup())
        tp = ((x.tid,x.pos,'t',Locus(x)) for x in tfile.pileup())
        self.merged = heapq.merge(tp,np)
        self.current = self.merged.next()

    def __iter__(self):
        return self

    def next(self):
        x = self.merged.next()
        while((self.current[0]!=x[0]) or (self.current[1]!=x[1])):
            if((x[0]>self.current[0]) or (x[1]>self.current[1])):
                self.current=self.merged.next()
            x=self.merged.next()
        y = self.current
        self.current=self.merged.next()
        return (y,x)


y = PairedPileup(normalfile,tumorfile)
for z in y:
    print z[0][0],z[0][1],z[0][3].counts,z[1][3].counts


j=0
t = []
for pc in pileup:
    j+=1
    x = Locus(pc)
    if(x.is_variant):
        if(x.n>20):
            vals = sorted([v for v in x.counts.values()])
            x.vals=vals
            if(vals[-2]>3):
                t.append(x)
                print x.pos,x.n,float(x.vals[-2])/(vals[-2]+vals[-1]),x.vals,x.mapq
    if((j % 100000)==0):
        print j,x.pos,len(t)


