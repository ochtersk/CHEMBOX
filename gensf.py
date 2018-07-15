from sigfig.createsf import *
from random import *

qlist = []
ztypes = [None,"","M","T","MT",]
lztypes =["L","LM","LT","LMT"]
for i in ztypes:
    number = SciSigFig.generate(ztypes=i,notation="scientific")
    qlist.append((number,i))
ztypes.extend(lztypes)
for i in ztypes:
    number = SciSigFig.generate(ztypes=i,notation="regular")
    qlist.append((number,i))

qlist = []
exp1 = randint(1,6)
number = SciSigFig.generate(ztypes='T',notation="regular",exp_range=(exp1,exp1),nsf_range=(exp1+1,exp1+1))
qlist.append((number,'Tdec'+ str(exp1) + " " + str(exp1+1)))
exp1 = randint(2,6)
nsf = exp1 - randint(1,exp1-1)
number = SciSigFig.generate(ztypes='N',notation="regular",exp_range=(exp1,exp1),nsf_range=(nsf,nsf))
qlist.append((number,'======>>>>> not Tdec exp:'+ str(exp1) + " nsf:" + str(nsf)))

shuffle(qlist)
for i in qlist:
    print(i[0]+" "+str(i[1]))
