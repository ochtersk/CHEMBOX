import pytest
import json
from pprint import pformat
import CHEMBOX.chemplates.Chemplate as CP
import CHEMBOX.chemplates.ChemplateUtils as CPU
import CHEMBOX.refdata.DataValue as DV

def test_create_Chemplate_from_sources_sources_only():
    source = CP.Chemplate(DoD={"rand1" :{'random_value' :{'type' : 'exact', 'exact' : '123.456'}}})
    var = CPU.create_Chemplate_from_sources(source)
    assert str(var.getIDattr('rand1','value')) == str(DV.DataValue("123.456"))

def test_create_Chemplate_from_sources_multisources_only():
    source = CP.Chemplate(DoD={'rand1a' :{'random_value' :{'type' : 'exact', 'exact' : '123.456'}},
                               'rand1b' :{'random_value' :{'type' : 'exact', 'exact' : '123.567'}}})
    var = CPU.create_Chemplate_from_sources(source)
    assert str(var.getIDattr('rand1a','value')) == str(DV.DataValue("123.456"))
    assert str(var.getIDattr('rand1b','value')) == str(DV.DataValue("123.567"))

def test_create_Chemplate_from_sources_bad_generator():
    source = CP.Chemplate(DoD={'rand1a' :{'randomdalue' : {"foo": 123}}})
    with pytest.raises(AssertionError):
        var = CPU.create_Chemplate_from_sources(source)

def test_create_Chemplate_from_sources_bad_generator():
    source = CP.Chemplate(DoD={'rand1a' :{'randomdalue' :  123}})
    with pytest.raises(AssertionError):
        var = CPU.create_Chemplate_from_sources(source)

def test_create_Chemplate_from_sources_with_overrides1():
    overrides = CP.Chemplate(DoD={"rand2" :{'random_value' :{'type' : 'exact', 'exact' : '126.456'}}})
    source = CP.Chemplate(DoD={"rand2" :{'random_value' : {'range' : {'low': 11.0, 'high': 12.0}}}})
    var = CPU.create_Chemplate_from_sources(source,overrides)
    assert str(var.getIDattr('rand2','value')) == str(DV.DataValue("126.456"))

def test_create_Chemplate_from_sources_multisource_with_overrides1():
    overrides = CP.Chemplate(DoD={"rand2a" :{'random_value' :{'type' : 'exact', 'exact' : '126.456'}}})
    source = CP.Chemplate(DoD={"rand2a" :{'random_value' : {'range' : {'low': 11.0, 'high': 12.0}}},
                               'rand2b' :{'random_value' :{'type' : 'exact', 'exact' : '123.567'}}})

    var = CPU.create_Chemplate_from_sources(source,overrides)
    assert str(var.getIDattr('rand2a','value')) == str(DV.DataValue("126.456"))
    assert str(var.getIDattr('rand2b','value')) == str(DV.DataValue("123.567"))

def test_create_Chemplate_from_sources_multisource_with_two_overrides1():
    overrides = CP.Chemplate(DoD={"rand2a" :{'random_value' :{'type' : 'exact', 'exact' : '126.456'}},
                               'rand2b' :{'random_value' :{'type' : 'exact', 'exact' : '123.567'}}})
    source = CP.Chemplate(DoD={"rand2a" :{'random_value' : {'range' : {'low': 11.0, 'high': 12.0}}},
                               'rand2b' :{'random_value' : {'range' : {'low': 11.0, 'high': 12.0}}}})
    var = CPU.create_Chemplate_from_sources(source,overrides)
    assert str(var.getIDattr('rand2a','value')) == str(DV.DataValue("126.456"))
    assert str(var.getIDattr('rand2b','value')) == str(DV.DataValue("123.567"))

def test_create_Chemplate_from_sources_with_overrides2():
    overrides = CP.Chemplate(DoD={"rand3" :{'random_value' :{'type' : 'exact', 'exact' : '127.456', 'units': 'g/mL'}}})
    source = CP.Chemplate(DoD={'rand3':{'random_value' : {'range' : {'low': 11.0, 'high': 12.0}}}})
    var = CPU.create_Chemplate_from_sources(source,overrides)
    assert str(var.getIDattr('rand3','value')) == str(DV.DataValue("127.456 g/mL"))

