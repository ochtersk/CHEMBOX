from collections import Counter
import CHEMBOX.sigfig.createsf as SF
import CHEMBOX.refdata.DataUnits as DU

class DataValue():
    """DataValue class for ChemBox to hold values and units

    Attributes
    ----------
    magnitude : SciSigFig
        The numerical value
    units : DataUnits
        The units for this value

    Public Methods
    --------------
    __init__ create a new DataValue withthe supplied magnitude and units
    __str__  give a string representation of the DataValue
    __repr__ give a more detailed representation of the DataValue
    __mul__
    __truediv__
    __add__
    __sub__
        do math with two DataValues do the right thing with sig figs and units

    """
    def __init__(self, magnitude = None , units = None, unitsformat = '', ):
        verbose = False
        if verbose: print("DV init params mag rep:",repr(magnitude),"units:",units)
        if isinstance(magnitude,DataValue):
                magnitude, units = str(magnitude.magnitude), str(magnitude.units)
        elif isinstance(magnitude,str) and units is None:
            if ' ' in magnitude:
                (magnitude,units) = magnitude.split(sep=None)
            else:
                units = ''
        elif isinstance(magnitude,str) and units is not None:
            pass
        elif magnitude is None:
            magnitude = "0.0"
            units = ''
        else: #handle ints and floats
            magnitude = magnitude
            units = ''
        if verbose: print("DV init mag:", magnitude,"units:",units)
        self.magnitude = SF.SciSigFig(magnitude)
        self.units = DU.DataUnits(units, unitsformat)

    def __str__(self):
        mag = str(self.magnitude)
        units = str(self.units)
        #no trailing space if no units
        return ' '.join(filter(None,[mag,units]))

    def __repr__(self):
        mag = repr(self.magnitude)
        units = str(self.units)
        return f'DV.DataValue("{mag}", "{units}")'

    def __mul__(self,other):
        other = DataValue(other)
        mag = self.magnitude*other.magnitude
        units = self.units*other.units
        new = DataValue()
        new.magnitude = mag
        new.units = units
        #print("mul new:",repr(new), "\n mag:",mag)
        return new

    __rmul__ = __mul__

    def __truediv__(self,other):
        other = DataValue(other)
        #print("\nDIV self:",repr(self),"\nOTHER:",repr(other))
        mag = self.magnitude/other.magnitude
        units = self.units/other.units
        new = DataValue()
        new.magnitude = mag
        new.units = units
        #print("div new:",repr(new), "\n mag:",mag)

        return new

    def __add__(self,other):
        other = DataValue(other)
        mag = self.magnitude+other.magnitude
        units = self.units+other.units
        new = DataValue()
        new.magnitude = mag
        new.units = units
        #print("add new:",repr(new), "\n mag:",mag)
        return new


    def __sub__(self,other):
        verbose = False
        other = DataValue(other)
        if verbose: print("sub self",repr(self),"other:",repr(other))
        mag = self.magnitude-other.magnitude
        units = self.units-other.units
        new = DataValue()
        new.magnitude = mag
        new.units = units
        if verbose: print("sub new:",repr(new), "\n mag:",mag)
        return new

    def __float__(self):
        return float(self.magnitude)
