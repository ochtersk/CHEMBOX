import pytest
from pprint import pformat
import chemistry.ChemTypes as CT

@pytest.mark.parametrize("formula,type",[
("H2O","water"),
("HOH","water"),
("Ca", "element"),
("H2", "element"),
("CaCl2","ionic"),
("NH4Cl","ionic"),
("(NH4)S","ionic"),
("HCl","acid"),
("CO2","covalent"),
("H2SO4","acid"),
("O2", "oxygen"),
("Cl2","element"),
("C6H5OH","hydrocarbon"),
("N2O3","covalent")
])
def test_ChemTypes(formula,type):
    foundtype = CT.detectChemicalType(formula)
    assert foundtype == type, f"{formula} failed found:{foundtype} wanted:{type}"
