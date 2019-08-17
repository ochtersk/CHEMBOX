import copy
from pprint import pformat
import chemplates.Chemplate as CP
import chemplates.DataGenerators as DG
""" These are functions that do utility work using Chemplates.
"""

def fillvar(sources, overrides):
    """ fillvar - fill a library (var) given sources and overrides
        Synopsis
        --------
        var = fillvar(sources, overrides)
            sources : a dictionary with DataGenerators method names as keys and
                a dictionary arguments for the DataGenerator as values
            overrides : similar to sources, but values in this dictionary replace
                those in sources with matching keys, allowing for override of
                default values in sources.
            var : a Python dictionary. Each key is a DataGenerators method name and
                the value is a dictionary of results from the DataGenerator
    """
    #make local copies, so there are no accidetal changes to the original when we override
    verbose = False
    if verbose: print()
    if verbose: print("sources:",pformat(sources))
    if verbose: print("overrides:",pformat(overrides))
    locSources = copy.deepcopy(sources)
    locSources.update(overrides)
    locVar={}
    if verbose: print("locSources:",pformat(locSources))
    for id in locSources.keys():
        locVar[id] = _dispatch(id, locSources[id])
        if verbose: print("locVarid:",id,pformat(locVar[id]))
    if verbose: print("locVar:",pformat(locVar))
    return locVar

def _dispatch(generator, config):
    verbose = False
    if verbose: print("gen:",pformat(generator))
    if verbose: print("config:",pformat(config))
    try:
        func = getattr(DG, generator)
    except AttributeError:
        assert 1==0, "no such DataGenerator:"+generator
    else:
        result = func(config)
    return result
