import pytest
import refdata.DataValue as DV
import refdata.RefData as RD

#pytestmark = pytest.mark.skip("all tests still WIP")
@pytest.mark.parametrize("Cprop,Cname,answer", [
    ("density","ethanol","0.7851 g/mL"),
    ("density","ethanol at 20C","0.789 g/mL"),
])
def test_RefData_object(Cprop, Cname, answer):
    #ans = DV.DataValue(answer)
    test_str = f'{Cname} has a {Cprop} value of {answer}'
    x = RD.RefData(chemicalProperty = Cprop, chemicalName=Cname )
    assert str(x.value) == str(answer)
    assert str(x) == test_str

@pytest.mark.parametrize("Cprop,Cname,answer", [
    ("destinyXX","ethanol","0.7851 g/mL"),
    ("density","ethanol at XXC","0.789 g/mL"),
    ("density","ethanol","0.7856 g/mL"),
])
def test_RefData_object_fail(Cprop, Cname, answer):
    #ans = DV.DataValue(answer)
    with pytest.raises(AssertionError):
        x = RD.RefData(chemicalProperty = Cprop, chemicalName=Cname )
        assert str(x.value) == str(answer)


def test_RefData_object_proponly():
    #ans = DV.DataValue(answer)
    x = RD.RefData(chemicalProperty = "density")
    #assert str(x.value) == str(answer)



def test_RefData_object_fail_proponly():
    with pytest.raises(AssertionError):
        x = RD.RefData(chemicalProperty = "destinyXX")
        #destinyXX is not a typo
        assert str(z) == "DV: 4.4 g"


def test_RefData_object_fail_duplicate():
    with pytest.raises(AssertionError):
        x = RD.RefData(chemicalProperty = "destiny", chemicalName ="duplicate")
        #destinyXX is not a typo
        assert str(z) == "DV: 4.4 g"
