import pytest
from pprint import pformat
import copy
import CHEMBOX.chemplates.Chemplate as CP

@pytest.mark.parametrize("ID, attribute,value,answer", [
     ("Test","Attr1","seven","{'Test': {'Attr1': 'seven'}}"),
     ('Test1',None,None,"{}"),
     (None,'Attr1',None,"{}"),
     (None,None,None,"{}"),
])
def test_Chemplate_object(ID,attribute,value,answer):
    x = CP.Chemplate(ID,attribute,value)
    assert repr(x) == answer
    assert str(x) == answer

DoD = { "a":
        {
        "a1" : "7",
        "a2" : ["a","b"]
        },
        "b":
        {
        "b1" : "7",
        "b2" : 8
        },
      }
def test_Chemplate_init_from_DoD():
    x = CP.Chemplate(DoD=DoD)
    #print(pformat(DoD))
    assert repr(x) == pformat(DoD)

def test_Chemplate_init_fail_TypeError():
    with pytest.raises(TypeError):
        fail = CP.Chemplate(DOD=DoD)

x = CP.Chemplate()
y = CP.Chemplate()
@pytest.mark.parametrize("ID, attribute,value,answer", [
     # add 1 attribute
     ("Test","Attr1","seven","{'Test': {'Attr1': 'seven'}}"),
     # add another to the same one
     ("Test","Attr2","eight","{'Test': {'Attr1': 'seven', 'Attr2': 'eight'}}"),
     #replace 1 attr
     ("Test","Attr1","six","{'Test': {'Attr1': 'six', 'Attr2': 'eight'}}"),
])
def test_Chemplate_setID(ID,attribute,value,answer):
    y.setID(ID=ID,attribute=attribute,value=value)
    assert repr(y) == answer
    x.setID(ID,attribute,value)
    assert repr(x) == answer

def test_Chemplate_getID():
    x = CP.Chemplate(DoD=DoD)
    a = x.getID(ID="a")
    assert pformat(a) == pformat(DoD["a"])
    with pytest.raises(KeyError):
        fail = x.getID(ID="c")

def test_Chemplate_getIDattr():
    x = CP.Chemplate(DoD=DoD)
    a = x.getIDattr(ID="a",attribute="a1")
    assert pformat(a) == pformat(DoD["a"]["a1"])
    with pytest.raises(KeyError):
        fail = x.getIDattr(ID="c", attribute="a1")
    with pytest.raises(KeyError):
        fail = x.getIDattr(ID="a", attribute="ax")

def test_Chemplate_getIDs():
    x = CP.Chemplate(DoD=DoD)
    a = x.getIDs()
    assert pformat(a) == pformat(DoD.keys())
    x = CP.Chemplate(DoD={})
    a = x.getIDs()
    assert pformat(a) == pformat({}.keys())

def test_Chemplate_updateWith():
    x = CP.Chemplate(DoD=DoD)
    new = {
            "b":
            {
            "b1" : "string",
            "b3" : "number"
            },
          }
    newCP = CP.Chemplate(DoD=new)
    newDoD = DoD.copy()
    newDoD["b"] = new["b"]
    savedDoD = DoD.copy()
    x.updateWith(new = newCP)
    assert repr(x) == pformat(newDoD)
    #make sure we didn't screw with DoD
    assert pformat(savedDoD) == pformat(DoD)

def test_Chemplate_delID():
    x = CP.Chemplate(DoD=DoD)
    savedDoD = DoD.copy()
    alteredDoD = DoD.copy()
    alteredDoD.pop("b")
    deleted = x.delID(ID="b")
    assert pformat(deleted) == pformat(DoD["b"])
    assert repr(x) == pformat(alteredDoD)
    #make sure we didn't screw with DoD
    assert pformat(savedDoD) == pformat(DoD)
    with pytest.raises(KeyError):
        fail = x.delID(ID="c")
    with pytest.raises(TypeError):
        fail = x.delID(ID="b",attribute="b1" )

def test_Chemplate_delIDattr():
    x = CP.Chemplate(DoD=DoD)
    savedDoD = copy.deepcopy(DoD)
    alteredDoD = copy.deepcopy(DoD)
    alteredDoD["b"].pop("b1")
    deleted = x.delIDattr(ID="b",attribute="b1")
    assert pformat(deleted) == pformat(DoD["b"]["b1"])
    assert repr(x) == pformat(alteredDoD)
    #make sure we didn't screw with DoD
    assert pformat(savedDoD) == pformat(DoD)
    with pytest.raises(KeyError):
        fail = x.delIDattr(ID="c",attribute="b1")
    with pytest.raises(KeyError):
        fail = x.delIDattr(ID="b",attribute="bx")
