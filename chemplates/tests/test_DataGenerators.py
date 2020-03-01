import pytest
from pprint import pformat
import chemplates.DataGenerators as DG
import refdata.DataValue as DV

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
def test_random_value(repl,low,high,units):
    #print("\ntestrepl:",pformat(repl))
    x = DG.random_value(repl)
    urepl = repl.copy()
    urepl.update(units)
    #print("urepl:",pformat(urepl), "units:",pformat(units))
    #print("test x:",pformat(x))
    assert isinrange(x['value'].magnitude,low,high)
    ux = DG.random_value(urepl)
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
    x = DG.random_value(repl)
    assert str(x['value'].magnitude)==answerstr


@pytest.mark.parametrize("expression, vars, answer", [
    #I use str because I don't want rounding errors in comparison
    ("1+2",{},3 ),
    ("one + two", {'one' : DV.DataValue("1"), 'two': DV.DataValue("2")}, DV.DataValue("3")),
    ("one + two", {'one' : DV.DataValue("1 g"), 'two': DV.DataValue("2 g")}, DV.DataValue("3 g")),
])
def test_parser(expression, vars, answer ):
    x = DG.parse_expression(expression, vars)
    print("test_parser x:",pformat(x))
    assert str(x) == str(answer)


@pytest.mark.parametrize("template, vars, answer", [
    ("1+2",{"a" : "1"}, "1+2" ),
    ("1+{{a}}",{"a" : "1"}, "1+1" ),
])
def test_fill_template(template, vars, answer ):
    x = DG.fill_template(template, vars)
    print("test_fill_template x:",pformat(x))
    assert str(x) == str(answer)

@pytest.mark.parametrize("text, answer", [
    ("1+2", "1+2" ),
    ("dog cat chicken", "dog cat chicken" ),
])
def test_copy_text(text, answer ):
    x = DG.copy_text(text)
    print("test_copy_text x:",pformat(x))
    assert str(x) == str(answer)
