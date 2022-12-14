from pprint import pformat
from pyvalem.reaction import Reaction
import chemistry.RxnComponent as RC

class Rxn(Reaction):
    """Rxn class for ChemBox to handle reactions

    Attributes
    ----------
    RxnEquation : text version of the reeaction equation
    RxnReactants : list of RxnComponent reactants
    RxnProducts : list of RxnComponent products
    RxnDifficulty : level of difficutly for balancing
    RxnType : text -
           single replacement|double replacement|synthesis|decomposition|combustion|uncategorized


    Public Methods
    --------------
    __init__ create a new ChemForula with the supplied formula, charge and name:
                - formula: a chemical formula in text format, like Co3(PO4)2
                - charge : optional charge (zero is the default)
                - name : optional name of the compound
         Raises: ChemFormula Error

    __str__  give a string representation of the formula in plain text
    __repr__ give a string representation of code to recreate the RxnComponent object


    """
    def __init__(self, reactionText):
        super().__init__(reactionText)
        self.reaction = self._parseReaction(reactionText)
        self.RxnEquation = reactionText


    def __repr__(self):
        string=f"Rxn(\"{self.RxnEquation}\")"
        return string

    def __str__(self):
        string=f"{self.RxnEquation}"
        return string

    def _parseReaction(self,reactionText):
        verbose = False
        if verbose: print(f"_parseReaction: {reactionText}")
        reaction = Reaction(reactionText)
        if verbose:
            print(f"Reaction.reactants: {pformat(reaction.reactants)}")
            print(f"Reaction.products: {pformat(reaction.products)}")
        return reaction

    def _getFormulas(self,componentList):
        formulas =[RC.RxnComponent(x[0],str(x[1])) for x in componentList]
        return formulas

    def RxnReactants(self):
        return self._getFormulas(self.reactants)

    def RxnProducts(self):
        return self._getFormulas(self.products)


    def detectRxnType(self):
        #XXX refactor this
        verbose = False
        reactantSet = { x.chemicalType for x in self.RxnReactants()}
        productSet = { x.chemicalType for x in self.RxnProducts()}
        if verbose: print(f"reaction: {self.RxnEquation}")
        if verbose: print(f"reactant set:{pformat(reactantSet)}")
        if verbose: print(f"product  set:{pformat(productSet)}")
        rxnType = "uncategorized"

        if reactantSet == {"oxygen","hydrocarbon"}:
            rxnType = "combustion"

        if reactantSet == {"water","element"} and productSet=={"ionic","element"}:
            rxnType = "single replacement"
        if reactantSet == {"ionic","element"} and productSet=={"water","element"}:
            rxnType = "single replacement"
        if reactantSet == {"ionic","element"} and productSet=={"ionic","element"}:
            rxnType = "single replacement"
        if reactantSet == {"ionic","element"} and productSet=={"covalent","element"}:
            rxnType = "single replacement"
        if reactantSet == {"acid","element"} and productSet=={"ionic","element"}:
            rxnType = "single replacement"

        if reactantSet == {"ionic"} and len(self.reactants) ==2 and len(self.products) ==2:
            rxnType = "double replacement"
        if reactantSet == {"ionic","acid"} and len(self.reactants) ==2 and len(self.products) ==2:
            rxnType = "double replacement"

        if len(self.reactants) == 1 and len(self.products) > 1:
            rxnType = "decomposition"

        if len(self.reactants) > 1 and len(self.products) == 1:
            rxnType = "synthesis"
        return rxnType
