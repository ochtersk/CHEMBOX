from sigfig.createsf import *
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize("test_input,sfcode,sfid", [
    ("0.312","LDSSS", "NNSSU" ),
    ("0.00312", "LDLLSSS","NNNNSSU"),
    ("0.0302", "LDLSMS", "NNNSSU"),
    ("0.83100000","LDSSSTTTTT","NNSSSSSSSU"),
    ("0.030200", "LDLSMSTT","NNNSSSSU"),
    ("302", "SMS", "SSU"),
    ("312", "SSS", "SSU"),
    ("312.", "SSSD", "SSUN"),
    ('0.00026040460','LDLLLSSMSMSST','NNNNNSSSSSSSU'),
    ("30200", "SMSNN", "SSUNN"),
    ("30200.", "SMSTTD", "SSSSUN"),
])
def test_create(test_input,sfcode,sfid):
    num = SciSigFig(test_input)
    assert num.sfcode == sfcode
    assert num.sfid == sfid



@pytest.mark.parametrize("exp_in",[3,1,-4])
@pytest.mark.parametrize("nsf_in", [2,6,8])
@pytest.mark.parametrize("ztypes_in",["","L","M","T","LM","LT","MT","LMT","N"])
def test__determine_num_zeros(exp_in,nsf_in,ztypes_in):
    (L0,M0,T0, nsf, exp) = SciSigFig._determine_num_zeros(nsf_in,ztypes_in,exp_in)
    n_not0 = 0
    if 'L' in ztypes_in:
        assert L0 >= 1
        assert exp <= -L0
    if 'M' in ztypes_in:
        assert M0 >= 1
        n_not0 = 2
    if 'T' in ztypes_in:
        assert T0 >= 1
        n_not0 =1
    if 'N' in ztypes_in:
        assert T0 + M0 + L0 == 0
        n_not0 = nsf
    assert M0+T0+n_not0 <= nsf




@pytest.mark.parametrize("digits,T0,digits_out", [
    ([1,2,3,4,5,6,7], 1, [1,2,3,4,5,6,0]),
    ([1,2,3,4,5,6,7], 2, [1,2,3,4,5,0,0]),
    ([1,2,3,4,5,6,7], 3, [1,2,3,4,0,0,0]),
    ([1,2,3,4,5,6,7], 4, [1,2,3,0,0,0,0]),
    ([1,2,3,4,5,6,7], 5, [1,2,0,0,0,0,0]),
    ([1,2,3,4,5,6,7], 6, [1,0,0,0,0,0,0]),
])
def test__repl_with_T0(digits,T0, digits_out):
    SciSigFig._repl_with_T0(digits,T0)
    assert digits == digits_out

@pytest.mark.parametrize("digits,M0,T0", [
    ([1,2,3,4,5,6,7], 1, 1),
    ([1,2,3,4,5,6,7], 2, 2),
    ([1,2,3,4,5,6,7], 3, 0),
    ([1,2,3,4,5,6,7], 4, 1),
    ([1,2,3,4,5,6,7], 5, 0),
    ([1,2,3,4,5,6,7], 2, 0),
])
def test__repl_with_M0(digits,M0, T0):
    SciSigFig._repl_with_M0(digits,M0,T0)
    assert digits.count(0) == M0

@pytest.mark.parametrize("digits,M0,T0", [
    ([1,2,3,4,5,6,7], 1, 1),
    ([1,2,3,4,5,6,7], 2, 2),
    ([1,2,3,4,5,6,7], 3, 0),
    ([1,2,3,4,5,6,7], 4, 1),
    ([1,2,3,4,5,6,7], 0, 5),
    ([1,2,3,4,5,6,7], 2, 0),
])
def test__repl_with_M0_and_T0(digits,M0, T0):
    SciSigFig._repl_with_T0(digits,T0)
    SciSigFig._repl_with_M0(digits,M0,T0)
    assert digits.count(0) == M0 + T0


