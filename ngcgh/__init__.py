class Region(object):
    """A simple region class with chromosome, rbeg (start), and rend (end)"""
    def __init__(self,chromosome,rbeg,rend):
        self.chromosome=chromosome
        self.rbeg=int(rbeg)
        self.rend=int(rend)
