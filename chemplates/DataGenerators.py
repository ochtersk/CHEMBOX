from pprint import pformat
from copy import deepcopy
from functools import wraps
from py_expression_eval import Parser
from jinja2 import Template
import refdata.DataValue as DV
import sigfig.createsf as SF
import chemplates.unit_conversion_utils as UCU


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
    if verbose: print("VERBOSE in DG.validate_args")
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
                if verbose: print(f"arg {arg} value is dict : {func_valid_args[arg]}") # compare subargs
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
            'units_format' : '',
        })
def random_value(repl=None):
    """generate a random DataValue

    Parameters
    ----------
    type (str): context for generating random number 'range'|'approx'|'exact' default: range,
    range (dict): numerical range for range context default: {'low': 0.01, 'high': 10.0},
    approx (dict): target and variance for approximate random number default: {'target' : 9.99999, 'pct': 10.0},
    exact (str): magnitude to use for an exact number no default,
    nsf_range (list): number of sig figs to create result with, default:[3,5],
    units (str) :string to use for units, default: ''
    units_format (str): how to format the units, 'abbrev' and/or 'HTML', default: '',

    Returns
    -------
    a DataValue with the units specified, if any

    Raises
    ------
    AttributeError
        if no attribute, value pair or dict is specified.

    """
    verbose = True
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
    if config['units'] == '':
        use_units = None
    else:
        use_units = config['units']
    use_format = config['units_format']
    datavalue = DV.DataValue(magnitude=str(mag), units=use_units, units_format = use_format)
    if verbose: print("randomValue return:",pformat(datavalue))
    return {'value' : datavalue}


@set_valid_args_and_register({"expression":"",
            "vars": {}})
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
    return {'value' : DV.DataValue(result)}

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


@set_valid_args_and_register({
    "setcollection":"",
    "setname":"",
        })
def get_named_set(args):
    """get a named set of information

    Parameters
    ----------
        setcollection (required str): which collection to get the set from,
        setname (required str): which set to get from that collection,


    Returns
    -------
    the specified set of strings

    Raises
    ------
    AttributeError
        if no attribute, value pair or dict is specified.

    """
    verbose = False
    setcollection = args["setcollection"]
    setname = args["setname"]
    resultset=set()
    resultset = UCU.get_units_set(type=setcollection,set_label=setname)
    return {"value":resultset}

@set_valid_args_and_register({
    "n":"",
    "setvalues":"",
    "vars":{},
        })
def choose_n_from_set(args):
    verbose = False
    setvalues = args["setvalues"]
    vars = args["vars"]
    if verbose: print(">>>setvarname:",pformat(setvalues))
    if verbose: print(">>>vars choose n:",pformat(vars))
    if verbose: print(">>>setvalues:",pformat(vars[setvalues]))
    n_to_get = args["n"]
    tempvals = set(vars[setvalues])
    results_list=[]
    for i in range(n_to_get):
        results_list.append(tempvals.pop())
    return {"value":results_list}


@set_valid_args_and_register({
    "from":"",
    "to":"",
    "vars":{},
        })
def get_conversion_factor(args):
    verbose = False
    from_template = args["from"]
    to_template = args["to"]
    vars = args["vars"]
    if verbose: print(">>>from::",pformat(from_template))
    if verbose: print(">>>to:",pformat(to_template))
    if verbose: print(">>>vars:",pformat(vars))
    from_t = Template(from_template)
    from_units = from_t.render(vars)
    to_t = Template(to_template)
    to_units = to_t.render(vars)
    conv_factor = UCU.get_conversion_factor(from_units,to_units)
    if verbose: print(">>>conv_factor:",pformat(conv_factor),from_units,to_units)
    return {"value":conv_factor}

@set_valid_args_and_register({
    "setA":"",
    "setB":"",
        })
def permute_sets(args):
    """create a permutation of two sets - the result is a set of strings from
        set A catenated with stringgs from set B

    Parameters
    ----------
        setA (required set of str): set of strings for the first part of the catenation
        setB (required set of str): set of strings for the second part of the catenation

    Returns
    -------
    a set of strings

    Raises
    ------
    AttributeError
        if no attribute, value pair or dict is specified.

    """
    verbose = False
    setAname = args["setA"]
    setBname = args["setB"]
    vars = args["vars"]
    if verbose: print(f"permute_sets {setAname =} {setBname =}")
    if verbose: print(">>>vars:",pformat(vars))
    resultset=set()
    for a in vars[setAname]:
        for b in vars[setBname]:
            resultset.add(f"{a}{b}")
    return {"value":resultset}
