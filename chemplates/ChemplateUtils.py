import copy
from pprint import pformat
from py_expression_eval import Parser
from jinja2 import Template
import chemplates.Chemplate as CP
import chemplates.DataGenerators as DG

""" These are functions that do utility work using Chemplates.
"""

def fillvar(sources, overrides):
    """ fillvar - fill a Chemplate (var) with information, given sources and overrides
        Synopsis
        --------
        var = fillvar(sources, overrides)
            sources : a ChemPlate with variable names as keys and
                a dictionary with DataGenerators as keys and arguments for
                the DataGenerator as values
            overrides : similar to sources, but values in this dictionary replace
                those in sources with matching keys, allowing for override of
                default values in sources.
            var : a Python dictionary. Each key is a the variable name and the
                value is a dictionatry with the DataGenerator name as a key and
                the value is a dictionary of results from the DataGenerator
        Raises
        --------
        AssertionError if the DataGenerator does not exits in DataGenerators

    """
    #make local copies, so there are no accidetal changes to the original when we override
    verbose = False
    if verbose: print()
    if verbose: print("sources:",pformat(sources))
    if verbose: print("overrides:",pformat(overrides))
    locSrc = copy.deepcopy(sources)
    locSrc.updateWith(overrides)
    locVar=CP.Chemplate()
    if verbose: print("locSrc:",pformat(locSrc))
    ids = locSrc.getIDs()
    for id in ids:
        gen = locSrc.getID(ID=id)
        for (generator, args) in gen.items():
            res = _dispatch(generator, args)
            locVar.setID(ID=id, dict=res)
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

def assignvals(map=None,resultsCP=None):
        """ assignvals - remap the results of fillvars to a dictionary where the
                         keys are variable names and the values are values from
                         the DataGenerator
            Synopsis
            --------
            vals = assignvals(map=map, results=results)
                map : a dictionary with variable names as keys, and a list of ID,attr pairs
                      to get the infromation from a Chemplate
                results : a Chemplate from fillvars that has the results stored in it
            Raises
            --------
            AssertionError

        """
        verbose = False
        valdict={}
        for var in map:
            (ID,attr)=map[var]
            if verbose: print("var:",var,"ID:",ID,"attr:",attr)
            valdict[var]=resultsCP.getIDattr(ID,attr)
        return valdict

def fillanswerlist(answer_template_list,vars):
    parser = Parser()
    answer_list =[]
    for template in answer_template_list:
        filled = {}
        if 'value' in template:
            filled['value'] = parser.parse(template['value']).evaluate(vars)
            vars['value'] = filled['value'] # now we can use it in other places
        else:
            assert value in templates
        if 'text' in template:
            jt = Template(template['text'])
            filled['text'] = jt.render(vars)
        answer_list.append(filled)
    return answer_list
