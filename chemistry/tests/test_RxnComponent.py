import pytest
from pprint import pformat
import CHEMBOX.chemistry.RxnComponent as RC

def test_new_RxnComponent_primitive():
    component = RC.RxnComponent(3,"NaOH")
    print("RxnComponent:",str(component))
    assert True, "no ChemFormula tests yet"
