from collections import Counter
import sigfig.createsf as SF
import refdata.DataUnits as DU

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
        if units is None:
            if magnitude is not None:
                if ' ' in magnitude:
                    (magnitude,units) = magnitude.split(sep=None)
                else:
                    units = ''
            else:
                units = ''
        if magnitude is None:
            magnitude = "0.0"
        self.magnitude = SF.SciSigFig(magnitude)
        self.units = DU.DataUnits(units, unitsformat)

    def __str__(self):
        mag = str(self.magnitude)
        units = str(self.units)
        #no trailing space if no units
        return ' '.join(filter(None,[mag,units]))

    def __repr__(self):
        mag = repr(self.magnitude)
        return f'DV.DataValue("{mag}", "{self.units}")'

    def __mul__(self,other):
        mag = self.magnitude*other.magnitude
        units = self.units*other.units
        new = DataValue()
        new.magnitude = mag
        new.units = units
        #print("mul new:",repr(new), "\n mag:",mag)
        return new


    def __truediv__(self,other):
        mag = self.magnitude/other.magnitude
        units = self.units/other.units
        new = DataValue()
        new.magnitude = mag
        new.units = units
        #print("div new:",repr(new), "\n mag:",mag)
        return new

    def __add__(self,other):
        mag = self.magnitude+other.magnitude
        units = self.units+other.units
        new = DataValue()
        new.magnitude = mag
        new.units = units
        #print("add new:",repr(new), "\n mag:",mag)
        return new


    def __sub__(self,other):
        mag = self.magnitude-other.magnitude
        units = self.units-other.units
        new = DataValue()
        new.magnitude = mag
        new.units = units
        #print("sub new:",repr(new), "\n mag:",mag)
        return new
