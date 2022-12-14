from collections import Counter
from . import ureg, Q_
import sigfig.createsf as SF

class DataValue():
    """DataValue class for ChemBox to hold values and units

    Attributes
    ----------
    quantity = pint Quantity

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
    def __init__(self, magnitude = None , units = None, units_format = '',exact = False ):
        verbose = True
        if verbose: print("----------")
        magnitude_in = magnitude
        units_in = units
        magnitude = None
        units= None
        if verbose: print("DV init params mag rep:",repr(magnitude_in),"units:",units_in)

        if isinstance(magnitude_in,DataValue) and units_in is None:
            if verbose: print("DV.init:DV,None")
            magnitude, units = str(magnitude_in.magnitude), str(magnitude_in.units)
        elif isinstance(magnitude_in,DataValue) and units_in is not None:
            if verbose: print("DV.init:DV,not None")
            magnitude, units = str(magnitude_in.magnitude), str(units_in)
        elif isinstance(magnitude_in,str) and units_in is None:
            if verbose: print("DV.init:str,None")
            if ' ' in magnitude_in:
                (magnitude,units) = magnitude_in.split(sep=None,maxsplit=1)
            else:
                magnitude = magnitude_in
                units = ''
        elif isinstance(magnitude_in,str) and units_in is not None:
            if verbose: print("DV.init:str,not None")
            magnitude = magnitude_in
            units = str(units_in)
        elif magnitude_in is None:
            if verbose: print("DV.init:None")
            magnitude = "0.0"
            units = ""
        else: #handle ints and floats
            if verbose: print("DV.init:"+str(type(magnitude_in))+" only")
            magnitude = str(magnitude_in)
            if units_in is not None:
                units = str(units_in)
            else:
                units =''
        if verbose: print("DV init mag:", magnitude,"units:",units)
        if verbose: print("DV REPR mag:", repr(magnitude),"units:",repr(units))
        assert magnitude is not None
        magnitude_SF = SF.SciSigFig(str(magnitude), exact = exact )
        if verbose: print("DV mag_SF:",magnitude_SF.dump())
        self.quantity=Q_(magnitude_SF,units)
        self.units_format = units_format
        if verbose: print("DV Q_:",self.quantity)
        self.magnitude = magnitude_SF
        # the % inthe next line is Pint - % means don't use the string "dimensionless"
        if verbose: print(f"formatted units:{self.quantity.units:%}")
        if verbose: print(f"formatted type:{type(self.quantity.units)}")
        if verbose: print(f"{self.units_format =}")
        self.units=self.quantity.units


    def __str__(self):
        verbose = True
        str = f"{self.quantity.magnitude}"
        # the % inthe next line is Pint - % means don't use the string "dimensionless"
        pint_format_spec = "%" # don't use "dimensionless"
        if "abbrev" in self.units_format:
            pint_format_spec += "~"
        if "HTML" in self.units_format:
            pint_format_spec += "H"
        units = f"{self.quantity.units:{pint_format_spec}}"
        if verbose: print(f"{pint_format_spec =}      {units =}")
        if units == '':
            return str
        return " ".join([str,units])

    def __repr__(self):
        mag = repr(self.magnitude)
        units = str(self.units)
        return f'DVx.DataValue("{mag}", "{units}")'

    def __mul__(self,other):
        other = DataValue(other)
        mag = self.magnitude*other.magnitude
        units = self.units*other.units
        #print("mul mag:",repr(mag), "\n str:",str(mag))
        #print("mul units:",repr(units), "\n str:",str(units))
        new = DataValue(mag,units)
        #print("mul new:",repr(new), "\n str:",str(new))
        return new

    __rmul__ = __mul__

    def __truediv__(self,other):
        other = DataValue(other)
        #print("\nDIV self:",repr(self),"\nOTHER:",repr(other))
        mag = self.magnitude/other.magnitude
        units = self.units/other.units
        new = DataValue(mag,units)
        return new

    def __add__(self,other):
        other = DataValue(other)
        mag = self.magnitude+other.magnitude
        assert str(self.units)  == str(other.units)
        units = self.units
        new = DataValue(mag,units)
        return new


    def __sub__(self,other):
        verbose = False
        if verbose: print("sub ----")
        other = DataValue(other)
        if verbose: print("sub self",repr(self),"other:",repr(other))
        mag = self.magnitude-other.magnitude
        if verbose: print("sub mag:",repr(mag)," str:",str(mag)," mag:",mag)
        assert str(self.units)  == str(other.units)
        units = self.units
        new = DataValue(mag,units)
        if verbose: print("sub new:",repr(new), "\n mag:",mag)
        return new

    def __float__(self):
        return float(self.magnitude)
