from collections import Counter
from pprint import pformat

class DataUnits():
    """
    A class used to represent Units for DataValue calculations

    Attributes
    ----------
    units : a list of 2 lists
        the first list is a list of strings representing numerator units
        the second list is a list of strings representing denominator units

    Public Methods
    -------
    __mul__(other)-> DataUnits
        Multiplies units in self by units in other, cancelling as needed
    __truediv__(other)-> DataUnits
        Divides units in self by units in other, cancelling as needed
    __add__(other)-> DataUnits
    __sub__(other)-> DataUnits
        Simply checks whether units are the same in self and other, raises an
          AssertionError if not.
    __str__-> str
        Returns a string rep of the units, numerator adn denominator. If the
          DataUnits was created with unitsformat="expanded", then all the unists
          are explicitly listed, otherwise exponeted are used (ex: sec^2)

    """
    def __init__(self, units, unitsformat = 'expanded'):
        """Create a DataUnits object from a string

        Parameters
        ----------
        units: str
        a string representing the desired units
            numerator and denominator are separated by "/"
            units within the numerator or denominator are separated by "*", and
            can be either in exponetial "m^2" or expanded "m*m" notation

        unitsformat: str
        If the argument `unitsformat` isn't passed in, the default exponential
        representation is used (ex: "kg*m/sec^2") is used.
        If unitsformat is set to expanded, and expanded notation is used:
        (ex: "kg *m/sec*sec")

        Raises
        ------
        AttributeError
            if something other than a string is passed in.

        """
        numerator_str,_,denominator_str = units.partition("/")
        self.unitsformat = unitsformat
        self.units=[]
        for i in (numerator_str, denominator_str):
            unexpanded = i.split("*")
            splitted = [(unit.split("^")) for unit in unexpanded]
            expanded = [x if len(x)==1 else int(x[1])*[x[0]] for x in splitted  ]
            final = [x for row in expanded for x in row]
            final=list(filter(None,final))
            self.units.append(final)
        #print("DU init:",units, "out:",pformat(self.units))

    def _fromLists(numerator,denominator):
        """Create a DataUnits object from 2 lists of units

        This is used internally to create new DataUnits objects

        Parameters
        ----------
        numerator: a list of strings of units
        denominator : a list of strings of units

        """
        new = DataUnits("")
        new.units=[]
        new.units.append(numerator)
        new.units.append(denominator)
        return new

    def __str__(self):
        """Create a string representation of a DataUnits object

        Creates two styles of notation:
            expanded: units with exponents appear multiple times
                example: min^2 = "min*min"
            exponential: repeated units are converted to exponentials
                example: sec*sec = "sec^2"
        Which notation used depends on the unitsformat parameter at creation
        time. Expenential is the default, and probably should be the only, but
        it's there, so I keep it for now.

        There's some fudgy stuff to make the output conform to

        Parameters
        ----------
        None

        """
        verbose = False
        numerator, denominator = self.units
        if verbose: print("In numer:",pformat(numerator), "denom:",pformat(denominator))
        if self.unitsformat == "expanded":
            denominator_str = '*'.join(denominator)
            numerator_str = "*".join(numerator)
            if denominator and not numerator:
                numerator = "1" # 1/denominator_str
        else:
            n_counter = Counter(numerator)
            n_units = [x if n==1 else str(x)+"^"+str(n) for x,n in n_counter.items()]
            d_counter = Counter(denominator)
            d_units = [x if n==1 else str(x)+"^"+str(n) for x,n in d_counter.items()]
            denominator_str = '*'.join(d_units)
            numerator_str = "*".join(n_units)
        if denominator_str == "1":
            denominator_str = ""
        if verbose: print("OUT numer:",numerator_str, "denom:",denominator_str)
        if denominator_str:
            if not numerator_str:
                numerator_str = "1"
            return "/".join([numerator_str,denominator_str])
        else:
            return numerator_str

    def __mul__(self,other):
        """Create a new DataUnits object from self*other. Identical units in
        the numerator and denominator are cancelled.

        Parameters
        ----------
        other: the units to multiply self by.

        """
        numerator = self.units[0].copy()
        denominator = self.units[1].copy()
        other_numerator = other.units[0].copy()
        other_denominator = other.units[1].copy()
        numerator.extend(other_numerator)
        denominator.extend(other_denominator)
        # This bit does the cancelling - it counts the occurences of units in
        # the numerator and denominator and subtracts, leaving only the positive
        # exponents. The same is done on the other side of the fraction, leaving
        # exactly the units we need.
        n=Counter(numerator)
        d=Counter(denominator)
        new_numer = n - d
        numer_elements = sorted(new_numer.elements())
        new_denom = d - n
        denom_elments =  sorted(new_denom.elements())
        new = DataUnits._fromLists(numer_elements,denom_elments)
        return new

    def _reciprocal(self):
        """Create a new DataUnits object from self, which holds the reciprocal
        units

        Parameters
        ----------
        None

        """
        numerator, denominator = self.units
        new = DataUnits._fromLists(denominator,numerator)
        return new

    def __truediv__(self, other):
        """Create a new DataUnits object from self and other which is self/other.
        It is accomplishe dby multiplying by the reciprocal of other.

        Parameters
        ----------
        other: the DataUnits to divide self by.

        """
        new = self*other._reciprocal()
        return new

    def _UnitsEquiv(self,other):
        """Creates a new DataUnits object if the units in both self and other
        are equivalent. This is used for adding and subtracting units.

        Parameters
        ----------
        other: units to compare to

        """
        s_numerator, s_denominator = self.units
        o_numerator, o_denominator = other.units
        assert Counter(s_numerator)==Counter(o_numerator)
        assert Counter(s_denominator)==Counter(o_denominator)
        new = DataUnits._fromLists(s_numerator,s_denominator)
        return new

    def __add__(self,other):
        """Creates a new DataUnits object with the same units as self, if they
        are equivalent to those in other.

        Parameters
        ----------
        other: units to add to

        """
        new = DataUnits._UnitsEquiv(self,other)
        return new

    def __sub__(self,other):
        """Creates a new DataUnits object with the same units as self, if they
        are equivalent to those in other.

        Parameters
        ----------
        other: units to subtract

        """
        new = DataUnits._UnitsEquiv(self,other)
        return new
