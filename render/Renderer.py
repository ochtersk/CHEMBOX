from pprint import pformat
import CHEMBOX.chemplates.Chemplate as CP
import CHEMBOX.refdata.DataValue as DV
import CHEMBOX.chemplates.ChemplateUtils as CPU


def is_correct(target_item):
    """ is_correct(target_item) returns true if this is a correct answer) """
    assert isinstance(target_item,CP.Chemplate)
    if target_item.existsIDattr("correct","value"):
        return target_item.getIDvalue("correct") == "true"
    else:
        return False

def render_item_to_string(target_item, print_list=None):
    """ render_item_to_string(target_item, print_list) renders and returns a string
            representation of a Chemplate answer.
            If the answer is incorrect, it forcres the units to be those given
            in the Chemplate
     print_list - a list of modifiers, which can alter the output txt:
            Implemented so far:
            'text' - append on the value of the 'text' ID in the Chemplate
    """
    assert isinstance(target_item,CP.Chemplate)
    verbose = False
    if verbose:
        print("PRINT_LIST:",pformat(print_list))
    if print_list is None:
        print_list = []
    if is_correct(target_item):
        if (verbose): print("answer item is correct")
        answer_str = str(target_item.getIDvalue("value"))
    else:
        value = target_item.getIDvalue("value")
        if (verbose): print("answer item is incorrect",value)
        if isinstance(value, DV.DataValue):
            magnitude = value.magnitude
            units = target_item.getIDvalue("units")
            value = DV.DataValue(magnitude = str(magnitude), units = units)
        answer_str = str(value)
    if "text" in print_list:
        answer_str += " " + target_item.getIDvalue("text")

    return answer_str

def _gettoken(c,chars,knownsigils):
    """returns a token following a knownsigil, and the next character in chars
    """
    verbose = False
    token = None
    if (c!= "end"):
        toktext = []
        matches = knownsigils[c][0]
        toktype = knownsigils[c][1]
        if verbose: print("BEF toktype:",toktype," matches:",matches)
        while (True):
            c = next(chars, "end")
            if verbose: print("c->",c)
            if c in matches:
                toktext.append(c)
            else:
                break
        if verbose: print("AFT toktype:",toktype," toktext:",toktext)
        token = (''.join(toktext), toktype)
    return (c,token)


def post_process(text):
    """ post_process(text,output_target) post processes text strings and returns
            a list of formatiing requests as tuples
            Formating sigils:
            ^ superscript trailing digits and "+" or "-"
            _ subscript trailing digits
    input - a text string
          example: "ion: CH_3^1+"

    output - returns a list of text and formatting request tuples:
         example:
        [
         ("ion: CH", "NORMAL"),
         ("3", "SUBSCRIPT"),
         ("1+", "SUPERSCRIPT")
        ]
    """
    verbose = False
    request_list = []
    chars = iter(text)
    normal_text = []
    knownsigils = {"end":('',"NONE"),
                    "^": ("0123456789+-","SUPERSCRIPT"),
                    "_": ("0123456789","SUBSCRIPT")
                    }
    c = next(chars, "end")
    while (True):
        if (c in knownsigils.keys()):
            if len(normal_text): request_list.append((''.join(normal_text), "NORMAL"))
            normal_text.clear()
            (c,token) = _gettoken(c,chars,knownsigils)
            if (token is not None): request_list.append(token)
            if (c=="end"):
                break
            else:
                continue
        else:
            normal_text.append(c)
        c = next(chars, "end")
    return request_list
