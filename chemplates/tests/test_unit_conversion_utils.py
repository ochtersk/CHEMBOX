from CHEMBOX.chemplates.unit_conversion_utils import *
import CHEMBOX.refdata.DataValue as DV
import pint
import pytest


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

    #XXX TO DO:
    # make conversions exact
    # DONE: make arbitrary units work
    #get datavalue to take strings with no space delimiters

@pytest.mark.parametrize("inputunitsstr,finalunitsstr,answerstr", [
    ("feet", "inches", "12"),
    ("inches", "feet", "0.083"),
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

# XXX needs more test on other sets
@pytest.mark.parametrize("setname,abbrev,lookfor,shouldntsee", [
    ("3-3", "NO", ["deca","centi"], ["da","m"]),
    ("3-3", "YES", ["c"], ["centi","y","yotta"]),
    ("3-3", "BOTH", ["c","centi"], ["y","yotta"]),
    ])
def test_get_metric_prefix_set(setname,abbrev,lookfor,shouldntsee):
    prefix_set = get_metric_prefix_set(set_label=setname, abbreviations=abbrev)
    for item in lookfor:
        assert (item in prefix_set), f"can't find {item} in {*prefix_set,}"
    for item in shouldntsee:
        assert (item not in prefix_set), f"found {item} in {*prefix_set,}"
