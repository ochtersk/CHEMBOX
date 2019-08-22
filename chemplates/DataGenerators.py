import refdata.DataValue as DV
import sigfig.createsf as SF
from pprint import pformat
"""
These are the various data generators for ChemplateUtils.
"""

def randomValue(repl=None):
    """generate a random DataValue

    Parameters
    ----------
    replace : dictionary
        a dictionary containing any defaults which shoud be replaces/updated.

    Returns
    -------
    a DataValue with the units specified, if any

    Raises
    ------
    AttributeError
        if no attribute, value pair or dict is specified.

    """
    verbose = False
    config = {'type' : 'range',
                'range' : {'low': 0.01, 'high': 10},
                'approx' : {'target' : 10, 'pct': 10},
                'exact' : '',
                'nsf_range' : [3,5],
                'units' : '',
               }
    if verbose: print("repl:",pformat(repl))
    if repl is not None:
        config.update(repl)
        if verbose: print("updating:")
    if verbose: print("randomValue config:",pformat(config))
    if config['type'] == 'range':
        mag = SF.SciSigFig.in_range(config['range']['low'],config['range']['high'],config['nsf_range'])
    elif config['type'] == 'approx':
        mag = SF.SciSigFig.approximate_magnitude(config['approx']['target'],config['approx']['pct'])
    elif (config['type'] == 'exact'):
        numberstr = config['exact']
        assert float(numberstr), f"value for exact ({numberstr}) is not a number"
        mag = SF.SciSigFig(str(numberstr))
    else:
        assert False, f"config.type \"{config['type']}\" is not 'range'|'approx'"
    datavalue = DV.DataValue(magnitude=str(mag), units=config['units'])
    if verbose: print("randomValue return:",pformat(datavalue))
    return {'value' : datavalue}