def test_create_Chemplate_from_sources_with_overrides2():
    overrides = CP.Chemplate(DoD={"rand3" :{'random_value' :{'type' : 'exact', 'exact' : '127.456', 'units': 'g/mL'}}})
    source = CP.Chemplate(DoD={'rand3':{'random_value' : {'range' : {'low': 11.0, 'high': 12.0}}}})
    var = CPU.create_Chemplate_from_sources(source,overrides)
    assert str(var.getIDattr('rand3','value')) == str(DV.DataValue("127.456 g/mL"))

def test_create_Chemplate_from_sources_with_valsdict():
    source = CP.Chemplate(DoD={ "expr":{"parse_expression":{ "expression":"mass/density",
            "use_values": "true"}
            }})
    overrides = None
    valsdict = {"mass": 5.0, "density": 10.0}
    var = CPU.create_Chemplate_from_sources(source,overrides,valsdict)
    assert str(var.getIDattr('expr','value')) == str(DV.DataValue("0.5"))

def test_create_Chemplate_from_sources_with_chemplate():
    source = CP.Chemplate(DoD={ "text4" :  {"fill_template":{ "template":"vol = {{data.mass/data.density}}", "use_values":"true"}},
            })
    overrides = None
    values = CP.Chemplate(DoD={ "data": {"mass": 5.0, "density": 10.0}})
    var = CPU.create_Chemplate_from_sources(source,overrides,values)
    assert str(var.getIDattr('text4','value')) == "vol = 0.5"



# this needs to be better tested -
# tests with errors
#tests with values as Chemplate
#
def test_answer_template():
    source = CP.Chemplate(DoD={"rand1" :{'random_value' :{'type' : 'exact', 'exact' : '12.02'}},
                               "rand2" :{'random_value' :{'type' : 'exact', 'exact' : '6.01'}}})

    var = CPU.create_Chemplate_from_sources(source)
    answer_template_1 = CP.Chemplate(DoD={
            "value" : { "parse_expression":{ "expression":"mass/density", "use_values":"true"}},
            "units" : {"copy_text":{"text": "g/mL"}},
            "text" :  {"fill_template":{ "template":"mass/volume = ({{mass}})/{{volume}} = {{density}}", "use_values":"true"}},
            "text2" :  {"fill_template":{ "template":"mag units = {{property.magnitude}} {{property['units']}}", "use_values":"true"}},
            "text3" :  {"fill_template":{ "template":"density = {{mass/volume}}", "use_values":"true"}},
            "text4" :  {"fill_template":{ "template":"two = {{rand1.value/rand2.value}}", "use_values":"true"}},
            "correct" : {"copy_text":{"text": "true"}},
            "reason" : {"copy_text":{"text":"To be implemented"}},        #"partials" : [{"parse_expression":{ "expression":"2.00*mass", "vars":true}},
        #              {"parse_expression":{ "expression":"0.0500*mass", "vars":true}},
        #             ]
        })
    correct_answers = {'correct': {'value': 'true'},
        'reason': {'value': 'To be implemented'},
        'text': {'value': 'mass/volume = (10.00 g)/2.00 mL = 5.0000 g/mL'},
        'text2': {'value': 'mag units = 7.777 km/hr'},
        'text3': {'value': 'density = 5.00 g/mL'},
        'text4': {'value': 'two = 2.00'},
        'units': {'value': 'g/mL'},
        'value': {'value': str(DV.DataValue("2.000 mL"))}
        }
    #print("SOURCE:",pformat(var))
    overrides = CP.Chemplate(DoD= {})
    correct_CP = CP.Chemplate(DoD=correct_answers)
    ten =  DV.DataValue('10.00 g')
    #This should be a DOD with "values"
    vars = { 'mass' : ten,
             'volume' : DV.DataValue('2.00 mL'),
             'density': DV.DataValue('5.0000 g/mL'),
             'property':{"magnitude":7.777, "units":"km/hr"}
             }
    vars.update([("rand1",var.getID("rand1")),("rand2",var.getID("rand2"))])

    filled = CPU.create_Chemplate_from_sources(answer_template_1, overrides, values=vars)
    print("ANSWERS:",pformat(filled))
    assert filled.equalTo(correct_CP)
