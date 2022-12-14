import pytest
from pprint import pformat
import chemplates.DataGenerators as DG
import refdata.DataValue as DV
import re

#print("Known:",pformat(DG.known_generators))
#for name, func in DG.known_generators.items():
#    print(name, func)
#    print(name,pformat(func.valid_args))




def isinrange(val,low,high):
    if (float(val)>=low and float(val) <= high):
        return True
    else:
        print("isinrange:",low,val,high)
    return False


@pytest.mark.parametrize("units", [
    ({'units':"gram",'formatted':'gram', 'units_format':''}),
    ({'units':'', 'formatted':'', 'units_format':'%'}),
    ({'units':"meter / second",'formatted':'meter / second', 'units_format':''}),
    ({'units':"gram", 'formatted':'g', 'units_format':'abbrev'}),
    ({'units':"meter / second",'formatted':'m / s', 'units_format':'abbrev'}),
    ({'units':"meter / second**2",'formatted':'m / s ** 2', 'units_format':'abbrev'}),
    ({'units':"meter / second**2",'formatted':'meter/second<sup>2</sup>', 'units_format':'HTML'}),
    ({'units':"meter / second**2",'formatted':'m/s<sup>2</sup>', 'units_format':'abbrev,HTML'}),
])
@pytest.mark.parametrize("repl,low,high", [
    ({}, 0.01,10),
    ({'range' : {'low': 11.0, 'high': 12.0}}, 11,12),
    ({'type': 'approx','approx' : {'target' : 10, 'pct': 10}}, 9,11),
])
def test_random_value(repl,low,high,units):
    verbose = False
    if verbose: print("\ntestrepl:",pformat(repl))
    x = DG.random_value(repl)
    urepl = repl.copy()
    urepl.update(units)
    if verbose: print("urepl:",pformat(urepl), "units:",pformat(units))
    if verbose: print("test x:",pformat(x))
    assert isinrange(x['value'].magnitude,low,high)
    ux = DG.random_value(urepl)
    assert isinrange(ux['value'].magnitude,low,high)
    val = ux['value']
    strval = str(val)
    just_units = re.sub('^[^ ]+ ?', '', strval )
    if verbose: print(f"{strval =} {just_units =}  {units['formatted'] =}")
    assert just_units == units['formatted']

@pytest.mark.parametrize("number, answerstr", [
    #I use str because I don't want rounding errors in comparison
    ("0.10", "0.10" ),
    ("-200","-2e+2"),
    ("200.","2.00e+2"),
    ("4.003e-10","4.003e-10"),
])
def test_exactnumbers(number,answerstr):
    repl = {'type': 'exact','exact' : number}
    x = DG.random_value(repl)
    assert str(x['value'].magnitude)==answerstr


@pytest.mark.parametrize("expression, vars, answer", [
    #I use str because I don't want rounding errors in comparison
    ("1+2",{},"3" ),
    ("one + two", {'one' : DV.DataValue("1"), 'two': DV.DataValue("2")}, DV.DataValue("3")),
    ("one + two", {'one' : DV.DataValue("1 g"), 'two': DV.DataValue("2 g")}, DV.DataValue("3 gram")),
])
def test_parser(expression, vars, answer ):
    x = DG.parse_expression({"expression":expression, "vars":vars})
    #print("test_parser x:",pformat(x))
    assert str(x["value"]) == str(answer)


@pytest.mark.parametrize("template, vars, answer", [
    ("1+2",{"a" : "1"}, "1+2" ),
    ("1+{{a}}",{"a" : "1"}, "1+1" ),
])
def test_fill_template(template, vars, answer ):
    x = DG.fill_template({"template":template, "vars":vars})
    #print("test_fill_template x:",pformat(x))
    assert str(x["value"]) == str(answer)

@pytest.mark.parametrize("text, answer", [
    ("1+2", "1+2" ),
    ("dog cat chicken", "dog cat chicken" ),
])
def test_copy_text(text, answer ):
    x = DG.copy_text({"text":text})
    #print("test_copy_text x:",pformat(x))
    assert str(x["value"]) == str(answer)


