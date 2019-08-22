import pytest
from pprint import pformat
import chemplates.DataGenerators as DG

def isinrange(val,low,high):
    if (float(val)>=low and float(val) <= high):
        return True
    else:
        print("isinrange:",low,val,high)
    return False


@pytest.mark.parametrize("units", [
    ({'units':"g"}),
    ({'units':''}),
    ({'units':"m/s"}),
])
@pytest.mark.parametrize("repl,low,high", [
    ({}, 0.01,10),
    ({'range' : {'low': 11.0, 'high': 12.0}}, 11,12),
    ({'type': 'approx','approx' : {'target' : 10, 'pct': 10}}, 9,11),
])
def test_randomValue(repl,low,high,units):
    #print("\ntestrepl:",pformat(repl))
    x = DG.randomValue(repl)
    urepl = repl.copy()
    urepl.update(units)
    #print("urepl:",pformat(urepl), "units:",pformat(units))
    #print("test x:",pformat(x))
    assert isinrange(x['value'].magnitude,low,high)
    ux = DG.randomValue(urepl)
    assert isinrange(ux['value'].magnitude,low,high)
    assert str(ux['value'].units) == units['units']
    #print(pformat(str(ux)))

@pytest.mark.parametrize("number, answerstr", [
    #I use str because I don't want rounding errors in comparison
    ("0.10", "0.10" ),
    ("-200","-2e+2"),
    ("200.","2.00e+2"),
    ("4.003e-10","4.003e-10"),
])
def test_exactnumbers(number,answerstr):
    repl = {'type': 'exact','exact' : number}
    x = DG.randomValue(repl)
    assert str(x['value'].magnitude)==answerstr
