from pprint import pformat
from CHEMBOX.refdata import ureg, Q_
import CHEMBOX.refdata.DataValue as DV
import CHEMBOX.sigfig.createsf as SF
import CHEMBOX.chemplates.units_sets as UNIT_SETS

def create_conversion(PintDefinition):
    """create_conversion creates a units conversion
            Note: most useful conversions already exist this is meant to make
            dummy conversions

    Parameters
    ----------
    PintDefinition: a Pint string to make into a conversion factor


    Returns
    -------
    nothing right now

    Raises
    ------
    xAttributeError
        xif no attribute, value pair or dict is specified.

    """
    # put the conversion factors in the right place
    # the destination units should be in convfactorDV[1] and the starting units in
    # convfactorDV[0]
    verbose = True

    ureg.define(PintDefinition)

    return ureg


def do_convert(inputDV,finalunits):
    """do_convert calculate a units conversion

    Parameters
    ----------
    inputDV : a DataValue to be converted to different units
    finalunits: a string representing the units to convert to

    Returns
    -------
    a DataValue with the units specified in final units

    Raises
    ------
    pint.errors.DimensionalityError
        if there's no way to convert the units

    """
    verbose = True
    resultDV = inputDV.quantity.to(finalunits)
    return resultDV

def get_conversion_factor(input_units,output_units):
    """get_conversion_factor determine the conversion factor between units

    Parameters
    ----------
    input_units : a string representing the units to convert from
    output_units: a string representing the units to convert to

    Returns
    -------
    a DataValue with the units conversion factor (1 in_unit = xx out_units)

    Raises
    ------

    """
    inputDV=DV.DataValue(" ".join(("1.0",input_units)))
    resultDV = do_convert(inputDV,output_units)
    return resultDV


def get_metric_prefix_set(set_label=None, abbreviations="YES"):
    """get_metric_prefix_set get a set of metric prefixes to convert from/to

    Parameters
    ----------
    set_label 3-3|15-15|24-24 to get sets of metric prefixes ("3-3"=10^3- to 10^-3, etc)
    abbreviations YES to return just abbreviations (default), NO for full prefix, BOTH returns both

    Returns
    -------
    a set of strings which can be used as metric prefixes

    Raises
    ------

    """
    prefix_set =set();
    if (set_label) in UNIT_SETS.prefixes:
        if abbreviations == "YES":
            prefix_set = set(UNIT_SETS.prefixes[set_label].values())
        elif abbreviations == "NO":
            prefix_set = set(UNIT_SETS.prefixes[set_label].keys())
        else:

            prefix_set = set(UNIT_SETS.prefixes[set_label].keys()).union(\
                         set(UNIT_SETS.prefixes[set_label].values()))
    else:
        raise KeyError(f"key {set_label} does not exist in prefixes")
    return prefix_set

def get_units_set():
    """get_units_set get a set of units to convert from/to

    Parameters
    ----------
    dimensionality : (optional) dimensionality of units
    compatible_with : (optional) units to make the set compatible with
    use_metric : (optional) BASIC|EXTENDED|ALL to include sets of metric prefixes
    SI_only : (optional) use only SI units
    predefined_set : (optional) the name of a predefined set of

    Returns
    -------
    a set of strings which can be used as units

    Raises
    ------

    """
    pass
