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
    verbose = False

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
    verbose = False
    result = inputDV.quantity.to(finalunits)
    resultDV = DV.DataValue(result.magnitude,result.units)
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
    inputDV=DV.DataValue(" ".join(("1",input_units)), exact=True)
    resultDV = do_convert(inputDV,output_units)
    #print("get_conversion_factor::",pformat(resultDV))
    return resultDV


def _get_units_sets_set(type=None,set_label=None):
    """_get_units_sets_set get a set of from units_sets.py

    Parameters
    ----------
    type = SI|prefixes
    set_label = a key for the

    Returns
    -------
    a set of strings which can be used for prefixes or units

    Raises
    ------

    """
    verbose = False
    return_set =set();
    if (set_label) in UNIT_SETS.units_sets[type]:
        if verbose: print(f"{type =} {set_label =} = {UNIT_SETS.units_sets[type] =}")
        return_set = set(UNIT_SETS.units_sets[type][set_label])
        if verbose: print(f"from: _get_units_sets_set {type =} {set_label =} {return_set =}")
    else:
        raise KeyError(f"key {set_label} does not exist in {units_sets[type]}")
    return return_set

def get_metric_prefix_set(set_label=None):
    """get_metric_prefix_set get a set of metric prefixes to convert from/to

    Parameters
    ----------
    set_label 3-3|15-15|24-24 to get sets of metric prefixes ("3-3"=10^3- to 10^-3, etc)

    Returns
    -------
    a set of strings which can be used as metric prefixes

    Raises
    ------

    """
    type="prefixes"
    return _get_units_sets_set(type,set_label)

def _get_matching_dimensionality(dimensionality=None,compatible_with=None):
    units_set = set()
    to_match = ""
    if compatible_with is not None:
        try:
            to_match = ureg.get_dimensionality(compatible_with)
        except:
            pass
    elif dimensionality is not None:
        to_match = dimensionality
    else:
        raise Exception(f"Either dimensionality or compatible_with must be specified")
    for i in ureg:
        try:
            i_dimensionality = ureg.get_dimensionality(i)
            #print(f"i:{i} dim:{i_dimensionality}")
        except:
            i_dimensionality = "no dims?"
        if i_dimensionality == to_match:
            units_set.add(i)
    #print("with dimensionality:",pformat(units_set))
    return units_set


def get_units_set(dimensionality=None, metric_prefixes=None,set_label=None):
    """get_units_set get a set of units to convert from/to

    Parameters
    ----------
    dimensionality : (optional) dimensionality of units
    compatible_with : (optional) units to make the set compatible with
    set_label : (optional) the name of a predefined set of units

    Returns
    -------
    a set of strings which can be used as units

    Raises
    ------

    """
    verbose = False
    if metric_prefixes is not None:
        prefixes = get_metric_prefix_set(metric_prefixes)
        unit_set = _get_units_sets_set("units",set_label)
        if verbose: print(f"{metric_prefixes =}{prefixes =}\n{set_label =} {unit_set =}")
        unit = unit_set.pop()
        metric_set = set()
        for pref in prefixes:
            metric_set.add(f"{pref}{unit}")
        return metric_set
    if set_label is not None:
        type="units"
        return _get_units_sets_set(type,set_label)
    if dimensionality is not None:

        units_set = _get_matching_dimensionality(dimensionality=dimensionality)
        #print("with dimensionality:",pformat(units_set))
        return units_set


def create_conversion_parameters(unit_set):
    """create_conversion_parameters - create a set of conversion parmeters from a given unit set

    Parameters
    ----------
    unit_set a set of strings

    Returns
    -------
    a tuple of two strings and a DataValue. The strings are from the set to use as
        input and output units, and the DataValue is a conversion factor between the units

    Raises
    ------

    """
    input_units =  unit_set.pop()
    output_units = unit_set.pop()
    conversion_factor = get_conversion_factor(input_units,output_units)
    return(input_units,output_units,conversion_factor)
