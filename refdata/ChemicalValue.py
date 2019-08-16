import itertools

class ChemicalValue():
    """ ChemicalValue class for ChemBox to hold chemical identification info

        Properties:
        a unique identifier and formula data ()
        it takes an optional list of structural formulas
    """

    newChemid = itertools.count().next
    def __init__(self, name, formula, structural_formulas=None)
    self.id = resource_cl.newid()
    self.name = name
    self.formula = formula
    if structural_formulas is None:
        self.structural_formulas = []
    else:
        self.structural_formulas = structural_formulas
