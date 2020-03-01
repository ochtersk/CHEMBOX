import refdata.DataValue as DV
import sigfig.createsf as SF
from pprint import pformat
from py_expression_eval import Parser
from jinja2 import Template

"""
These are the various data generators for ChemplateUtils.
"""

def random_value(repl=None):
    """generate a random DataValue

    Parameters
    ----------
    replace : dictionary
        a dictionary containing any defaults which shoud be replaced/updated.

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


def parse_expression(args,vars):
    """generate data from a parsed expression

    Parameters
    ----------
    expression = an expression to parse
    vars :  Each key is a the variable name and the
            value is a DataValue to use in the expression

    Returns
    -------
    a DataValue which is the result of the expression

    Raises
    ------
    AttributeError
        if no attribute, value pair or dict is specified.

    """
    verbose = False
#make this more robust and test it XXX
    expression = args["expression"]
    if verbose: print("expression:",pformat(expression),"\nvars:",pformat(vars))

    parser = Parser()
    result = parser.parse(expression).evaluate(vars)
    return {'value' : result}

def fill_template(template,vars):
    """fill a template

    Parameters
    ----------
    template = an Jinja2 template to fill
    vars :  Each key is a the variable name and the
            value is a DataValue to use in the expression

    Returns
    -------
    the filled template

    Raises
    ------
    AttributeError
        if no attribute, value pair or dict is specified.

    """
    verbose = False
    jt = Template(template)
    result = jt.render(vars)
    return result

def copy_text(text):
    """copy and return argument

    Parameters
    ----------
    text = text to copy

    Returns
    -------
    the argument

    Raises
    ------
    AttributeError
        if no attribute, value pair or dict is specified.

    """
    result = text
    return result
