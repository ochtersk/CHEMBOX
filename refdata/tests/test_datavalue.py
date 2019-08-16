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


def test_datavalue_div():
    x = DV.DataValue("2.414", "g")
    y = DV.DataValue("2.0", "mL")
    z = x/y
    #print("repr z:",repr(z))
    assert str(z) == "1.2 g/mL"


def test_datavalue_add_ok():
    x = DV.DataValue("2.414", "g")
    y = DV.DataValue("2.0", "g")
    z = x+y
    #print("repr z:",repr(z))
    assert str(z) == "4.4 g"


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


def test_datavalue_sub_fail_units():
    x = DV.DataValue("2.414", "g")
    y = DV.DataValue("2.0", "mL")
    with pytest.raises(AssertionError):
        z = x-y
        ##print("repr z:",repr(z))
        assert str(z) == "4.4 g"
