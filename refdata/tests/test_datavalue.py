import pytest
import refdata.DataValue as DV


@pytest.mark.parametrize("mag,units,answer", [
    ("2.4","L/min","2.4 L/min"),
    ("2.4e+2","L/min","2.4e+2 L/min"),
    ("2.4","mol/L*min","2.4 mol/L*min"),
    ("2.4","L/min^2","2.4 L/min^2"),
])
def test_DataValue_object(mag, units, answer):
    x = DV.DataValue(mag, units)
    assert str(x) == answer
    assert str(x.magnitude) == mag
    assert str(x.units) == units


def test_datavalue_mul():
    x = DV.DataValue("2.314", "g/mL")
    y = DV.DataValue("2.0", "mL")
    z = x*y
    #print("repr z:",repr(z))
    assert str(z) == "4.6 g"

def test_datavalue_mul_float_int():
    x = DV.DataValue("2.314")
    y = 2
    z = x*y
    #print("repr z:",repr(z))
    assert str(z) == "5"
    y = 2.0000001
    z = x*y
    #print("repr z:",repr(z))
    assert str(z) == "4.628"


def test_datavalue_div():
    x = DV.DataValue("2.414", "g")
    y = DV.DataValue("2.0", "mL")
    z = x/y
    #print("repr z:",repr(z))
    assert str(z) == "1.2 g/mL"

def test_datavalue_div_float_int():
    x = DV.DataValue("2.424")
    y = 2
    z = x/y
    #print("repr z:",repr(z))
    assert str(z) == "1"
    y = 2.0000000000001
    z = x/y
    #print("repr z:",repr(z))
    assert str(z) == "1.212"


def test_datavalue_add_ok():
    x = DV.DataValue("2.414", "g")
    y = DV.DataValue("2.0", "g")
    z = x+y
    #print("repr z:",repr(z))
    assert str(z) == "4.4 g"


def test_datavalue_add_float_int():
    x = DV.DataValue("2.414", "")
    y = 2
    z = x+y
    #print("repr z:",repr(z))
    assert str(z) == "4"
    y = 2.001
    z = x+y
    #print("repr z:",repr(z))
    assert str(z) == "4.415"


def test_datavalue_add_fail_units():
    x = DV.DataValue("2.414", "g")
    y = DV.DataValue("2.0", "mL")
    with pytest.raises(AssertionError):
        z = x+y
        #print("repr z:",repr(z))
        assert str(z) == "4.4 g"

def test_datavalue_sub_ok():
    x = DV.DataValue("22.414", "g")
    y = DV.DataValue("22.0", "g")
    z = x-y
    #print("repr z:",repr(z))
    assert str(z) == "0.4 g"

def test_datavalue_sub_ok_int_float():
    x = DV.DataValue("22.414","")
    y = 22
    z = x-y
    #print("repr z:",repr(z))
    assert str(z) == "0" # rounded to nearest  unit
    y=22.000
    z = x-y
    #print("repr z:",repr(z))
    assert str(z) == "0" # rounded to nearest unit because no way to tell SF
    y=22.001
    z = x-y
    #print("repr z:",repr(z))
    assert str(z) == "0.413"



def test_datavalue_sub_fail_units():
    x = DV.DataValue("2.414", "g")
    y = DV.DataValue("2.0", "mL")
    with pytest.raises(AssertionError):
        z = x-y
        ##print("repr z:",repr(z))
        assert str(z) == "4.4 g"


@pytest.mark.parametrize("magunits,answer", [
    ("2.4 L/min","2.4 L/min"),
    ("2.4e+2 L/min","2.4e+2 L/min"),
    ("2.4 mol/L*min","2.4 mol/L*min"),
    ("2.4 L/min^2","2.4 L/min^2"),
])
def test_DataValue_object(magunits, answer):
    x = DV.DataValue(magunits)
    assert str(x) == answer


def test_DataValue_object_default():
    x = DV.DataValue()
    #print("DV:",repr(x))
    assert str(x) == "0.0"
