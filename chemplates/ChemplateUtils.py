import copy
from pprint import pformat
#from py_expression_eval import Parser
import CHEMBOX.chemplates.Chemplate as CP
import CHEMBOX.chemplates.DataGenerators as DG

""" These are functions that do utility work using Chemplates.
"""

def create_Chemplate_from_sources(sources, overrides, vals_dict=None):
    """ create_Chemplate_from_sources - create a Chemplate (var) with
              information from given sources and overrides


        Synopsis
        --------
        var = create_Chemplate_from_sources(sources, overrides, vals_dict)
            sources : a ChemPlate with variable names as keys and
                a dictionary with DataGenerators as keys and arguments for
                the DataGenerator as values
            overrides : similar to sources, but values in this dictionary replace
                those in sources with matching keys, allowing for override of
                default values in sources.
            vals_dict : a dictionary of values that get passed into generators that
                need information other than from sources (if use_vals_dict == True)
            var : a Chemplate, which is a Python dictionary of dictionaries.
                Each key is a the variable name and the value is a dictionary
                with the DataGenerator name as a key and the value is a
                dictionary of results from the DataGenerator
        Raises
        --------
        AssertionError if the DataGenerator does not exist in DataGenerators

    """
    #make local copies, so there are no accidental changes to the original when we override
    verbose = True
    if vals_dict is None:
        vals_dict = {}
    if verbose: print()
    if verbose: print("sources:",pformat(sources))
    if verbose: print("overrides:",pformat(overrides))
    if verbose: print("vals_dict:",pformat(vals_dict))
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
            assert isinstance(args,dict),"create_Chemplate_from_sources:Datagenerator args must be dict"
            if "use_vals_dict" in args and args["use_vals_dict"]== "true":
                res = _dispatch(generator, args, vals_dict )
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

def assignvals(map=None,resultsCP=None):
        """ assignvals - remap the results of fillvars to a dictionary where the
                         keys are variable names and the values are values from
                         the DataGenerator
            Synopsis
            --------
            vals = assignvals(map=map, results=results)
                map : a dictionary with variable names as keys, and a list of ID,attr pairs
                      to get the information from a Chemplate
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

def fillansweritem(answer_template_item,vars):
    """ fillansweritem - takes an answer templates and fills it with
                         vars, and returns the filled answer template
        Synopsis
        --------
            vars : a dictionary of variables to fill in and their associated values.
            answer_template: an answer_template is a dictionary with the following
                         keys (those currently used have asterisks. The others
                         are currently ignored):
                'value'* : the equation to get the answer, which is parsed and evaluated
                'units' : units desired for the answer
                'text'* : text to be rendered as a jinja2 template. It could explain
                          the answer with variable values filled in
                'correct' : a boolean flag tell in this answer is correct.
                'reason' : A text reason explaining answers,
                'partials' : intermediate values in calulations
        Example answer_template:
        answer_template_1 = {
            "value" : { "parse_expression":{ "expression":"mass/density", "use_vals_dict":true}},
            "units" : {"copy_text":{"text": "g/mL"}},
            "text" :  {"fill_template":{ "template":"mass/volume = ({{mass}})/{{volume}} = {{value}}", "use_vals_dict":true}},
            "correct" : "true",
            "reason" : {"copy_text":{"text":"To be implemented"}},
            #'partials' : [{"parse_expression":{ "expression":"2.00*mass", "use_vals_dict":"rue"}},
            #              {{"parse_expression":{ "expression":"0.0500*mass", "use_vals_dict":"true"}},}
            #             ]
        }
        Raises
        --------
        AssertionError

    """
    filled_template = create_Chemplate_from_sources(answer_template, None, vals_dict=vars)
