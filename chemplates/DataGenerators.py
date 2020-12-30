from pprint import pformat
from copy import deepcopy
from functools import wraps
from py_expression_eval import Parser
from jinja2 import Template
import CHEMBOX.refdata.DataValue as DV
import CHEMBOX.sigfig.createsf as SF


# known gnerators keeps a dict of known generators, where teh name of the
# generator is the key and the generator itself is the value.
known_generators = {}
# create a decorator which accept args to set the dict of valid
# arguments to the generator, and also to register the generator into known_generators.
def set_valid_args_and_register(valid_args):
    def decorator(func):
        @wraps(func)
        def generator(*args, **kwargs):
            # only use a wrapper if you need extra code to be run here
            return func(*args, **kwargs)
        generator.valid_args = valid_args
        known_generators[generator.__name__] = generator
        return generator
    return decorator

def validate_args(DoD):
    verbose = False
    error_list = []
    for funcname, argsdict in DoD.items():
        if verbose: print("FN:",funcname," ARGS:", pformat(argsdict))
        if funcname not in known_generators:
            error_list.append(f" unknown generator ({funcname})")
            continue
        func = known_generators[funcname]
        func_valid_args = func.valid_args
        if verbose: print("KNOWNFN:",funcname," ARGS:", pformat(func_valid_args))
        for arg, value in argsdict.items():
            if arg not in func_valid_args:
                error_list.append(f" supplied arg ({arg}) is not valid."
                    f"valid: {func_valid_args.keys()}")
                continue
            if isinstance(value, dict):
                if verbose: print(f"arg {arg} value is dict ") # compare subargs
                if len(func_valid_args[arg].keys())>0: # empty dict means don't check args
                    for subarg, subvalue in value.items():
                        if verbose: print(f"     subarg {subarg} value is {subvalue} ") # compare subargs

                        if subarg not in func_valid_args[arg]:
                            error_list.append(f" supplied subarg ({subarg}) to arg ({arg}) is not valid."
                                f"valid args: {func_valid_args[arg].keys()}")
                            continue
                        if type(subvalue) != type(func_valid_args[arg][subarg]):
                            error_list.append(f"TypeError for argument {subarg}; wanted:{type(func_valid_args[arg][subarg])} got:{type(subvalue)}")
                            continue
            else:
                if (type(value) != type(func_valid_args[arg])):
                    error_list.append(f"TypeError for argument {arg}; wanted:{type(func_valid_args[arg])} got:{type(value)}")
                    continue

    return error_list

"""
These are the various data generators for ChemplateUtils.
"""


@set_valid_args_and_register({'type' : 'range',
            'range' : {'low': 0.01, 'high': 10.0},
            'approx' : {'target' : 9.99999, 'pct': 10.0},
            'exact' : '',
            'nsf_range' : [3,5],
            'units' : '',
        })
def random_value(repl=None):
    """generate a random DataValue

    Parameters
    ----------
    repl : dictionary
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
    config = deepcopy(random_value.valid_args)
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


@set_valid_args_and_register({"expression":"",
            "vars": ""})
def parse_expression(args):
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
    vars = args["vars"]
    if verbose: print("expression:",pformat(expression),"\nvars:",pformat(vars))

    parser = Parser()
    result = parser.parse(expression).evaluate(vars)
    return {'value' : result}

@set_valid_args_and_register({"template":"",
            "vars":{}    })
def fill_template(args):
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
    template = args["template"]
    vars = args["vars"]
    if verbose: print("fill_template:",pformat(template),"\nvars:",pformat(vars))
    jt = Template(template)
    result = jt.render(vars)
    if verbose: print("fill_template result:",str(result))
    return {"value":result}

@set_valid_args_and_register({"text":"",
        })
def copy_text(args):
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
    verbose = False
    text = args["text"]
    result = text
    return {"value":result}
