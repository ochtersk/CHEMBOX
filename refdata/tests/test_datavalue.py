import pytest
import refdata.DataValue as DV


@pytest.mark.parametrize("mag,units,answer", [
    ("2.4","liter / minute","2.4 liter / minute"),
    ("2.4e+2","liter / minute","2.4e+2 liter / minute"),
    ("2.4","minute * mole / liter","2.4 minute * mole / liter"),
    ("2.4","liter / minute ** 2","2.4 liter / minute ** 2"),
])
def test_DataValue_object_noformat(mag, units, answer):
    x = DV.DataValue(mag, units)
    #print("DV repr:"+repr(x))
    assert str(x) == answer
    assert str(x.magnitude) == mag
    assert str(x.units) == units

@pytest.mark.parametrize("spec_in,mag,units,answer", [
    ("","2.4","liter / minute","2.4 liter / minute"),
    ("","2.4e+2","liter / minute","2.4e+2 liter / minute"),
    ("","2.4","minute * mole / liter","2.4 minute * mole / liter"),
    ("","2.4","liter / minute ** 2","2.4 liter / minute ** 2"),
    ("abbrev","2.4","liter / minute","2.4 l / min"),
    ("abbrev","2.4e+2","liter / minute","2.4e+2 l / min"),
    ("abbrev","2.4","minute * mole / liter","2.4 min * mol / l"),
    ("abbrev","2.4","liter / minute ** 2","2.4 l / min ** 2"),
    ("HTML","2.4","liter / minute","2.4 liter/minute"),
    ("HTML","2.4e+2","liter / minute","2.4e+2 liter/minute"),
    ("HTML","2.4","minute * mole / liter","2.4 minute mole/liter"),
    ("HTML","2.4","liter / minute ** 2","2.4 liter/minute<sup>2</sup>"),
    ("abbrev,HTML","2.4","liter / minute","2.4 l/min"),
    ("abbrev,HTML","2.4e+2","liter / minute","2.4e+2 l/min"),
    ("abbrev,HTML","2.4","minute * mole / liter","2.4 min mol/l"),
    ("abbrev,HTML","2.4","liter / minute ** 2","2.4 l/min<sup>2</sup>"),
])
def test_DataValue_object_format(mag, units, answer, spec_in):
    x = DV.DataValue(mag, units, units_format = spec_in)
    #print("DV repr:"+repr(x))
    assert str(x) == answer
    assert str(x.magnitude) == mag
    assert str(x.units) == units








@pytest.mark.parametrize("mag,mag_exact,units,answer", [
    ("2.4","2.4000000000000000000","liter / minute","2.4000000000000000000 liter / minute"),
    ("2.4e2","240.00000000000000000","liter / minute","240.00000000000000000 liter / minute"),
    ("2.4","2.4000000000000000000","minute * mole / liter","2.4000000000000000000 minute * mole / liter"),
    ("2.4","2.4000000000000000000","liter / minute ** 2","2.4000000000000000000 liter / minute ** 2"),
])
def test_DataValue_object_exact(mag, mag_exact, units, answer):
    x = DV.DataValue(mag, units, exact = True)
    #print("DV repr:"+repr(x))
    assert str(x) == answer
    assert str(x.magnitude) == mag_exact
    assert str(x.units) == units


def test_datavalue_mul():
    x = DV.DataValue("2.314", "g/mL")
    y = DV.DataValue("2.0", "mL")
    z = x*y
    #print("repr x:",repr(x))
    #print("repr y:",repr(y))
    #print("repr z:",repr(z))
    assert str(z) == "4.6 gram"

def test_datavalue_mul_float_int():
    x = DV.DataValue("2.314")
    y = 2
    z = x*y
    #print("repr z:",repr(z))
    #print("str z:",str(z),"<<")
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
    assert str(z) == "1.2 gram / milliliter"


def test_datavalue_div2():
    x = DV.DataValue("10.00", "g")
    y = DV.DataValue("2.00", "mL")
    z = x/y
    #print("repr z:",repr(z))
    assert str(z) == "5.00 gram / milliliter"

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
    assert str(z) == "4.4 gram"


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
        assert str(z) == "4.4 gram"

def test_datavalue_sub_ok():
    x = DV.DataValue("22.414", "g")
    y = DV.DataValue("22.0", "g")
    z = x-y
    #print("repr z:",repr(z))
    assert str(z) == "0.4 gram"

def test_datavalue_sub_ok_int_float():
    x = DV.DataValue("22.414","")
    y = 22
    z = x-y
    #print("repr z:",repr(z))
    assert str(z) == "0" # rounded to nearest  unit
    y=22.000
    z = x-y
    #print("repr z:",repr(z))
    assert str(z) == "0.4"
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
        assert str(z) == "4.4 gram"




def test_DataValue_object_default():
    x = DV.DataValue()
    #print("DV:",repr(x))
    assert str(x) == "0.0"
