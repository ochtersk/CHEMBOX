from pprint import pformat
from pyvalem.formula import Formula
import CHEMBOX.chemistry.ChemTypes as CT

class RxnComponent(Formula):
    """RxnComponent class for ChemBox to handle reactants and products

    Attributes
    ----------
    formula : text version of formula
    coefficient : stoichiometric coefficient
    chemicalType : text - ionic|covalent|element|acid|water


    Public Methods
    --------------
    __init__ create a new ChemFormula with the supplied formula, charge and name:
                - formula: a chemical formula in text format, like Co3(PO4)2
                - charge : optional charge (zero is the default)
                - name : optional name of the compound
         Raises: ChemFormula Error

    __str__  give a string representation of the formula in plain text
    __repr__ give a string representation of code to recreate the RxnComponent object


    """
    def __init__(self, coefficient, formula):
        #print(f"RxnC init:{coefficient}< f:{formula}<")
        super().__init__(formula)
        self.coefficient = coefficient
        self.chemicalType = CT.detectChemicalType(formula)


#    def __str__(self):
#        string=f"coefficient:{self.coefficient} formula:{self.formula} type:{self.chemicalType}"
#        return string

#    __repr__= __str__
