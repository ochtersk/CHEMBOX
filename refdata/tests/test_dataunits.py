import pytest
import CHEMBOX.refdata.DataUnits as DU



#startpassed
@pytest.mark.parametrize("units_in,unitsformat_in,answer", [
    ("L/min","expanded", "L/min"),
    ("L/min","other", "L/min"),
    ("L*mol/min^2", "expanded","L*mol/min*min"),
    ("L*mol/min^2", "other","L*mol/min^2"),
    ("L*mol/min*min", "expanded","L*mol/min*min"),
    ("L*mol/min*min", "other","L*mol/min^2"),
    ("1/min","expanded", "1/min"),
    ("1/min","other", "1/min"),
])
def test_dataunit(units_in, unitsformat_in, answer):
    x = DU.DataUnits(units_in, unitsformat = unitsformat_in)
    assert str(x) == answer

def test_dataunit_forcestring():
    with pytest.raises(AttributeError):
        x = DU.DataUnits(["min"])
        assert str(x) == answer

@pytest.mark.parametrize("units1_in,units2_in,answer", [
    ("L/min","min^2/ft","L*min/ft"),
    ("g/mL","mL","g"),
    ("g","ml/g","ml"),
])
def test_dataunit_mult(units1_in,units2_in,answer):
    x = DU.DataUnits(units1_in)
    y = DU.DataUnits(units2_in)
    z = x*y
    assert str(z) == answer

@pytest.mark.parametrize("units1_in,answer", [
    ("L/min","min/L"),
    ("min^2/ft","ft/min*min"),
    ("1/mL","mL"),
    ("g","1/g"),
])
def test_dataunit_recip(units1_in,answer):
    x = DU.DataUnits(units1_in)
    z = x._reciprocal()
    assert str(z) == answer

@pytest.mark.parametrize("units1_in,units2_in,answer", [
    ("L/min","ft/min^2","L*min/ft"),
    ("g/mL","1/mL","g"),
    ("g","g/ml","ml"),
    ("L/min","min/L",'L*L/min*min'),
    ("L/min","L/min",''),
])
def test_dataunit_div(units1_in,units2_in,answer):
    x = DU.DataUnits(units1_in)
    y = DU.DataUnits(units2_in)
    z = x/y
    assert str(z) == answer

#endpassed


@pytest.mark.parametrize("units1_in,units2_in,answer", [
    ("L/min","L/min","L/min"),
])
def test_dataunit_addsub(units1_in,units2_in,answer):
    x = DU.DataUnits(units1_in)
    y = DU.DataUnits(units2_in)
    z = x+y
    assert str(z) == answer
    z = x-y
    assert str(z) == answer

def test_operator_chaining():
    w = DU.DataUnits("g A")
    x = DU.DataUnits("g A/mol A")
    y = DU.DataUnits("mol B/mol A")
    z = DU.DataUnits("g B/mol B")
    u = w/x*y*z
    assert str(u) == "g B"



@pytest.mark.parametrize("units1_in,units2_in,answer", [
    ("L/min","L/man","L/min"),
])
def test_dataunit_addsub_assertionfail(units1_in,units2_in,answer):
    with pytest.raises(AssertionError):
        x = DU.DataUnits(units1_in)
        y = DU.DataUnits(units2_in)
        z = x+y
        assert str(z) == answer
    with pytest.raises(AssertionError):
        x = DU.DataUnits(units1_in)
        y = DU.DataUnits(units2_in)
        z = x-y
        assert str(z) == answer
