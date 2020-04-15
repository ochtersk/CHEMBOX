import pytest
from pprint import pformat
import CHEMBOX.chemplates.Chemplate as CP
import CHEMBOX.chemplates.ChemplateUtils as CPU
import CHEMBOX.refdata.DataValue as DV

def test_create_Chemplate_from_sources_sources_only():
    source = CP.Chemplate(DoD={"rand1" :{'random_value' :{'type' : 'exact', 'exact' : '123.456'}}})
    overrides = CP.Chemplate(DoD= {})
    var = CPU.create_Chemplate_from_sources(source,overrides)
    assert str(var.getIDattr('rand1','value')) == str(DV.DataValue("123.456"))

def test_create_Chemplate_from_sources_multisources_only():
    source = CP.Chemplate(DoD={'rand1a' :{'random_value' :{'type' : 'exact', 'exact' : '123.456'}},
                               'rand1b' :{'random_value' :{'type' : 'exact', 'exact' : '123.567'}}})
    overrides = CP.Chemplate(DoD= {})
    var = CPU.create_Chemplate_from_sources(source,overrides)
    assert str(var.getIDattr('rand1a','value')) == str(DV.DataValue("123.456"))
    assert str(var.getIDattr('rand1b','value')) == str(DV.DataValue("123.567"))

def test_create_Chemplate_from_sources_bad_generator():
    source = CP.Chemplate(DoD={'rand1a' :{'randomdalue' : {"foo": 123}}})
    overrides = CP.Chemplate(DoD= {})
    with pytest.raises(AssertionError):
        var = CPU.create_Chemplate_from_sources(source,overrides)

def test_create_Chemplate_from_sources_bad_generator():
    source = CP.Chemplate(DoD={'rand1a' :{'randomdalue' :  123}})
    overrides = CP.Chemplate(DoD= {})
    with pytest.raises(AssertionError):
        var = CPU.create_Chemplate_from_sources(source,overrides)

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
            "use_vals_dict": "true"}
            }})
    overrides = CP.Chemplate(DoD= {})
    valsdict = {"mass": 5.0, "density": 10.0}
    var = CPU.create_Chemplate_from_sources(source,overrides,valsdict)
    assert str(var.getIDattr('expr','value')) == str(DV.DataValue("0.5"))


def xxtest_assignvals_multisources():
    source = CP.Chemplate(DoD={'rand1a' :{'random_value' :{'type' : 'exact', 'exact' : '123.456'}},
                               'rand1b' :{'random_value' :{'type' : 'exact', 'exact' : '123.567'}}})
    overrides = CP.Chemplate(DoD= {})
    var = CPU.create_Chemplate_from_sources(source,overrides)
    varmap = {'vrand1':['rand1a','value'],
              'vrand2':['rand1b','value'],
             }
    vals = CPU.assignvals(varmap,var)
    #print("VALS:",pformat(vals))
    assert str(vals['vrand1']) == str(DV.DataValue("123.456"))
    assert str(vals['vrand2']) == str(DV.DataValue("123.567"))

answer_template_1 = {
    "value" : { "parse_expression":{ "expression":"mass/density", "vars":"vars"}},
    "units" : {"copy_text":{"text": "g/mL"}},
    "text" :  {"fill_template":{ "template":"mass/volume = ({{mass}})/{{volume}} = {{value}}"}},
    "correct" : "true",
    "reason" : {"copy_text":{"text":"To be implemented"}},
}

ten =  DV.DataValue('10.00 g')
vars = { 'mass' : ten,
         'density' : DV.DataValue('2.00 g/mL')
         }
answer_template_list1 = [answer_template_1]
# def test_answer_template_simple():
#     answerlist=CPU.fillanswerlist(answer_template_list1, vars)
#     print(answerlist)
#     assert str(answerlist[0]['value']) == str(DV.DataValue('5.00 mL'))
