from CHEMBOX.chemplates.unit_conversion_utils import *
import CHEMBOX.refdata.DataValue as DV
import pint
import pytest
from pprint import pformat

@pytest.mark.parametrize("PintDefinition,unitslist", [
    ("beep =[sounds]",["beep"]),
    ("boop = 12.5 beep",["beep","boop"]),
    ])
def test_create_conversion(PintDefinition, unitslist):
    my_ureg = create_conversion(PintDefinition)
    for i in unitslist:
        assert i in my_ureg




@pytest.mark.parametrize("inputDVstr,finalunitsstr,answerDVstr", [
    ("6.0 boop", "beep", "75 beep"),
    ("6.0 ft","inch","72 inch"),
    ])
def test_do_convert(inputDVstr,finalunitsstr,answerDVstr):
    inputDV=DV.DataValue(inputDVstr)
    answerDV=DV.DataValue(answerDVstr)
    finalunits=finalunitsstr
    convertedDV = do_convert(inputDV,finalunits)
    assert str(answerDV)==str(convertedDV)
    assert isinstance(convertedDV,DV.DataValue)
    #print("do_convert:",pformat(convertedDV))
    #XXX TO DO:
    # DONE: make conversions exact
    # DONE: make arbitrary units work
    #get datavalue to take strings with no space delimiters

@pytest.mark.parametrize("inputunitsstr,finalunitsstr,answerstr", [
    ("feet", "inches", "12.000000000000000000"),
    ("inches", "feet", "0.083333333333333328707"),
    ("boop", "beep", "12.500000000000000000"),
    ])
def test_get_conversion_factor(inputunitsstr,finalunitsstr,answerstr):
    conversion_factor = get_conversion_factor(inputunitsstr,finalunitsstr)
    assert str(conversion_factor.magnitude)==answerstr

@pytest.mark.parametrize("inputDVstr,finalunitsstr,answerDVstr", [
    ("6.0 ft", "liters", "no answer"),
    ])
def test_do_convert_broken_calls(inputDVstr,finalunitsstr,answerDVstr):
    inputDV=DV.DataValue(inputDVstr)
    finalunits=finalunitsstr
    with pytest.raises(pint.errors.DimensionalityError) as excinfo:
        convertedDV = do_convert(inputDV,finalunits)
        assert "DimensionalityError" in str(excinfo.value)

@pytest.mark.parametrize("setname,abbrev,lookfor,shouldntsee", [
    ("3-3", "NO", ["deca","centi"], ["da","m"]),
    ("3-3", "YES", ["c"], ["centi","y","yotta"]),
    ("3-3", "BOTH", ["c","centi"], ["y","yotta"]),
    ("15-15", "NO", ["femto","peta"], ["f","P"]),
    ("15-15", "YES", ["P","p","n"], ["peta","pico","exa","yotta"]),
    ("15-15", "BOTH", ["c","centi"], ["y","yotta"]),
    ("24-24", "NO", ["femto","peta"], ["Q","q"]),
    ("24-24", "YES", ["P","f"], ["xpeta","xpico","xexa","xyotta"]),
    ("24-24", "BOTH", ["c","centi"], ["yY","yytta"]),
    ])
def test_get_metric_prefix_set(setname,abbrev,lookfor,shouldntsee):
    prefix_set = get_metric_prefix_set(set_label=setname, abbreviations=abbrev)
    for item in lookfor:
        assert (item in prefix_set), f"can't find {item} in {*prefix_set,}"
    for item in shouldntsee:
        assert (item not in prefix_set), f"found {item} in {*prefix_set,}"



@pytest.mark.parametrize("setname,abbrev,lookfor,shouldntsee", [
    ("length_common_english", "NO", ["feet","foot"], ["ft"]),
    ("length_common_english", "YES",  ["ft"], ["feet","foot"]),
    ("length_common_english", "BOTH",  ["ft","feet","foot"],["m","meter"]),
    ])
def test_get_units_set_setname(setname,abbrev,lookfor,shouldntsee):
    units_set = get_units_set(set_label=setname, abbreviations=abbrev)
    for item in lookfor:
        assert (item in units_set), f"can't find {item} in {*units_set,}"
    for item in shouldntsee:
        assert (item not in units_set), f"found {item} in {*units_set,}"
    #print("units set:",pformat(units_set))

@pytest.mark.parametrize("dimensionality,lookfor,shouldntsee", [
    ("[length]", ["feet","foot"], ["liter"]),
    ("[length] **3", ["gallon","liter"], ["feet","foot"]),
    ])
def test_get_units_set_dimensionality(dimensionality,lookfor,shouldntsee):
    units_set = get_units_set(dimensionality=dimensionality, abbreviations="NO")
    for item in lookfor:
        assert (item in units_set), f"can't find {item} in {*units_set,}"
    for item in shouldntsee:
        assert (item not in units_set), f"found {item} in {*units_set,}"


@pytest.mark.parametrize("unit_set,factor", [
    (set(("feet","inches")),"12.000000000000000000"),
    ])
def test_create_conversion_parameters(unit_set,factor):
    parameters = create_conversion_parameters(unit_set)
    #print("P:",pformat(parameters))
    for unit in unit_set:
        assert unit in parameters, f"unit missing from parameters:{unit}"
    assert isinstance(parameters[2],DV.DataValue)
