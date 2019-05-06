import itertools

class DataValue():
    """Data Value class for ChemBox.
        holds magnitue and units
        units are in two parts: numerator and denominator
    """
    def __init__(self, mag , numer, denom):
        self.magnitude = mag
        self.units_numerator = numer
        self.units_denominator = denom

    def __str__(self):
        return f'DataValue: {self.magnitude} {self.units_numerator}/{self.units_denominator}'



# class Chemical():
#     newChemid = itertools.count().next
#     """ Chemical class for ChemBox
#         hold identification and formula data
#         it takes an optional list of structural formulas
#     """
#     def __init__(self, name, formula, structural_formulas=None)
#     self.id = resource_cl.newid()
#     self.name = name
#     self.formula = formula
#     if structural_formulas is None:
#         self.structural_formulas = []
#     else:
#         self.structural_formulas = structural_formulas
#
#
#
#
#
# class ReferenceDataPoint(object):
#     """Reference data class for ChemBox. Someday, this should be a database."""
#     def __init__(self, arg):
#         superrefdata, self).__init__()
#         self.arg = arg
#         self.chemical = None
#         self.property_name = None
#         self.property_value = DataValue()
