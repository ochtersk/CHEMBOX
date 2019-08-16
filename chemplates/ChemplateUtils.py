import copy
import chemplates.Chemplate as CP

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
    locSources = copy.deepcopy(sources)
    locSources.update(overrides)
    locVar={}
    for id in locSources.getkeys():
        locVar(id) = _dispatch(id, locSources)
    return locVar

def _dispatch(generator, config):
    
