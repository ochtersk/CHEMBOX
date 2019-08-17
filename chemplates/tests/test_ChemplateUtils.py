import pytest
from pprint import pformat
import chemplates.Chemplate as CP
import chemplates.ChemplateUtils as CPU
import refdata.DataValue as DV

def test_fillvar_sources_only():
    source = CP.Chemplate(DoD={"rand1" :{'randomValue' :{'type' : 'exact', 'exact' : '123.456'}}})
    overrides = CP.Chemplate(DoD= {})
    var = CPU.fillvar(source,overrides)
    assert str(var.getIDattr('rand1','value')) == str(DV.DataValue("123.456"))

def test_fillvar_multisources_only():
    source = CP.Chemplate(DoD={'rand1a' :{'randomValue' :{'type' : 'exact', 'exact' : '123.456'}},
                               'rand1b' :{'randomValue' :{'type' : 'exact', 'exact' : '123.567'}}})
    overrides = CP.Chemplate(DoD= {})
    var = CPU.fillvar(source,overrides)
    assert str(var.getIDattr('rand1a','value')) == str(DV.DataValue("123.456"))
    assert str(var.getIDattr('rand1b','value')) == str(DV.DataValue("123.567"))

def test_fillvar_bad_generator():
    source = CP.Chemplate(DoD={'rand1a' :{'randomdalue' : 123}})
    overrides = CP.Chemplate(DoD= {})
    with pytest.raises(AssertionError):
        var = CPU.fillvar(source,overrides)

def test_fillvar_with_overrides1():
    overrides = CP.Chemplate(DoD={"rand2" :{'randomValue' :{'type' : 'exact', 'exact' : '126.456'}}})
    source = CP.Chemplate(DoD={"rand2" :{'randomValue' : {'range' : {'low': 11.0, 'high': 12.0}}}})
    var = CPU.fillvar(source,overrides)
    assert str(var.getIDattr('rand2','value')) == str(DV.DataValue("126.456"))

def test_fillvar_multisource_with_overrides1():
    overrides = CP.Chemplate(DoD={"rand2a" :{'randomValue' :{'type' : 'exact', 'exact' : '126.456'}}})
    source = CP.Chemplate(DoD={"rand2a" :{'randomValue' : {'range' : {'low': 11.0, 'high': 12.0}}},
                               'rand2b' :{'randomValue' :{'type' : 'exact', 'exact' : '123.567'}}})

    var = CPU.fillvar(source,overrides)
    assert str(var.getIDattr('rand2a','value')) == str(DV.DataValue("126.456"))
    assert str(var.getIDattr('rand2b','value')) == str(DV.DataValue("123.567"))

def test_fillvar_multisource_with_two_overrides1():
    overrides = CP.Chemplate(DoD={"rand2a" :{'randomValue' :{'type' : 'exact', 'exact' : '126.456'}},
                               'rand2b' :{'randomValue' :{'type' : 'exact', 'exact' : '123.567'}}})
    source = CP.Chemplate(DoD={"rand2a" :{'randomValue' : {'range' : {'low': 11.0, 'high': 12.0}}},
                               'rand2b' :{'randomValue' : {'range' : {'low': 11.0, 'high': 12.0}}}})
    var = CPU.fillvar(source,overrides)
    assert str(var.getIDattr('rand2a','value')) == str(DV.DataValue("126.456"))
    assert str(var.getIDattr('rand2b','value')) == str(DV.DataValue("123.567"))

def test_fillvar_with_overrides2():
    overrides = CP.Chemplate(DoD={"rand3" :{'randomValue' :{'type' : 'exact', 'exact' : '127.456', 'units': 'g/mL'}}})
    source = CP.Chemplate(DoD={'rand3':{'randomValue' : {'range' : {'low': 11.0, 'high': 12.0}}}})
    var = CPU.fillvar(source,overrides)
    assert str(var.getIDattr('rand3','value')) == str(DV.DataValue("127.456 g/mL"))

def test_assignvals_multisources():
    source = CP.Chemplate(DoD={'rand1a' :{'randomValue' :{'type' : 'exact', 'exact' : '123.456'}},
                               'rand1b' :{'randomValue' :{'type' : 'exact', 'exact' : '123.567'}}})
    overrides = CP.Chemplate(DoD= {})
    var = CPU.fillvar(source,overrides)
    varmap = {'vrand1':['rand1a','value'],
              'vrand2':['rand1b','value'],
             }
    vals = CPU.assignvals(varmap,var)
    #print("VALS:",pformat(vals))
    assert str(vals['vrand1']) == str(DV.DataValue("123.456"))
    assert str(vals['vrand2']) == str(DV.DataValue("123.567"))

#documenation
