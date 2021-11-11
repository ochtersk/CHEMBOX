from pprint import pformat
from CHEMBOX.refdata import ureg, Q_
import CHEMBOX.refdata.DataValue as DV
import CHEMBOX.sigfig.createsf as SF

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
    finalunits: the units to convert to

    Returns
    -------
    a DataValue with the units specified in final units

    Raises
    ------
    xAttributeError
        xif no attribute, value pair or dict is specified.

    """
    # put the conversion factors in the right place
    # the destination units should be in convfactorDV[1] and the starting units in
    # convfactorDV[0]
    verbose = True


    resultDV = inputDV.quantity.to(finalunits)

    return resultDV
