from decimal import *
from random import *

class SciSigFig:
    """
    This class implements Scientific significant digits math, like you learned
    in high school (or college science class), like this:
    http://chemistry.bd.psu.edu/jircitano/sigfigs.html.

    Properties
    ----------
        number = a Decimal representation of the number. This is used for all
            the math.
        sfcode = a code with a character for each type of digit or character in
            the string representation of the number
            S=significant, L=leading 0, M=middle 0 T=trailing 0, D=decimal,
            s = sign
        sfid = a code with an identifier for the type of digit it is
            S=sig, N=nonsig, U=uncertain
        sfcount = the number of significant digits in the number. It is the
            number of sf in the incoming number if it is supplied. If not,
            the number is assumed to come from a calculation, where self.number will
            be set to the full precision calculated value, and the number of sf is
            set (via the force_sfcount method) to the number of sf the number should
            have on representation. This allows calculations to be chained together
            like (a-b)/c, and the sf will be done right.
        uexp = the location of the uncertain digit as an exponent of 10 (-1=0.1)
        notation = whether thios number should be represeted in normal or
            scientific notation

        Public Methods
        --------------
        __init__(numstring, notation="normal", exact=False)
            turns numstring into a number. If (optional) exact is True, then the
            number is stored with (right now) 20 digits. The optional notation
            parameter turns of scientific notation if it is set to "scientific".
        __str__ returns a representation (either normal or scientific) of the
            number to the number of sf in sfcount.
        __repr__ returns a list of the values of all the Properties
        default_exp returns a default range of powers of 10 a randomly generated
            number should fall in. Currently returns (-3,5)
        default_nsf returns a default range for the number of sf in a
            random number. Currently returns (4,8)
        generate(exp_range=None,notation="regular",ztypes=None,nsf_range=None)
            generates a random number with the characteristic specified.
            all parameters are optional
            exp_range is a tuple with the range of the number (as powers of 10)
            notation is "normal" or "scientific"
            ztypes is the types of zeros that should be in the number
                L = leading, M = middle, T = trailing or N for no zeroes.
                L doesn't make sense for scienitifc notation.
            nsf_range is the range of number of sf to use
        round_digpos(position)
            round the number to the nearest 10^-position
        round_numdig(numdig)
            round the number to a particular number of digits
        force_sfcount(n_sigfig)
            force sfcount to a particular value - this only affects how the
            number is represented as a string, not how it is represented internally
        add(addend)
        __add__(addend)
            return a new SciSigFig which is the sum of two SciSigFig's. The new
            number is stored with full precision, but sfcount is set to the
            proper value given the sf in the addends.
        subtract(subtrahend)
        __sub__(subtrahend)
            return a new SciSigFig which is the subtraction of two SciSigFig's. The new
            number is stored with full precision, but sfcount is set to the
            proper value given the sf in the terms.
        multiply(mult)
        __mul__(mult)
            return a new SciSigFig which is the product of two SciSigFig's. The new
            number is stored with full precision, but sfcount is set to the
            proper value given the sf in the terms.
        divide(denom)
        __truediv__(denom)
            return a new SciSigFig which is the division of two SciSigFig's. The new
            number is stored with full precision, but sfcount is set to the
            proper value given the sf in the terms.

    """
    EXACTPRECISION = 20 # the precision of "exact" numbers
    defined_constants = {
        'AVOGADRO' : '6.02214076e+23'
        }
    # these are any predefined constant we'd like to use they are assumed to
    # be exact
    def __init__(self,numstring, notation="normal", exact=False):
        if numstring in SciSigFig.defined_constants.keys():
            numstring = SciSigFig.defined_constants[numstring]
            exact = True
        self.number = Decimal(numstring)
        if exact:   # force the number to have plenty of digits
            sign,digits,dec_exp = self.number.as_tuple()
            zeros_to_add = SciSigFig.EXACTPRECISION -len(digits)
            zeroes = tuple([0]*zeros_to_add)
            newdigits = digits+zeroes
            newexp = dec_exp-zeros_to_add
            self.number = Decimal((sign,newdigits,newexp))
            numstring = str(self.number)
        self.sfcode = '' # holds specific character type
                         # S=sig, L=leading0, M=middle0 T=trailing0, D=decimal
        self.sfid = '' # holds type of each digit S=sig, N=nonsig, U=uncerttain
        self.sfcount = 0 # total nummer of sig digits
        self.uexp = 0 # exponent of the uncertain digit position
        self.notation= notation
        self._sfcode(str(numstring))
        return None

    def __repr__(self):
        numstr = str(self.number)
        return ' number:%s\n str(number):%s\n      sfcode:%s\n        sfid:%s\n     sfcount:%s\n        uexp:%s\n    notation:%s' % \
            (self.number,numstr, self.sfcode,self.sfid,self.sfcount,self.uexp,self.notation)

    def __str__(self):
        verbose = False
        numstr = ''
        nsf = self.sfcount
        notation = self.notation
        sign,digits,dec_exp = self.number.as_tuple()
        position = (len(digits)+dec_exp) - nsf
        if verbose: print("\nnotation:",notation)
        if (dec_exp==0) and (len(digits)==nsf) and (digits[-1]==0):
            notation = "scientific"
            if verbose: print("forcing scinetific notation")
        if notation == 'scientific':
            if nsf>0:
                format_str = "{:."+str(nsf-1)+"e}"
                #print("__str__ format:",format_str)
                numstr = format_str.format(self.number)
            else:
                numstr= "0"
        else:
            numstr = str(round(self.number,-position))
            if verbose: print("\nnormal notation:", numstr, " pos:",position, "nfs:",nsf)
        return numstr

    def _sfcode(self,numstring): # takes a Decimal representation
        verbose = 0
        ztypes = ('L','M','T') # Leading, Middle, Trailing
        zt_idx = 0 # pointer to the type of zero we are looking at
        number = self.number
        sfcode = []
        n_zeros = 0
        n_char = 0
        has_decimal = "." in numstring
        for character in numstring:
            if verbose >=3:
                print("char:",character,numstring)
            if character == 'e' or character == 'E':
                self.notation = "scientific"
                break # we've hit the end of the mantissa
            elif character == '0':
                sfcode.append(ztypes[zt_idx])
                n_zeros += 1
            elif character == '.':
                sfcode.append('D')
                has_decimal = True
            elif character == '-':
                sfcode.append('s')
                continue
            else: # assuming [1-9] here
                sfcode.append('S')
                if n_zeros > 0 or (n_char == 0):
                    zt_idx = 1  # all non-leading zeros are marked M then fixed later
                                # this is to account for multiple sets of zeros, like
                                # 0.0305050
                    n_zeros = 0 # reset counter
            n_char += 1
            if verbose>2:
                print("1nchar:",n_char," char:",character + ":" + ''.join(sfcode))
                print("1zt_idx:", zt_idx, " n_zeros:", n_zeros)
        found_M=True
        allzeros ='D' in sfcode and (sfcode[-1] == 'L') # L in the last digit means only zeros, like 0.00
        for index in range(len(sfcode)-1,-1,-1):
            if allzeros and sfcode[index] == "L":
                sfcode[index] = 'T'
                continue
            if sfcode[index] != 'M' and sfcode[index] != 'D' :
                break
            elif sfcode[index] == 'D':
                if allzeros:
                    break
                else:
                    continue
            else:
                sfcode[index] = 'T'
        if verbose>2:
            print("2nchar:",n_char," char:",character + ":" + ''.join(sfcode))
        sfid = []
        sfcount = 0
        for character in sfcode:
            if not has_decimal and character == 'T': # trailing zeros not sig unless decimal
                sfid.append('N')
            elif (character in ('S','M','T')):
                sfid.append('S')
                sfcount += 1
            elif character == "D":
                sfid.append('.')
            else:
                sfid.append('N')
            #print("sfid:",sfid," char:",character)

        for index in range(len(sfid)-1,-1,-1): #last SF is uncertain
            if sfid[index] == 'S':
                upos= len(sfid)-index
                __, __, dec_exp = number.as_tuple()
                uexp=dec_exp + upos - 1
                sfid[index] = 'U'
                self.uexp=uexp
                if verbose>1:
                    print(numstring + " upos:" + str(upos) + " dec_exp" + str(dec_exp) + " uexp:" + str(uexp))

                break
            else:
                pass
        if (verbose>0):
            print(">"  + ":" + numstring)
            print("C" + ":" + ''.join(sfcode))
            print("I" + ":" + ''.join(sfid)) # S =sig, N=nonsig U=uncertain
        self.sfcode = ''.join(sfcode)
        self.sfid = ''.join(sfid)
        self.sfcount = sfcount
        return self

    def _determine_num_zeros(nsf,ztypes,exp):
        """
        Notes:
        1) this routine will change nsf in order to comply with zero types request
        2) if leading zeros are requested, and exp is positive, it will be changed
           to the largest value which will still get leading L0 zeros (rnd(1,5))
        """
        L0=0 # number of leading zeros
        M0=0 # number of middle zeros
        T0=0 # number of training zeros

        if 'L' in ztypes:
            if exp > -1:
                L0=randint(1,5) # between 1 and 5 leading zeros
                exp = -L0 #make it 10^-L0
            else:
                L0 = -exp
                #print("update exp:"+str(exp) + "L0:" + str(L0))
        if ('M' in ztypes and
            'T' in ztypes):
            if nsf < 4:
                nsf = 4 # with middle and trailing zeros, we need at least 4 SF
            T0 = randint(1,nsf-3)
            M0 = randint(1,nsf-2-T0)
        elif 'M' in ztypes:
            if nsf < 3:
                nsf = 3
            M0 = randint(1,nsf-2)
        elif 'T' in ztypes:
            T0 = randint(1,nsf-1)
        return (L0,M0,T0,nsf,exp)

    def _repl_with_T0(digits,T0): # replace the last T0 digits with 0s
        end = len(digits)
        for i in range(end-T0,end):
            digits[i] = 0
        #print("digits:" + str(digits))

    def _repl_with_M0(digits,M0, T0=0): # replace the last T0 digits with 0s
        if M0 == 0:
            return
        end = len(digits)
        low = 1 # lowest position to start replacement
        high = end - T0 - M0 - 1# last possible starting position
        #print("lo, hi:" + str(low) + " " + str(high))
        start = randint(low,high)
        for i in range(start,start+M0):
            digits[i] = 0
        #print("digits:" + str(digits))

    def default_exp():
        return (-3,5)

    def default_nsf():
        return (4,8)

    def generate(exp_range=None,notation="regular",ztypes=None,nsf_range=None):

        if exp_range is None:
            exp_range = SciSigFig.default_exp()
        exp = randint(*exp_range)
        #print()
        #print( "exp" + str(exp_range) + " = " + str(exp))
        if nsf_range is None:
            nsf_range = SciSigFig.default_nsf()
        nsf = randint(*nsf_range)
        #print( "nsf" + str(nsf_range) + " = " + str(nsf))
        digits = [randint(1,9)]
        if ztypes is None: #this needs more thought about L: M: T:
            digits.extend([ randint(0,9) for i in range(nsf-1) ])
            ztypes =""
            #number = Decimal((0,tuple(digits),exp))
            #print("ztypes(None):" + ztypes)
        elif 'N' in ztypes: # guarantee no significant zeros
            digits.extend([ randint(1,9) for i in range(nsf-1) ])

        else:
            (L0,M0,T0,nsf,exp) =SciSigFig._determine_num_zeros(nsf,ztypes,exp)
            digits.extend([ randint(1,9) for i in range(nsf-1) ])


        #print("start digits:" + str(digits))

            SciSigFig._repl_with_T0(digits,T0)
            SciSigFig._repl_with_M0(digits,M0,T0)
        # print("ztypes:" + ztypes + " L0:"+str(L0)+" M0:"+
        #         str(M0)+" T0:"+str(T0) + " nsf:" + str(nsf)+
        #         " exp:" + str(exp))
            #number = Decimal(0,tuple(digits),exp)
        dec_exp = -len(digits)+exp+1
        t= (0,tuple(digits),dec_exp)
        number = Decimal(t)
        strnumber = str(number)
        #print("ztypes:" + ztypes + " " + strnumber)
        if(exp >= 1 and nsf-exp ==1):
            strnumber +="." #append a decimal, because Decimal doesn't :/
        elif (exp >= 1 and nsf<exp and 'T' not in ztypes and ztypes != ''):
            format_str = "{:.0f}"
            strnumber = format_str.format(number)
        #print("XDecimals number:" + strnumber + notation)

        if (notation == 'scientific'):
                format_str = "{:."+str(nsf-1)+"e}"
                strnumber = format_str.format(number)

        #print("FDecimals number:" + " = " + str(number))
        #print("--------------")
        return strnumber

    def approximate_magnitude(target=10.0,percent=10.0,nsf_range=None):
        diff = random()*percent/100.0*target
        sign = 1 if random() < 0.5 else -1
        magnitude = target + sign*diff
        if nsf_range is None:
            nsf_range = [3,5]
        nsf = randint(*nsf_range)
        new = SciSigFig(str(magnitude))
        new.round_numdig(nsf)
        return new

    def in_range(low=0.01,high=20.0,nsf_range=None):
        magnitude = uniform(low,high)
        if nsf_range is None:
            nsf_range = [3,5]
        nsf = randint(*nsf_range)
        new = SciSigFig(str(magnitude))
        new.round_numdig(nsf)
        return new


    def round_digpos(self,position):
        #print("self:",str(self))
        #print("repr:\n"+repr(self))
        comp =Decimal("1e"+str(position))
        roundnumstr = str(self.number.quantize(comp))
        roundnum = SciSigFig(roundnumstr)
        result = self._sfcode(str(roundnum.number))

    def round_numdig(self,numdig):
        verbose = False
        sign,digits,dec_exp = self.number.as_tuple()
        if verbose: print("tuple:",str(sign),str(digits),str(dec_exp),"\n")
        exp = len(digits)+dec_exp
        position = exp - numdig
        comp = Decimal("1e"+str(position))
        if verbose: print("position:",position," = exp:",exp," - numdig:",numdig,  "comp:",comp)
        rndnum =Decimal(self.number).quantize(comp)
        if verbose: print(" rndnum:",str(rndnum))
        if verbose: print("repr:\n"+repr(rndnum))
        # i used -position because I want to round to nearest 10^-position
        self.number = rndnum
        result = self._sfcode(str(rndnum))
        self.sfcount = numdig

    def force_sfcount(self,n_sigfig):
        self.sfcount = n_sigfig

