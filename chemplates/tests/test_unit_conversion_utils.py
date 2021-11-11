from CHEMBOX.chemplates.unit_conversion_utils import *
import CHEMBOX.refdata.DataValue as DV
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

    # TO DO:
    # make conversions exact
    # future: make arbitrary units work
    #get datavalue to take strings with no space delimiters
