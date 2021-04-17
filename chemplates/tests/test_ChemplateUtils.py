import pytest
import commentjson
import glob
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
    #print("ANSWERS:",pformat(filled))
    assert filled.assertEqualTo(correct_CP)

def test_validateFullChemplate():
    full = {
      "description": "Description of the problem type",
      "keywords": ["keywords for looking up problems"],
      "sources" : {
      # "source_name" : {"function": {"param":value, ... } },
        "mass" : { "random_value" : {"range" :{"low": 11.0, "high": 12.0}, "units" : "g" }},
        "volume" : { "random_value" : {"range" : {"low": 5.5, "high": 6.0}, "units" : "mL" }}
      },

      "questionlist" : [
      # template with vars, callables(chemformula, chemreaction)
      # uses template_variables (see below)
      # {"function": {"param":value, ... } },
        {"fill_template":{ "template":"What is the density of a sample with mass {{mass}} and volume {{volume}}?", "vars":{"var1":"true"}}}
      ],

      "answerlist" : [
      # uses values from sources
      #answer_template: an answer_template is a dictionary with the following
      #             keys (those currently used have asterisks. The others
      #             are currently ignored):
      #    'value' : the equation to get the answer, which is parsed and evaluated
      #    'units' : units desired for the answer
      #    'text' : text to be rendered as a jinja2 template. It could explain
      #              the answer with variable values filled in
      #    'correct' : a boolean flag tell in this answer is correct.
      #  {"dictkey" : {"function": {"param":value, ... } },
      #  },
        {
          "value" : { "parse_expression":{ "expression":"volume/mass", "vars":{}}},
          "units" : {"copy_text":{"text": "g/mL"}},
          "text" :  {"fill_template":{ "template":"mass/volume = ({{mass}})/{{volume}}", "vars":{}}},
          "correct" : {"copy_text":{"text": "false"}}
        },
      ]

      }
    res = CPU.validatefullChemplate(full)

def check_chemplatefile(filename):
    with open(filename, 'r') as handle:
        try:
            chemplateDict = commentjson.load(handle)
        except:
            print(f"malformed JSON in {filename}")
            handle.close()
            return

    chemplateNameList = [k for k in chemplateDict.keys() if "_answer" not in k ]

    for name in chemplateNameList:
        print(f"file:{filename} chemplate:{name}")
        chemplate = chemplateDict[name]
        answer = chemplateDict[name + "_answer"]
        res = CPU.validatefullChemplate(chemplate)
        #print("res::\n",str("\n".join(res)))
        assert str("\n".join(res)) == answer


def test_chemplatefiles():
    chemplateFilenamesList = glob.glob('chemplates/testchemplates/chemplate*.json')
    #print("files:",pformat(chemplateFilenamesList))
    for file in chemplateFilenamesList:
        check_chemplatefile(file)