# now for math methods

    def add(self,addend):
        max_uexp = max(self.uexp,addend.uexp)
        result = SciSigFig(self.number + addend.number)
        #print("\n>>add1:", max_uexp, "\n--result:",repr(result))
        roundnumstr = str(round(result.number,-max_uexp))
        temp = SciSigFig(roundnumstr)
        #print("\n>>add2:", roundnumstr, "\n--temp:",repr(temp))
        n_sigfig = temp.sfcount
        result.force_sfcount(n_sigfig)
        return (result)

    def __add__(self,addend):
        return self.add(addend)


    def subtract(self,sub):
        max_uexp = max(self.uexp,sub.uexp)
        result = SciSigFig(self.number - sub.number)
        #print("\n>>sub1:", max_uexp, "\n--result:",repr(result))
        roundnumstr = str(round(result.number,-max_uexp))
        temp = SciSigFig(roundnumstr)
        #print("\n>>sub2:", roundnumstr, "\n--temp:",repr(temp))
        n_sigfig = temp.sfcount
        result.force_sfcount(n_sigfig)
        return (result)

    def __sub__(self,subtrahend):
        return self.subtract(subtrahend)

    def multiply(self,mult):
        min_sf = min(self.sfcount,mult.sfcount)
        #print("operands:",self.number, mult.number)
        result = SciSigFig(self.number * mult.number)
        #print("multiply answer:",repr(result))
        result.force_sfcount(min_sf)
        return (result)

    def __mul__(self,mult):
        return self.multiply(mult)

    def divide(self,mult):
        min_sf = min(self.sfcount,mult.sfcount)
        result = SciSigFig(self.number / mult.number)
        #print("answwer:",str(result))
        result.force_sfcount(min_sf)
        return (result)

    def __truediv__(self,denom):
        return self.divide(denom)
