from sigfig.createsf import *
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize("a,operator,b,answer", [
    ("1.23","+","2.1","3.3"),
    ("1.2","+","2.14","3.3"),
    ("1.23","+","2.15","3.38"),
    ("1.234e+1","+","2.15","14.49"),
    ("1.23e+1","+","2.15","14.4"),
    ("1.23e+1","+","2.16","14.5"),
    ("1.23e+1","+","2.15e+0","14.4"),
    ("1.23e+1","+","2.16e+0","14.5"),
    ("1.23","-","2.1","-0.9"),
    ("1.2","-","2.14","-0.9"),
    ("1.23","-","2.15","-0.92"),
    ("1.234e+1","-","2.15","10.19"),
    ("1.23e+1","-","2.15","10.2"),
    ("1.23e+1","-","2.16","10.1"),
    ("1.23e+1","-","2.15e+0","10.2"),
    ("1.23e+1","-","2.16e+0","10.1"),
])
def test_addsub(a,operator,b,answer):
    aa = SciSigFig(a)
    ba = SciSigFig(b)
    res=0
    if operator == "+":
        res, rnd_to = aa.add(ba)
        print("ADD:",aa,"+",ba, "round to:",rnd_to)
    elif operator == "-":
        res, rnd_to = aa.subtract(ba)
        print("SUB:",aa,"-",ba, "round to:",rnd_to)
    else:
        pass

    res.round_digpos(rnd_to)
    print("result:\n", repr(res))
    assert str(res) == answer


@pytest.mark.parametrize("a,operator,b,answer", [
    ("1.23","*","2.1","2.6"),
    ("1.2","*","2.14","2.6"),
    ("1.23","*","2.15","2.64"),
    ("1.234e+1","*","2.15","26.5"),
    ("1.23e+1","*","2.15","26.4"),
    ("1.23e+1","*","2.16","26.6"),
    ("1.23e+1","*","2.15e+0","26.4"),
    ("1.23e+1","*","2.16e+0","26.6"),
    ("1.23","/","2.1","0.59"),
    ("1.2","/","2.14","0.56"),
    ("1.23","/","2.15","0.572"),
    ("1.234e+1","/","2.15","5.74"),
    ("1.23e+1","/","2.15","5.72"),
    ("1.23e+1","/","2.16","5.69"),
    ("1.23e+1","/","2.15e+0","5.72"),
    ("1.23e+1","/","2.16e+0","5.69"),
])
def test_muldiv(a,operator,b,answer):
    aa = SciSigFig(a)
    ba = SciSigFig(b)
    res=0
    if operator == "*":
        res, rnd_to = aa.multiply(ba)
        print("MUL:",aa,"*",ba, "round to:",rnd_to)
    elif operator == "/":
        res, rnd_to = SciSigFig.divide(aa,ba)
        print("DIV:",aa,"/",ba, "round to:",rnd_to)
    else:
        pass

    res.round_numdig(rnd_to)
    print("result:\n", repr(res))
    assert str(res) == answer
