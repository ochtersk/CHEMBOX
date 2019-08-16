import pytest
from pprint import pformat
import chemplates.ChemplateUtils as CPU
import refdata.DataValue as DV

def test_fillvar_sources_only():
    source = {'randomValue' :{'type' : 'exact', 'exact' : '123.456'}}
    overrides = {}
    var = CPU.fillvar(source,overrides)
    assert str(var['randomValue']) == str(DV.DataValue("123.456"))
    #print(pformat(var))


def test_fillvar_with_overrides1():
    overrides = {'randomValue' :{'type' : 'exact', 'exact' : '126.456'}}
    source = {'randomValue' : {'range' : {'low': 11.0, 'high': 12.0}}}
    var = CPU.fillvar(source,overrides)
    assert str(var['randomValue']) == str(DV.DataValue("126.456"))
    #print(pformat(var))

def test_fillvar_with_overrides2():
    overrides = {'randomValue' :{'type' : 'exact', 'exact' : '127.456', 'units': 'g/mL'}}
    source = {'randomValue' : {'range' : {'low': 11.0, 'high': 12.0}}}
    var = CPU.fillvar(source,overrides)
    assert str(var['randomValue']) == str(DV.DataValue("127.456 g/mL"))
    #print(pformat(var))
