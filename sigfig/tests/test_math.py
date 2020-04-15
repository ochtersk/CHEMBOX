from CHEMBOX.sigfig.createsf import *
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize("overload",[0,1])
@pytest.mark.parametrize("a,operator,b,answer", [
    ("1.23","+","2.1","3.3"),
    ("2.23","+","-1.1","1.1"),
    ("-2.23","+","-1.1","-3.3"),
    ("2.23","+","-3.3","-1.1"),
    ("1.2","+","2.14","3.3"),
    ("1.23","+","2.15","3.38"),
    ("1.234e+1","+","2.15","14.49"),
    ("1.23e+1","+","2.15","14.4"),
    ("1.23e+1","+","2.16","14.5"),
    ("1.23e+1","+","2.15e+0","14.4"),
    ("1.23e+1","+","2.16e+0","14.5"),
    ("1.23","-","-2.1","3.3"),
    ("1.23","-","2.1","-0.9"),
    ("1.2","-","2.14","-0.9"),
    ("1.23","-","2.15","-0.92"),
    ("1.234e+1","-","2.15","10.19"),
    ("1.23e+1","-","2.15","10.2"),
    ("1.23e+1","-","2.16","10.1"),
    ("1.23e+1","-","2.15e+0","10.2"),
    ("1.23e+1","+","-2.16e+0","10.1"),
])
def test_addsub(a,operator,b,answer,overload):
    aa = SciSigFig(a)
    ba = SciSigFig(b)
    res=0
    if operator == "+":
        if overload:
            res = aa+ba
        else:
            res = aa.add(ba)
        #print("ADD:",aa,"+",ba, "round to:",res.sfcount)
    elif operator == "-":
        if overload:
            res = aa-ba
        else:
            res = aa.subtract(ba)
        #print("SUB:",aa,"-",ba, "round to:",res.sfcount)
    else:
        pass
    #print("result:\n", repr(res))
    assert str(res) == answer

@pytest.mark.parametrize("overload",[0,1])
@pytest.mark.parametrize("a,operator,b,answer", [
    ('10.00',"/",'2.00','5.00'),
    ("1.23","*","2.1","2.6"),
    ("1.23","*","-2.1","-2.6"),
    ("-1.23","*","2.1","-2.6"),
    ("-1.23","*","-2.1","2.6"),
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
def test_muldiv(a,operator,b,answer,overload):
    aa = SciSigFig(a)
    ba = SciSigFig(b)
    res=0
    if operator == "*":
        if overload:
            res = aa*ba
        else:
            res = aa.multiply(ba)
        #print("MUL:",aa,"*",ba, "round to:", res.sfcount)
    elif operator == "/":
        if overload:
            res = aa/ba
        else:
            res = SciSigFig.divide(aa,ba)
        #print("DIV:",aa,"/",ba, "round to:",res.sfcount)
    else:
        assert False, "bad operator:"+operator
    #print("result:\n", repr(res))
    assert str(res) == answer



def test_math_chaining():
    #print("CHAIN-------------------------------------------------")
    aa = SciSigFig("23.72")
    ba = SciSigFig("22.72")
    ca = SciSigFig("2.345678")
    res1 = (aa-ba)
    #print("result1:\n", repr(res1), "\nround to:", res1.sfcount)
    res = (aa-ba)/ca
    #print("result2:\n", repr(res), "\nround to:", res.sfcount)
    assert str(res) == "0.426"



def test_exactnumbers_normal():
    aa = SciSigFig("1",exact = True)
    #print("exact repr:\n", repr(aa),"\n exact str",str(aa))
    assert str(aa) == '1.0000000000000000000'

def test_exactnumbers_exp():
    aa = SciSigFig("6.02214076e23",exact = True)
    #print("exact repr:\n", repr(aa),"\n exact str",str(aa))
    assert str(aa) == '6.0221407600000000000e+23'

def test_exactnumbers_defined_constants():
    aa = SciSigFig("AVOGADRO")
    #print("exact repr:\n", repr(aa),"\n exact str",str(aa))
    assert str(aa) == '6.0221407600000000000e+23'



@pytest.mark.parametrize("exactnum,floatnum,multans,divans,divans2", [
    ("2","6.68","13.4","0.299","3.34"),
])
def test_exactmath(exactnum,floatnum,multans,divans,divans2):
    #print("---------EXACT MATH--------\n")
    exact = SciSigFig(exactnum,exact = True)
    flt = SciSigFig(floatnum)
    mulres = exact*flt
    #print("mulres:\n", repr(mulres), "\nround to:", mulres.sfcount)
    assert str(mulres) == multans
    divres = exact/flt
    assert str(divres) == divans
    divres2 = flt/exact
    assert str(divres2) == divans2
