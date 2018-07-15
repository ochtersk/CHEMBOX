from sigfig.createsf import *
from random import *

qlist = []
ztypes = [None,"","M","T","MT",]
ztypes = ["",]
lztypes =["L","LM","LT","LMT"]
for i in ztypes:
    number = SciSigFig.generate(ztypes=i,notation="regular")
    qlist.append(number)
    number = SciSigFig.generate(ztypes=i,notation="scientific")
    qlist.append(number)

for i in qlist:
    print("N:",i)
    j = SciSigFig(i)
    #j.round_digpos(2)
    j.round_numdig(3)
    print("repr j:",repr(j))
    print("----------\n")
