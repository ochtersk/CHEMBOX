import pytest
from pprint import pformat
import CHEMBOX.chemistry.Rxn as Rxn

def test_new_Rxn():
    components = Rxn.Rxn('O2 + 2H2 -> 2H2O')
    print(components.html)
    assert len(components.RxnReactants)==2, "reaction creation failed"

@pytest.mark.parametrize("reaction,string,representation",[
('7O2 + C6H5OH -> 6CO2 + 3H2O',"7O2 + C6H5OH -> 6CO2 + 3H2O is combustion",'Rxn("7O2 + C6H5OH -> 6CO2 + 3H2O")' ),
])
def test_Rxn_reps(reaction,string,representation):
    rxn = Rxn.Rxn(reaction)
    assert str(rxn)==string, "str() doesn't match"
    assert repr(rxn)==representation, "repr() doesn't match"

@pytest.mark.parametrize("reaction,rxntype",[
("ZnCl2 + H2S = ZnS + 2 HCl","double replacement"),
("Zn + 2 HCl = ZnCl2 + H2","single replacement"),
("10 KClO3 + 3 P4 = 3 P4O10 + 10 KCl","uncategorized"),
("2 Al(OH)3 + 3 H2CO3 = Al2(CO3)3 + 6 H2O","double replacement"),
("2 KOH + H2CO3 = 2 H2O + K2CO3","double replacement"),
("2 Na + 2 H2O = 2 NaOH + H2","single replacement"),
("2 NaOH + H2 = 2 Na + 2 H2O","single replacement"),
("2 PbO + C = 2 Pb + CO2","single replacement"),
("3 Al + 3 NH4ClO4 = Al2O3 + AlCl3 + 3 NO + 6 H2O","uncategorized"),
("2 C10H22 + 31 O2 = 20 CO2 + 22 H2O","combustion"),
])
def test_rxn_categorization(reaction,rxntype):
    rxn = Rxn.Rxn(reaction)
    assert rxn.RxnType==rxntype, "RxnType doesn't match"

def regenerate_cleaned_rxns():
    with open('RXN/no_state_raw.txt', "r") as file_object:
        # read file content
        print('@pytest.mark.parametrize("reaction,rxntype",[')
        for line in file_object.readlines():
            cleanLine= line.rstrip()
            components = Rxn.Rxn(cleanLine)
            print(f"(\"{cleanLine}\",\"{components.RxnType}\"),")
        print('])')
