from pint import UnitRegistry
import pprint

pp = pprint.PrettyPrinter(indent=4)
ureg = UnitRegistry()
can_convert_among=dict()
for i in ureg:
    try:
        dimensionality = ureg.get_dimensionality(i)
    except:
        dimensionality = "no dims?"
    can_convert_among.setdefault(str(dimensionality),[]).append(i)
#for ele in range(int(val), int(val) + 2):
#        myDict.setdefault(ele, []).append(val)
    #print("adding:",dimensionality, i)

for dim in can_convert_among.keys():
    print("DIM:",dim)
    pp.pprint(can_convert_among[dim])
