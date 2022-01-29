from pprint import pformat
import pyparsing as pp
from .element_lists import element_symbols, ionic_metal_symbols, ammonium_formula

def detectChemicalType(formula):
    """detectChemicalType: utility routine for detecting chemical type

    Arguments
    ----------
    formula : text version of formula

    Returns
    -------
    type: string "element"|"ionic"|"covalent"|"acid"|"water"

    """
    verbose = False
    #if verbose: print(f"detect formula:{formula}")
    if formula in ['H2O','HOH']:
        return "water"
    if formula == 'O2':
        return "oxygen"

    integer = pp.Word(pp.nums)
    element = pp.StringStart()+pp.oneOf(element_symbols)+pp.Optional(integer)+pp.StringEnd()
    try:
        parts = element.parseString(formula)
        return "element"
    except pp.ParseException:
            pass

    ammonium_formulas = [ammonium_formula,'('+ammonium_formula+')']
    cation = pp.StringStart()+pp.oneOf(ionic_metal_symbols)
    try:
        parts = cation.parseString(formula)
        return "ionic"
    except pp.ParseException:
        pass

    hydrocarbon_formula = [ammonium_formula,'('+ammonium_formula+')']
    integer_or_hco = pp.Word("HC","CHO1234567890")
    hydrocarbon = pp.StringStart()+integer_or_hco+pp.StringEnd()
    if formula in ["CO2","CO"]: return "covalent"
    if formula in ["H2CO3"]: return "ionic"
    try:
        parts = hydrocarbon.parseString(formula)
        return "hydrocarbon"
    except pp.ParseException:
        pass


    ammonium_formulas = [ammonium_formula,'('+ammonium_formula+')']
    polycation = pp.StringStart()+pp.oneOf(ammonium_formulas)
    try:
        parts = polycation.parseString(formula)
        return "ionic"
    except pp.ParseException:
        pass


    acid = pp.StringStart()+pp.Char('H') + pp.NotAny(pp.oneOf('e o f g s'))
    try:
        parts = acid.parseString(formula)
        return "acid"
    except pp.ParseException:
        pass

    return "covalent"
