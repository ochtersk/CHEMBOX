import copy
from pprint import pformat
#from py_expression_eval import Parser
import CHEMBOX.chemplates.Chemplate as CP
import CHEMBOX.chemplates.DataGenerators as DG

""" These are functions that do utility work using Chemplates.
"""

def create_Chemplate_from_sources(sources, overrides=None, values=None):
    """ create_Chemplate_from_sources - create a Chemplate (var) with
              information from given sources and overrides


        Synopsis
        --------
        var = create_Chemplate_from_sources(sources, overrides, values)
            sources : a ChemPlate with variable names as keys and
                a dictionary with DataGenerators as keys and arguments for
                the DataGenerator as values
            overrides : similar to sources, but values in this dictionary replace
                those in sources with matching keys, allowing for override of
                default values in sources.
            values : a Chemplate or a dictionary of values that get passed into generators that
                need information other than from sources (if use_values == True)
            var : a Chemplate, which is a Python dictionary of dictionaries.
                Each key is a the variable name and the value is a dictionary
                with the DataGenerator name as a key and the value is a
                dictionary of results from the DataGenerator
        Raises
        --------
        AssertionError if the DataGenerator does not exist in DataGenerators

    """
    #make local copies, so there are no accidental changes to the original when we override
    verbose = False
    temp=CP.Chemplate(DoD={})
    if verbose: print("\nSOURCES:",sources,"\nOVER:",overrides,"\nVALt:",type(values))
    if values is None:
        values = {}
    elif isinstance(values,CP.Chemplate):
        values = values.asdict()
    else:
        assert isinstance(values,dict) ,"create_Chemplate_from_sources: values parameter must be Chemplate or dict"

    if overrides is None:
        overrides = CP.Chemplate(DoD= {})
    if verbose: print()
    if verbose: print("sources:",pformat(sources))
    if verbose: print("overrides:",pformat(overrides))
    if verbose: print("values:",pformat(values))
    locSrc = copy.deepcopy(sources)
    locSrc.updateWith(overrides)
    locVar=CP.Chemplate()
    if verbose: print("locSrc:",pformat(locSrc))
    ids = locSrc.getIDs()
    for id in ids:
        gen = locSrc.getID(ID=id)
        if verbose: print("gen:",type(gen),"  -->",pformat(gen))
        assert isinstance(gen, dict)
        for (generator, args) in gen.items():
            if verbose: print("args:",type(args),"  -->",pformat(args))
            assert isinstance(args,dict),"create_Chemplate_from_sources:Datagenerator args must be dict"
            if "use_values" in args and args["use_values"]== "true":
                args.update({"vars":values})
                res = _dispatch(generator, args)
            else:
                res = _dispatch(generator, args)
            locVar.setID(ID=id, dict=res)
    if verbose: print("locVar:",pformat(locVar))
    return locVar

def _dispatch(generator, config, *args):
    verbose = False
    if verbose: print("gen:",pformat(generator))
    if verbose: print("config:",pformat(config))
    try:
        func = getattr(DG, generator)
    except AttributeError:
        assert 1==0, "no such DataGenerator:"+generator
    else:
        result = func(config,*args)
    return result
