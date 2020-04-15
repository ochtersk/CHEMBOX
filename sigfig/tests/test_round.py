from CHEMBOX.sigfig.createsf import *
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize("test_input,rndto,output,outputsci,sf", [
    (1.2345678e+3,4,"0","0",0),
    (1.2345678e+3,5,"0","0",0),
    (12000,4,"1e+4","1e+4",1),
    (200,2,"2e+2","2e+2",1),
    (1.2345678e+3,3,"1e+3","1e+3",1),
    (1.2345678e+3,2,"1.2e+3","1.2e+3",2),
    (1.2345678e+3,1,"1.23e+3","1.23e+3",3),
    (1.2345678e+3,0,"1235","1.235e+3",4),
    (1.2345678e+3,-1,"1234.6","1.2346e+3",5),
    (1.2345678e+3,-2,"1234.57","1.23457e+3",6),
    (1.2345678e+3,-3,"1234.568","1.234568e+3",7),
    (1.2345678e+3,-4,"1234.5678","1.2345678e+3",8),
    (1.2345678e+3,-5,"1234.56780","1.23456780e+3",9),
    (1.2345678e+3,-6,"1234.567800","1.234567800e+3",10),

])
def test_round_loc(test_input,rndto,output,outputsci,sf):
    num = SciSigFig(test_input)
    num.round_digpos(rndto)
    assert str(num).lower() == output
    assert num.sfcount == sf
    scinum = SciSigFig(test_input, notation="scientific")
    scinum.round_digpos(rndto)
    assert str(scinum) == outputsci
    assert scinum.sfcount == sf


@pytest.mark.parametrize("test_input,rndto,output,outputsci,sf", [
    (1.2345678e+3,0,"0","0",0),
    (12000,4,"1.200e+4","1.200e+4",4),
    (200,3,"2.00e+2","2.00e+2",3),
    (1.2345678e+3,1,"1e+3","1e+3",1),
    (1.2345678e+3,2,"1.2e+3","1.2e+3",2),
    (1.2345678e+3,3,"1.23e+3","1.23e+3",3),
    (1.2345678e+3,4,"1235","1.235e+3",4),
    (1.2345678e+3,5,"1234.6","1.2346e+3",5),
    (1.2345678e+3,6,"1234.57","1.23457e+3",6),
    (1.2345678e+3,7,"1234.568","1.234568e+3",7),
    (1.2345678e+3,8,"1234.5678","1.2345678e+3",8),
    (1.2345678e+3,9,"1234.56780","1.23456780e+3",9),
    (1.2345678e+3,10,"1234.567800","1.234567800e+3",10),

])
def test_round_num(test_input,rndto,output,outputsci,sf):
    num = SciSigFig(test_input)
    num.round_numdig(rndto)
    #print(repr(num))
    assert str(num).lower() == output
    assert num.sfcount == sf
    scinum = SciSigFig(test_input, notation="scientific")
    scinum.round_numdig(rndto)
    assert str(scinum) == outputsci
    assert scinum.sfcount == sf

# now scientific notation input
@pytest.mark.parametrize("test_input,rndto,output,outputsci,sf", [
    (1.2345678e+3,4,"0","0",0),
    (1.2345678e+3,5,"0","0",0),
    (12000,4,"1e+4","1e+4",1),
    (200,2,"2e+2","2e+2",1),
    (1.2345678e+3,3,"1e+3","1e+3",1),
    (1.2345678e+3,2,"1.2e+3","1.2e+3",2),
    (1.2345678e+3,1,"1.23e+3","1.23e+3",3),
    (1.2345678e+3,0,"1235","1.235e+3",4),
    (1.2345678e+3,-1,"1234.6","1.2346e+3",5),
    (1.2345678e+3,-2,"1234.57","1.23457e+3",6),
    (1.2345678e+3,-3,"1234.568","1.234568e+3",7),
    (1.2345678e+3,-4,"1234.5678","1.2345678e+3",8),
    (1.2345678e+3,-5,"1234.56780","1.23456780e+3",9),
    (1.2345678e+3,-6,"1234.567800","1.234567800e+3",10),

])
def test_sround_loc(test_input,rndto,output,outputsci,sf):
    num = SciSigFig(test_input)
    num.round_digpos(rndto)
    assert str(num).lower() == output
    assert num.sfcount == sf
    scinum = SciSigFig(test_input, notation="scientific")
    scinum.round_digpos(rndto)
    assert str(scinum) == outputsci
    assert scinum.sfcount == sf


@pytest.mark.parametrize("test_input,rndto,output,outputsci,sf", [
    (1.2345678e+3,0,"0","0",0),
    (12000,4,"1.200e+4","1.200e+4",4),
    (200,3,"2.00e+2","2.00e+2",3),
    (1.2345678e+3,1,"1e+3","1e+3",1),
    (1.2345678e+3,2,"1.2e+3","1.2e+3",2),
    (1.2345678e+3,3,"1.23e+3","1.23e+3",3),
    (1.2345678e+3,4,"1235","1.235e+3",4),
    (1.2345678e+3,5,"1234.6","1.2346e+3",5),
    (1.2345678e+3,6,"1234.57","1.23457e+3",6),
    (1.2345678e+3,7,"1234.568","1.234568e+3",7),
    (1.2345678e+3,8,"1234.5678","1.2345678e+3",8),
    (1.2345678e+3,9,"1234.56780","1.23456780e+3",9),
    (1.2345678e+3,10,"1234.567800","1.234567800e+3",10),

])
def test_sround_num(test_input,rndto,output,outputsci,sf):
    num = SciSigFig(test_input)
    num.round_numdig(rndto)
    assert str(num).lower() == output
    assert num.sfcount == sf
    scinum = SciSigFig(test_input, notation="scientific")
    scinum.round_numdig(rndto)
    assert str(scinum) == outputsci
    assert scinum.sfcount == sf