def _validate_number(nsf,exp,ztypes,numberstr):
    """ check if a number generated by SciSigFig.generate meets all the criteria
    This can be a bit tricky, because generate plays with nsf and exp to make
    sure ztypes (LMT) is satisfied.
    """
    number = Decimal(numberstr)
    valid = True
    print("VALID exp,nsf,ztypes numberstr:" +str(exp) + " " + str(nsf) + " " + str(ztypes) + " " + numberstr)
    if ztypes is None:
        ztypes = '' #no expectations for zeros
    if exp is None:
        exp_range=SciSigFig.default_exp()
        exp_lo, exp_hi = exp_range[0],exp_range[1]+1
    else:
        exp_lo = exp
        exp_hi = exp + 1
    if nsf is None:
        nsf_lo, nsf_hi=SciSigFig.default_nsf()
    else:
        nsf_lo, nsf_hi = (nsf,nsf)
    print("NSF range:" + ",".join([str(nsf_lo),str(nsf_hi)]))
    range_hi = Decimal((0,tuple([1]),exp_hi))
    range_lo = Decimal((0,tuple([1]),exp_lo))
    if 'L' in ztypes:
        print("L exp,nsf:" +str(exp_lo) + " " + str(nsf))
        if (number < 10**(-8) or number > 10**0):
            print("Leading zero number out of range:" + " ".join([str(10**-8),numberstr,str(10**0)]))
            valid = False
    elif (number > range_hi or number < range_lo):
        #print("number out of range:" + " ".join([str(range_lo),numberstr,str(range_hi)]))
        print("number out of range:")
        print(str(range_lo))
        print(numberstr)
        print(str(range_hi))
        valid = False
    sf = SciSigFig(numberstr)
    sf_count = sf.sfcount
    if 'M' in ztypes and nsf_lo < 3:
        nsf_lo = 3
        nsf_hi = 3
        if 'T' in ztypes and nsf_lo < 4:
            nsf_lo = 4
            nsf_hi = 4
    if not (sf_count >= nsf_lo and sf_count <= nsf_hi):
        valid = False
        print("nsf not met(nsf_lo,count,nsf_hi):" + ",".join([str(nsf_lo),str(sf_count),str(nsf_hi)]))
    if ('L' in ztypes and 'L' not in sf.sfcode):
        valid = False
        print("No leading zeros found in:" + ",".join([numberstr,sf.sfcode]))
    if ('M' in ztypes and 'M' not in sf.sfcode):
        valid = False
        print("No middle zeros:" + ",".join([numberstr,sf.sfcode]))
    if ('T' in ztypes and 'T' not in sf.sfcode):
        valid = False
        print("No trailing zeros:" + ",".join([numberstr,sf.sfcode]))
    if ('N' in ztypes):
        for i in range(sf_count):
            if numberstr[i] == 0:
                valid = False
                print("found zero in number, no zeros requested:" + ",".join([numberstr,sf.sfcode]))
    return valid

@pytest.mark.parametrize("nsf_in,exp_in,ztypes_in,number,result",[
(2,1,'T','80.',True),
(2,1,'T','80',False),
(1,1,'N','80',True),
(2,1,'N','81',True),
(1,1,'','80',True),
(2,-4,'LT', '0.00010', True),
])
def test_validate_number(nsf_in,exp_in,ztypes_in,number,result):
    assert _validate_number(nsf_in,exp_in,ztypes_in,number)==result


@pytest.mark.parametrize("exp_in",[3,1,-4])
@pytest.mark.parametrize("nsf_in", [2,6,8])
@pytest.mark.parametrize("notate",['regular'])
@pytest.mark.parametrize("ztypes_in",[None, "","L","M","T","MT","LM","LT","LMT","N"])
def test_generate(exp_in,ztypes_in,nsf_in,notate):
    #number = SciSigFig.generate(exp_range,"regular",ztypes,nsf_range)
    number = SciSigFig.generate(
        exp_range=(exp_in,exp_in),
        notation= notate,
        ztypes=ztypes_in,
        nsf_range=(nsf_in,nsf_in)
        )
    valid = _validate_number(nsf_in,exp_in,ztypes_in,number)
    assert valid


@pytest.mark.parametrize("ztypes_in",["","M","T","MT"])
@pytest.mark.parametrize("exp_in",[3,1,-4])
@pytest.mark.parametrize("nsf_in", [2,6,8])
@pytest.mark.parametrize("notate",['scientific'])
def test_generate1(exp_in,ztypes_in,nsf_in,notate):
    #number = SciSigFig.generate(exp_range,"regular",ztypes,nsf_range)
    number = SciSigFig.generate(
        exp_range=(exp_in,exp_in),
        notation= notate,
        ztypes=ztypes_in,
        nsf_range=(nsf_in,nsf_in)
        )
    valid = _validate_number(nsf_in,exp_in,ztypes_in,number)
    assert valid


@pytest.mark.parametrize("ztypes_in",[None,"","L","M","T","MT","LM","LT","LMT","N"])
@pytest.mark.parametrize("ntype",[None,"","regular","scientific"])
def test_generate_ztypes_defaults(ztypes_in,ntype):
    #number = SciSigFig.generate(exp_range,"regular",ztypes,nsf_range)
    number = SciSigFig.generate(
        ztypes=ztypes_in,
        notation = ntype,
        )
    valid = _validate_number(None,None,ztypes_in,number)
    if ntype == 'scientific':
        valid = 'e' in number
    print("number:" + number + " ntype:" + str(ntype))
    #valid = True
    #XXX fix this test
    assert valid == True
