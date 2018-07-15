from decimal import *
from random import *

class SciSigFig:

    def __init__(self,numstring, notation="normal"):
        self.number = Decimal(numstring)
        self.sfcode = '' # holds specific character type
                         # S=sig, L=leading0, M=middle0 T=trailing0, D=decimal
        self.sfid = '' # holds type of each digit S=sig, N=nonsig, U=uncerttain
        self.sfcount = 0 # total nummer of sig digits
        self.uexp = 0 # exponent of the uncertain digit position
        self.notation= notation
        result = self._sfcode(str(numstring))
        return None

    def __repr__(self):
        numstr = str(self)
        return ' number:%s\n sfcode:%s\n   sfid:%s\n fcount:%s\n   uexp:%s\n notation:%s' % \
            (numstr, self.sfcode,self.sfid,self.sfcount,self.uexp,self.notation)

    def __str__(self):
        numstr = ''
        if self.notation == 'scientific':
            nsf = self.sfcount
            if nsf>0:
                format_str = "{:."+str(nsf-1)+"e}"
                print("__str__ format:",format_str)
                numstr = format_str.format(self.number)
            else:
                numstr= "0"
        else:
            numstr = str(self.number)
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
            else: # assuming [1-9] here
                sfcode.append('S')
                if n_zeros > 0 or (n_char == 0):
                    zt_idx = 1  # all non-leading zeros are marked M then fixed later
                                # this is to account for multiple sets of zeros, like
                                # 0.0305050
                    n_zeros = 0 # reset counter
            n_char += 1
            if verbose>2:
                print(character + ":" + ''.join(sfcode))
        found_M=True
        for index in range(len(sfcode)-1,-1,-1):
            if sfcode[index] != 'M' and sfcode[index] != 'D' :
                break
            elif sfcode[index] == 'D':
                continue
            else:
                sfcode[index] = 'T'

        sfid = []
        sfcount = 0
        for index in range(len(sfcode)):
            character = sfcode[index]
            if not has_decimal and character == 'T':
                sfcode[index]='N'
                character= 'N'
            if (character in ('S','M','T')):
                sfid.append('S')
                sfcount += 1
            else:
                sfid.append('N')
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

#   XXX TODO def set_rounding_type

    def round_digpos(self,position):
        #print("position:",position)
        #print("self:",str(self))
        #print("repr:\n"+repr(self))
        rndnum = SciSigFig(round(self.number,-position))
        # i used -position because I want to round to nearest 10^-position
        self.number = rndnum.number
        result = self._sfcode(str(rndnum.number))

    def round_numdig(self,numdig):
        sign,digits,dec_exp = self.number.as_tuple()
        position = (len(digits)+dec_exp) - numdig
        print("position:",position," = - exp:",(len(digits)+dec_exp)," - numdig:",-numdig)
        #print("self:",str(self))
        #print("repr:\n"+repr(self))
        rndnum = SciSigFig(round(self.number,-position))
        print(" rndnum:",str(rndnum))
        print("repr:\n"+repr(rndnum))
        # i used -position because I want to round to nearest 10^-position
        self.number = rndnum.number
        result = self._sfcode(str(rndnum.number))


# now for math methods

    def add(self,addend):
        max_uexp = max(self.uexp,addend.uexp)
        result = SciSigFig(self.number + addend.number)
        return (result,max_uexp)

    def subtract(self,sub):
        max_uexp = max(self.uexp,sub.uexp)
        result = SciSigFig(self.number - sub.number)
        return (result,max_uexp)

    def multiply(self,mult):
        min_sf = min(self.sfcount,mult.sfcount)
        #print("operands:",self.number, mult.number)
        result = SciSigFig(self.number * mult.number)
        return (result,min_sf)

    def divide(self,mult):
        min_sf = min(self.sfcount,mult.sfcount)
        result = SciSigFig(self.number / mult.number)
        print("answwer:",str(result))
        return (result,min_sf)