@pytest.mark.parametrize("test_dict, answer", [
    ({"mass" : { "random_value" : {"range" :{"low": 11.0, "high": 12.0}, "units" : "g" }}},[]),
    ({"volume" : { "rxndom_value" : {"range" : {"low": 11.0, "high": 12.0}, "units" : "mL" }}},
        [' unknown generator (rxndom_value)']),
    ({"volume" : { "random_value" : {"rxnge" : {"low": 11.0, "high": 12.0}, "units" : "mL" }}},
        [" supplied arg (rxnge) is not valid.valid: dict_keys(['type', 'range', 'approx', 'exact', 'nsf_range', 'units', 'units_format'])"]),
    ({"volume" : { "random_value" : {"range" : {"lxw": 11.0, "high": 12.0}, "units" : "mL" }}},
        [" supplied subarg (lxw) to arg (range) is not valid.valid args: dict_keys(['low', 'high'])"]),
    ({"volume" : { "random_value" : {"range" : {"low": 11.0, "hxgh": 12.0}, "units" : "mL" }}},
        [" supplied subarg (hxgh) to arg (range) is not valid.valid args: dict_keys(['low', 'high'])"]),
    ({"volume" : { "random_value" : {"range" : {"lxw": 11.0, "hxgh": 12.0}, "units" : "mL" }}},
        [" supplied subarg (lxw) to arg (range) is not valid.valid args: dict_keys(['low', 'high'])", " supplied subarg (hxgh) to arg (range) is not valid.valid args: dict_keys(['low', 'high'])"]),
    ({"mass" : { "random_value" : {"range" :{"low":'11', "high": 12.0}, "units" : "g" }}},
        ["TypeError for argument low; wanted:<class 'float'> got:<class 'str'>"]),
    ({"mass" : { "random_value" : {"exact" : '12.34'}}},[]),
    ({"mass" : { "random_value" : {"exact" : 12.34}}},["TypeError for argument exact; wanted:<class 'str'> got:<class 'float'>"]),
    ({"mass" : { "random_value" : {"range" :{"low": 11.0, "high": 12.0}, "units" : "g", "nsf_range": [3,5] }}},[]),
    ({"mass" : { "random_value" : {"range" :{"low": 11.0, "high": 12.0}, "units" : "g", "nsf_range": 3 }}},["TypeError for argument nsf_range; wanted:<class 'list'> got:<class 'int'>"]),
    ({"mass" : { "random_value" : {"approx" :{"target": 11.0, "pct": 12.0}, "units" : "g", }}},[]),
    ({"mass" : { "random_value" : {"approx" :{"target": '11.0', "pct": 12.0}, "units" : "g", }}},["TypeError for argument target; wanted:<class 'float'> got:<class 'str'>"]),
    ({"added" : { "parse_expression" : {"expression" : '1+2'}}},[]),
    ({"added" : { "parse_expression" : {"expression" : 1+2}}},["TypeError for argument expression; wanted:<class 'str'> got:<class 'int'>"]),
    ({"added" : { "fill_template" : {"template" : ' a {animal}', "vars":{"animal" : "Millie"} }}},[]),
    #({"added" : { "parse_expression" : {"expression" : 1+2}}},["TypeError for argument expression; wanted:<class 'str'> got:<class 'int'>"]),
    ])
def test_args_validator(test_dict, answer):

    for name, DoD in test_dict.items():
        result = DG.validate_args(DoD)
        #print("Name:", name, " result:", result)
        assert answer == result

@pytest.mark.parametrize("A, B, result", [
    (["A1","A2"], ["B1","B2"], ["A1B1", "A2B1", "A1B2", "A2B2"] ),
])
def test_permute_sets(A,B,result):
    vars = {"A":A, "B":B}
    resultset = DG.permute_sets({"setA":"A", "setB":"B", "vars":vars})
    assert len(resultset["value"]) == len(result), f"set lengths don't match: {resultset =} {result =}"
    for checkstr in result:
        assert checkstr in resultset["value"], f"string {checkstr =} not in {resultset =}"
